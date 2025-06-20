#!/usr/bin/env python3
"""
Site Visit Bot with Response Time Metrics

This script is based on simple_visit.py but includes:
1. Reduced wait time (2 minutes instead of 3min30s)
2. Bot response time metrics
3. Performance monitoring

It uses the Telethon library to interact with the Telegram API and
urllib.request for direct HTTP requests without opening a browser.
"""

import os
import sys
import logging
import asyncio
import time
import re
import urllib.request
import urllib.error
import ssl
import statistics
import random
from datetime import datetime
from dotenv import load_dotenv
from telethon import TelegramClient, events, errors, Button

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bot_visite.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables with fallbacks to original values
api_id = os.environ.get('TELEGRAM_API_ID', '22214283')
api_hash = os.environ.get('TELEGRAM_API_HASH', 'd3ebb9a92636d8b111564fa4db2ab8da')
phone = os.environ.get('TELEGRAM_PHONE', '+261333147872')

# Target bot username
TARGET_BOT = 'BTC_CIickersBot'

class SiteVisitBot:
    """A Telegram client to automate site visits with response time tracking."""
    
    def __init__(self, api_id, api_hash, phone):
        """Initialize the Telegram client with credentials."""
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone = phone
        self.client = None
        self.last_message = None
        self.visit_in_progress = False  # Flag to track visit state
        self.go_to_site_clicked = False  # Flag to track if Go to Site was clicked
        self.current_url = None  # Store the current URL being visited
        self.restart_scheduled = False  # Flag to prevent duplicate auto-restarts
        self.fake_attempts_count = 0  # Counter for fake attempt errors
        self.in_cooldown = False  # Flag for cooldown period after fake attempts
        self.cooldown_until = None  # Timestamp when cooldown ends
        
        # Performance metrics
        self.response_times = []
        self.last_command_time = None
        self.bot_response_times = []
        self.active_messages = []  # Store active messages from the bot
        self.bot_status_messages = []  # Store bot status messages
        
    async def start(self):
        """Start the Telegram client and set up event handlers."""
        try:
            self.client = TelegramClient('session_name', self.api_id, self.api_hash)
            
            # Record start time for initial connection
            connection_start = time.time()
            
            await self.client.start(self.phone)
            
            # Calculate connection time
            connection_time = time.time() - connection_start
            logger.info(f"Client started successfully in {connection_time:.2f} seconds")
            self.bot_status_messages.append(f"Bot connected in {connection_time:.2f} seconds")
            
            # Set up event handler for incoming messages
            @self.client.on(events.NewMessage(from_users=TARGET_BOT))
            async def handler(event):
                """Handle responses from the target bot with timing."""
                # Calculate response time if we have a last command time
                if self.last_command_time:
                    response_time = time.time() - self.last_command_time
                    self.bot_response_times.append(response_time)
                    self.last_command_time = None
                    logger.info(f"Bot response time: {response_time:.2f} seconds")
                    logger.info(f"Bot response time: {response_time:.2f} seconds")
                    self.bot_status_messages.append(f"Bot response time: {response_time:.2f} seconds")
                
                logger.info(f"Received message: {event.message.text}")
                self.last_message = event.message
                self.active_messages.append(f"Bot: {event.message.text[:50]}..." if len(event.message.text) > 50 else f"Bot: {event.message.text}")
                
                # Keep only the last 5 messages
                if len(self.active_messages) > 5:
                    self.active_messages = self.active_messages[-5:]
                    
                # Check for "wait 1min 30" message to auto-restart
                if "wait" in event.message.text.lower() and ("1min 30" in event.message.text.lower() or "1min30" in event.message.text.lower() or "1 min 30" in event.message.text.lower()):
                    logger.info("Detected 'wait 1min 30' message - scheduling auto-restart")
                    self.bot_status_messages.append("Detected wait message - scheduling auto-restart")
                    
                    # Only schedule if not already scheduled
                    if not self.restart_scheduled:
                        # Add a buffer to the wait time (100 seconds = ~1min 40s)
                        asyncio.create_task(self.restart_after_delay(100))
                        self.restart_scheduled = True
                        
                # Check for "Too many fake attempts" message
                elif "fake attempts" in event.message.text.lower() or "too many fake" in event.message.text.lower():
                    logger.warning("Detected 'Too many fake attempts' message")
                    self.bot_status_messages.append("⚠️ Detected 'Too many fake attempts'")
                    
                    # Increment the counter and determine cooldown period
                    self.fake_attempts_count += 1
                    
                    # Calculate cooldown time based on number of fake attempts (exponential backoff)
                    cooldown_seconds = min(30 * (2 ** (self.fake_attempts_count - 1)), 600)  # Max 10 minutes
                    
                    logger.info(f"Entering cooldown for {cooldown_seconds} seconds (attempt #{self.fake_attempts_count})")
                    self.bot_status_messages.append(f"Cooldown: {cooldown_seconds}s (attempt #{self.fake_attempts_count})")
                    
                    # Set cooldown flags
                    self.in_cooldown = True
                    self.cooldown_until = time.time() + cooldown_seconds
                    
                    # Reset visit flags
                    self.visit_in_progress = False
                    self.go_to_site_clicked = False
                    
                    # Schedule restart after cooldown
                    if not self.restart_scheduled:
                        # Add a small random buffer (5-15 seconds) to the cooldown
                        buffer = random.randint(5, 15)
                        asyncio.create_task(self.restart_after_delay(cooldown_seconds + buffer))
                        self.restart_scheduled = True
                        print(f"\n⚠️ Too many fake attempts detected. Cooling down for {cooldown_seconds + buffer} seconds...")
                        print("⚠️ Bot will automatically restart after cooldown")
                # Look for URLs in the message text
                if "http" in event.message.text:
                    urls = re.findall(r'(https?://\S+)', event.message.text)
                    if urls:
                        self.current_url = urls[0]
                        logger.info(f"Extracted URL from message: {self.current_url}")
                        self.bot_status_messages.append(f"URL: {self.current_url}")
                
                # If there are buttons, process them
                if event.message.buttons:
                    logger.info("Message has buttons - processing")
                    await self.process_message_with_buttons(event.message)
                else:
                    logger.info("Message has no buttons, checking if it contains error message")
                    # Check for error messages that might indicate failure
                    if "sorry" in event.message.text.lower() and "not visited" in event.message.text.lower():
                        logger.warning("Detected 'not visited' error message")
                        print("\n❌ Error: Site not visited properly!")
                        print("Restarting the process...")
                        self.bot_status_messages.append("Error: Site not visited properly - Restarting")
                        # Reset flags
                        self.visit_in_progress = False
                        self.go_to_site_clicked = False
                        await asyncio.sleep(2)
                        await self.start_process()
                
            return True
        except Exception as e:
            logger.error(f"Error starting client: {e}")
            self.bot_status_messages.append(f"Error: {str(e)}")
            return False
    
    async def start_process(self):
        """Start the site visit process by sending the /earn command."""
        try:
            # Check if we're in cooldown period
            if self.in_cooldown:
                current_time = time.time()
                if current_time < self.cooldown_until:
                    remaining = int(self.cooldown_until - current_time)
                    logger.info(f"Still in cooldown period. {remaining} seconds remaining.")
                    self.bot_status_messages.append(f"Cooldown: {remaining}s remaining")
                    print(f"\n⏳ Still in cooldown. Waiting {remaining} seconds before restarting...")
                    return False
                else:
                    # Cooldown period is over
                    self.in_cooldown = False
                    logger.info("Cooldown period completed")
                    self.bot_status_messages.append("Cooldown completed, restarting")
            
            # Reset the flags when starting a new process
            self.visit_in_progress = False
            self.go_to_site_clicked = False
            
            # Record command time for response timing
            self.last_command_time = time.time()
            
            await self.client.send_message(TARGET_BOT, '/earn')
            logger.info("Started site visit process with /earn command")
            self.bot_status_messages.append("Process started with /earn command")
            return True
        except Exception as e:
            logger.error(f"Error starting process: {e}")
            self.bot_status_messages.append(f"Error: {str(e)}")
            return False

    async def process_message_with_buttons(self, message):
        """Process a message with buttons to find and click appropriate buttons."""
        try:
            # Log all available buttons for debugging
            if message.buttons:
                logger.info("Available buttons:")
                for row_idx, row in enumerate(message.buttons):
                    for btn_idx, button in enumerate(row):
                        logger.info(f"Button [{row_idx}][{btn_idx}]: {button.text}")
            else:
                logger.info("Message has no buttons")
                return
            
            # If we're waiting for the "Visited" button after timer completion
            # Don't process any buttons during regular flow - let wait_and_click_visited handle it
            if self.go_to_site_clicked and not self.visit_in_progress:
                logger.info("Waiting for wait_and_click_visited to handle the 'Visited' button")
                return
                
            # First priority: Look for "Visit sites" button (🖥 Visit sites)
            # Only click this if we're not in the middle of a visit
            if not self.visit_in_progress and await self.click_button_if_exists(message, ["Visit sites", "🖥"], ignore_visited=True):
                logger.info("Clicked 'Visit sites' button")
                self.bot_status_messages.append("Clicked 'Visit sites' button")
                return
            
            # Second priority: Look for "Go to site" button (🌐 Go to site)
            # Only click this if we haven't already clicked it and we're not in a visit
            if not self.visit_in_progress and not self.go_to_site_clicked:
                # Look specifically for the Go to Site button
                for row_idx, row in enumerate(message.buttons):
                    for btn_idx, button in enumerate(row):
                        if button.text == "\U0001F310 Go to Site":
                            logger.info(f"Found exact 'Go to Site' button at position [{row_idx}][{btn_idx}]")
                            try:
                                # Record time before clicking
                                click_start_time = time.time()
                                
                                # Click the button
                                await message.click(row_idx, btn_idx)
                                
                                # Calculate button click response time
                                click_response_time = time.time() - click_start_time
                                logger.info(f"Button click response time: {click_response_time:.2f} seconds")
                                self.bot_status_messages.append(f"'Go to Site' clicked in {click_response_time:.2f} seconds")
                                
                                logger.info("Clicked 'Go to Site' button")
                                
                                # Update flags to indicate visit has started
                                self.visit_in_progress = True
                                self.go_to_site_clicked = True
                                
                                # Print status message
                                print("\n" + "="*50)
                                print("🔄 Starting site visit simulation...")
                                print("🔄 Making direct HTTP requests to the site")
                                print("🔄 All activity happens in background - no UI needed")
                                print("="*50 + "\n")
                                
                                # Start HTTP request in the background
                                asyncio.create_task(self.simulate_site_visit())
                                
                                # Allow a moment for the request to start
                                await asyncio.sleep(2)
                                
                                # Wait 2 minutes (120 seconds) and then click "Visited"
                                await self.wait_and_click_visited()
                                return
                            except Exception as e:
                                logger.error(f"Error clicking 'Go to Site' button: {e}")
                                self.bot_status_messages.append(f"Error: {str(e)}")
            
            # DO NOT look for "Visited" button here - it's handled in wait_and_click_visited
            logger.info("No relevant buttons found in this message")
        except Exception as e:
            logger.error(f"Error processing message with buttons: {e}")
            logger.error(f"Exception details: {str(e)}")
            self.bot_status_messages.append(f"Error processing buttons: {str(e)}")
            import traceback
            logger.error(f"Traceback: {traceback.format_exc()}")

    async def click_button_if_exists(self, message, button_texts, ignore_visited=False):
        """Click a button if any of the texts are found in it."""
        if not message or not message.buttons:
            logger.warning("No message or buttons to process")
            return False
            
        # NEVER allow clicking "Visited" button during normal flow
        # It should ONLY be clicked after the timer in wait_and_click_visited
        if not ignore_visited:
            # Check if we're trying to click a Visited button
            is_visited_button = False
            for text in button_texts:
                if "Visited" in text or "✅" in text:
                    is_visited_button = True
                    break
                    
            if is_visited_button:
                # Only allow Visited button clicks if:
                # 1. Go to Site was clicked first
                # 2. The visit is not in progress (timer completed)
                # 3. We're being called from wait_and_click_visited (after timer)
                if self.visit_in_progress:
                    logger.info("BLOCKED: Not clicking 'Visited' button because visit is still in progress")
                    return False
                    
                if not self.go_to_site_clicked:
                    logger.info("BLOCKED: Not clicking 'Visited' button because 'Go to Site' was not clicked first")
                    return False
                
                # If we get here, it's OK to click Visited (timer complete, Go to Site was clicked)
                logger.info("Visited button click is allowed now that timer is complete")
            
        try:
            # Check if we're looking for Visited button
            looking_for_visited = not ignore_visited and any(text in ["Visited", "✅", "✅ Visited"] for text in button_texts)
            
            # If looking for Visited button, do an exact match pass first
            if looking_for_visited:
                # Triple safety check
                if self.visit_in_progress:
                    logger.info("BLOCKED: Skipping Visited button check because visit is still in progress")
                    return False
                
                if not self.go_to_site_clicked:
                    logger.info("BLOCKED: Skipping Visited button check because Go to Site wasn't clicked first")
                    return False
                    
                # First do an exact match pass - specifically for "✅ Visited"
                for row_idx, row in enumerate(message.buttons):
                    for btn_idx, button in enumerate(row):
                        # Check for exact match with "✅ Visited" first
                        if button.text == "✅ Visited":
                            logger.info(f"Found exact match for '✅ Visited' button at position [{row_idx}][{btn_idx}]")
                            try:
                                # Record time before clicking
                                click_start_time = time.time()
                                
                                await message.click(row_idx, btn_idx)
                                
                                # Calculate button click response time
                                click_response_time = time.time() - click_start_time
                                logger.info(f"'Visited' button click response time: {click_response_time:.2f} seconds")
                                self.bot_status_messages.append(f"'Visited' clicked in {click_response_time:.2f} seconds")
                                
                                logger.info(f"[EXACT MATCH] Clicked button at position [{row_idx}][{btn_idx}]: {button.text}")
                                # Add a small delay after clicking
                                await asyncio.sleep(0.5)
                                return True
                            except Exception as e:
                                logger.error(f"Error clicking exact match button: {e}")
                                # Try alternative method
                                try:
                                    # Try directly using the button object as a fallback
                                    await button.click()
                                    logger.info(f"[ALTERNATIVE] Clicked '✅ Visited' button using direct button click")
                                    await asyncio.sleep(0.5)
                                    return True
                                except Exception as e2:
                                    logger.error(f"Alternative clicking method also failed: {e2}")
            
            # If exact match didn't succeed, try partial matches
            for row_idx, row in enumerate(message.buttons):
                for btn_idx, button in enumerate(row):
                    button_text = button.text.strip()
                    logger.info(f"Checking button at [{row_idx}][{btn_idx}]: '{button_text}'")
                    
                    # Check against our search texts
                    for text in button_texts:
                        # For "Go to Site", use exact match for better precision
                        if text == "\U0001F310 Go to Site" and button_text == "\U0001F310 Go to Site":
                            logger.info(f"Found exact match for 'Go to Site' button: '{button_text}'")
                            try:
                                # Record time before clicking
                                click_start_time = time.time()
                                
                                await message.click(row_idx, btn_idx)
                                
                                # Calculate button click response time
                                click_response_time = time.time() - click_start_time
                                logger.info(f"Button click response time: {click_response_time:.2f} seconds")
                                self.bot_status_messages.append(f"Button clicked in {click_response_time:.2f} seconds")
                                
                                logger.info(f"Clicked 'Go to Site' button at position [{row_idx}][{btn_idx}]")
                                await asyncio.sleep(0.5)
                                return True
                            except Exception as e:
                                logger.error(f"Error clicking 'Go to Site' button: {e}")
                        # Skip Visited buttons in regular flow (only process in wait_and_click_visited)
                        elif not ignore_visited and ("Visited" in text or "✅" in text):
                            logger.info(f"Skipping Visited button during regular flow")
                            continue
                        # For other buttons, use partial match
                        elif text in button_text:
                            try:
                                # Record time before clicking
                                click_start_time = time.time()
                                
                                # Click by row and column index instead of passing the button object directly
                                await message.click(row_idx, btn_idx)
                                
                                # Calculate button click response time
                                click_response_time = time.time() - click_start_time
                                logger.info(f"Button click response time: {click_response_time:.2f} seconds")
                                self.bot_status_messages.append(f"Button clicked in {click_response_time:.2f} seconds")
                                
                                logger.info(f"Clicked button at position [{row_idx}][{btn_idx}]: '{button_text}'")
                                await asyncio.sleep(0.5)
                                return True
                            except Exception as e:
                                logger.error(f"Error clicking button by index: {e}")
                                # Try alternative method
                                try:
                                    # Try directly using the button object as a fallback
                                    await button.click()
                                    logger.info(f"Clicked button using direct button click: '{button_text}'")
                                    await asyncio.sleep(0.5)
                                    return True
                                except Exception as e2:
                                    logger.error(f"Alternative clicking method also failed: {e2}")
            # If we reach here, no matching button was found
            logger.warning(f"No button matching any of {button_texts} was found")
            return False
        except Exception as e:
            logger.error(f"Error in click_button_if_exists: {e}")
            self.bot_status_messages.append(f"Error: {str(e)}")
            import traceback
            logger.error(f"Traceback: {traceback.format_exc()}")
            return False

    async def _search_and_click(self, message_texts, max_attempts=5, delay=2):
        """
        Helper method to search for and click a button with any of the specified texts.
        Repeatedly tries to find the button in recent messages.
        
        Args:
            message_texts: List of text strings to look for in buttons
            max_attempts: Maximum number of attempts to find the button
            delay: Delay in seconds between attempts
            
        Returns:
            True if button was found and clicked, False otherwise
        """
        logger.info(f"Searching for buttons with any of these texts: {message_texts}")
        
        for attempt in range(1, max_attempts + 1):
            logger.info(f"Button search attempt {attempt}/{max_attempts}")
            
            try:
                # Get the most recent messages that might contain our button
                messages = await self.client.get_messages(TARGET_BOT, limit=3)
                
                # Look through each message for buttons
                for message in messages:
                    if message and message.buttons:
                        logger.info(f"Checking message ID {message.id} for buttons")
                        
                        # Log all buttons in this message
                        for row_idx, row in enumerate(message.buttons):
                            for btn_idx, button in enumerate(row):
                                logger.info(f"Button [{row_idx}][{btn_idx}]: '{button.text}'")
                                
                                # Check if this button matches any of our search texts (case-insensitive)
                                button_text = button.text.strip()
                                for text in message_texts:
                                    if text.lower() in button_text.lower() or button_text.lower() in text.lower():
                                        logger.info(f"Found matching button: '{button_text}' at position [{row_idx}][{btn_idx}]")
                                        
                                        try:
                                            # Record time before clicking
                                            click_start_time = time.time()
                                            
                                            # Attempt to click by index
                                            await message.click(row_idx, btn_idx)
                                            
                                            # Calculate click response time
                                            click_response_time = time.time() - click_start_time
                                            logger.info(f"Button click response time: {click_response_time:.2f} seconds")
                                            self.bot_status_messages.append(f"Button clicked in {click_response_time:.2f} seconds")
                                            
                                            logger.info(f"Successfully clicked button on attempt {attempt}/{max_attempts}")
                                            return True
                                        except Exception as e:
                                            logger.error(f"Error clicking button by index: {e}")
                                            
                                            # Try alternative method
                                            try:
                                                # Try directly using the button object as a fallback
                                                await button.click()
                                                logger.info(f"Clicked button using direct button click: '{button_text}'")
                                                logger.info(f"Successfully clicked button on attempt {attempt}/{max_attempts} (alternative method)")
                                                return True
                                            except Exception as e2:
                                                logger.error(f"Alternative clicking method also failed: {e2}")
            
            except Exception as e:
                logger.error(f"Error in _search_and_click method: {e}")
                self.bot_status_messages.append(f"Error: {str(e)}")
    
    async def restart_after_delay(self, seconds):
        try:
            # Add a small random offset to the delay to appear more human-like
            random_offset = random.uniform(-3.0, 3.0)
            adjusted_seconds = max(1, seconds + random_offset)
            
            logger.info(f"Auto-restart scheduled in {adjusted_seconds:.1f} seconds")
            self.bot_status_messages.append(f"Auto-restart in {adjusted_seconds:.1f}s")
            
            # Wait for the specified delay
            await asyncio.sleep(adjusted_seconds)
            
            logger.info("Auto-restart delay complete, restarting process")
            self.bot_status_messages.append("Auto-restarting process with /earn")
            
            # Reset flags
            self.visit_in_progress = False
            self.go_to_site_clicked = False
            
            # Call start_process to send /earn
            await self.start_process()
            
            # Reset the restart flag so we can schedule another restart if needed
            self.restart_scheduled = False
            logger.info("Auto-restart delay complete, restarting process")
            self.bot_status_messages.append("Auto-restarting process with /earn")
            
            # Reset flags
            self.visit_in_progress = False
            self.go_to_site_clicked = False
            
            # Call start_process to send /earn
            await self.start_process()
            
            # Reset the restart flag so we can schedule another restart if needed
            self.restart_scheduled = False
            
        except Exception as e:
            logger.error(f"Error in auto-restart: {e}")
            self.bot_status_messages.append(f"Auto-restart error: {str(e)}")
            self.restart_scheduled = False
    
    async def wait_and_click_visited(self):
        """Wait for 2 minutes and then click the 'Visited' button."""
        try:
            # Safety check - only proceed if we've clicked "Go to Site"
            if not self.go_to_site_clicked:
                logger.warning("wait_and_click_visited called but Go to Site was not clicked first")
                return
                
            # Double-check we're in a visit
            if not self.visit_in_progress:
                logger.warning("wait_and_click_visited called but visit_in_progress is False")
                return
                
            logger.info("Waiting 2 minutes before clicking 'Visited'...")
            print("\n⏳ COUNTDOWN TIMER STARTED ⏳")
            print("HTTP requests are running in the background...")
            
            # Changed from 210 seconds (3min30s) to 120 seconds (2min)
            total_seconds = 120
            start_time = time.time()
            
            for remaining in range(total_seconds, 0, -1):
                # Calculate minutes and seconds for display
                mins, secs = divmod(remaining, 60)
                timeformat = f"{mins:02d}:{secs:02d}"
                
                # Create a progress bar
                progress_percentage = 100 - (remaining / total_seconds * 100)
                bar_length = 30
                filled_length = int(bar_length * (progress_percentage / 100))
                bar = '█' * filled_length + '░' * (bar_length - filled_length)
                
                # Create a visually appealing timer display
                timer_display = f"⏱️ Time remaining: {timeformat} [{bar}] {progress_percentage:.1f}%"
                
                # Print to console and log
                print(f"\r{timer_display}", end="", flush=True)
                
                # Give reminders at specific intervals
                if remaining == 90:  # At 1:30 remaining
                    print("\n🔄 1 minute 30 seconds left! HTTP connection maintained.")
                    self.bot_status_messages.append("1:30 remaining - HTTP active")
                elif remaining == 60:  # At 1 minute remaining
                    print("\n🔄 1 minute left! HTTP connection maintained.")
                    self.bot_status_messages.append("1:00 remaining - HTTP active")
                elif remaining == 30:  # At 30 seconds remaining
                    print("\n🔄 30 seconds left! Continuing HTTP activity.")
                    self.bot_status_messages.append("0:30 remaining - HTTP active")
                elif remaining == 15:  # At 15 seconds remaining
                    print("\n🔄 15 seconds left! Continuing HTTP activity.")
                    self.bot_status_messages.append("0:15 remaining - HTTP active")
                elif remaining == 10:  # At 10 seconds remaining
                    print("\n🔄 10 seconds left! Preparing to finish HTTP requests.")
                    self.bot_status_messages.append("0:10 remaining - Preparing to finish")
                elif remaining <= 5:  # Final countdown
                    logger.info(f"Waiting: {timeformat} remaining until clicking 'Visited'")
                await asyncio.sleep(1)
                
            # Calculate actual wait time
            actual_wait_time = time.time() - start_time
            logger.info(f"Actual wait time: {actual_wait_time:.2f} seconds")
            self.bot_status_messages.append(f"Wait completed in {actual_wait_time:.2f} seconds")
                
            # Final message when timer completes
            print("\n✅ Timer complete! Site visit simulated successfully.")
            print("\n" + "="*50)
            print("🔄 HTTP requests completed.")
            print("🔄 Now clicking the 'Visited' button automatically.")
            print("🔄 No manual interaction required in most cases.")
            
            # Mark visit as complete - now we can click "Visited"
            self.visit_in_progress = False
            
            # Give the user a moment to switch back to Telegram
            await asyncio.sleep(3)
            
            logger.info("Visit complete, now looking for 'Visited' button")
            
            # Request the latest message to ensure we have the current state
            try:
                # Record time before getting messages
                msg_fetch_start = time.time()
                
                # Get recent messages to make sure we have the latest one with the Visited button
                messages = await self.client.get_messages(TARGET_BOT, limit=5)
                
                # Calculate message fetch time
                msg_fetch_time = time.time() - msg_fetch_start
                logger.info(f"Message fetch time: {msg_fetch_time:.2f} seconds")
                self.bot_status_messages.append(f"Messages fetched in {msg_fetch_time:.2f} seconds")
                
                if messages and len(messages) > 0:
                    # Update last_message with the most recent message that has buttons
                    for msg in messages:
                        if msg.buttons:
                            self.last_message = msg
                            logger.info(f"Updated last_message with a recent message with buttons")
                            break
            except Exception as e:
                logger.error(f"Error getting recent messages: {e}")
                self.bot_status_messages.append(f"Error: {str(e)}")
            
            # Now look for the "Visited" button in the last message
            if self.last_message and self.last_message.buttons:
                logger.info("Looking for 'Visited' button after wait")
                
                # Record time before clicking
                visited_search_start = time.time()
                
                # Use our robust _search_and_click helper with multiple attempts
                logger.info("Using robust _search_and_click helper to find and click the 'Visited' button")
                
                # Try multiple button text variations for better matching with more attempts
                visited_button_texts = ["✅ Visited", "Visited", "✅"]
                if await self._search_and_click(visited_button_texts, max_attempts=10, delay=2):
                    logger.info("Successfully clicked 'Visited' button using robust search")
                    
                    # Calculate total 'Visited' button search and click time
                    total_visited_time = time.time() - visited_search_start
                    logger.info(f"Total 'Visited' button processing time: {total_visited_time:.2f} seconds")
                    self.bot_status_messages.append(f"Total 'Visited' processing: {total_visited_time:.2f} seconds")
                    
                    # Reset flags for next visit
                    self.go_to_site_clicked = False
                    self.visit_in_progress = False
                    
                    # Wait a moment then look for next site
                    await asyncio.sleep(3)
                    await self.start_process()
                    return
                
                # If robust search didn't work, try the original method as fallback
                logger.info("Robust search failed, trying original direct button detection as fallback")
                
                # Log the available buttons for debugging
                if self.last_message.buttons:
                    logger.info("Available buttons after wait:")
                    for row_idx, row in enumerate(self.last_message.buttons):
                        for btn_idx, button in enumerate(row):
                            logger.info(f"Button [{row_idx}][{btn_idx}]: '{button.text}'")
                            # Direct check: if we find the Visited button in last_message, click it directly
                            if "Visited" in button.text or "✅" in button.text:
                                logger.info(f"Found 'Visited' button directly at [{row_idx}][{btn_idx}]")
                                try:
                                    # Record time before clicking
                                    click_start_time = time.time()
                                    
                                    await self.last_message.click(row_idx, btn_idx)
                                    
                                    # Calculate button click response time
                                    click_response_time = time.time() - click_start_time
                                    logger.info(f"'Visited' button click response time: {click_response_time:.2f} seconds")
                                    self.bot_status_messages.append(f"'Visited' clicked in {click_response_time:.2f} seconds")
                                    
                                    logger.info(f"Direct click on 'Visited' button successful")
                                    # Reset flags for next visit
                                    self.go_to_site_clicked = False
                                    self.visit_in_progress = False
                                    
                                    # Calculate total 'Visited' button search and click time
                                    total_visited_time = time.time() - visited_search_start
                                    logger.info(f"Total 'Visited' button processing time: {total_visited_time:.2f} seconds")
                                    self.bot_status_messages.append(f"Total 'Visited' processing: {total_visited_time:.2f} seconds")
                                    
                                    # Wait a moment then look for next site
                                    await asyncio.sleep(3)
                                    await self.start_process()
                                    return
                                except Exception as e:
                                    logger.error(f"Error directly clicking 'Visited' button: {e}")
                                    self.bot_status_messages.append(f"Error: {str(e)}")
                
                # If direct button click didn't work, try using our helper method
                # Try multiple button text variations for better matching
                visited_button_texts = ["✅ Visited", "Visited", "✅"]
                if await self.click_button_if_exists(self.last_message, visited_button_texts):
                    logger.info("Successfully clicked 'Visited' button after waiting")
                    
                    # Calculate total 'Visited' button search and click time
                    total_visited_time = time.time() - visited_search_start
                    logger.info(f"Total 'Visited' button processing time: {total_visited_time:.2f} seconds")
                    self.bot_status_messages.append(f"Total 'Visited' processing: {total_visited_time:.2f} seconds")
                    
                    # Reset flags for next visit
                    self.go_to_site_clicked = False
                    self.visit_in_progress = False
                    # Wait a moment then look for next site
                    await asyncio.sleep(3)
                    await self.start_process()
                    return
                else:
                    # If we get here, all attempts to automatically click the Visited button failed
                    logger.info("All automated 'Visited' button attempts failed.")
                    print("\n❗ The bot couldn't automatically click the 'Visited' button.")
                    print("❗ Please try to click it manually if you see it.")
                    print("❗ Then press Enter to continue to the next site...")
                    
                    # Wait for user to acknowledge and manually click if needed
                    await self.wait_for_user_acknowledgment()
                    
                    # Continue to the next site
                    # Reset visit flags
                    self.visit_in_progress = False
                    self.go_to_site_clicked = False
                    await asyncio.sleep(1)
                    await self.start_process()
            else:
                logger.warning("No message with buttons found after waiting")
                # Inform the user
                print("\n❗ The bot couldn't find any buttons to click.")
                print("❗ Please check Telegram and click the 'Visited' button manually if you see it.")
                print("❗ Then press Enter to continue to the next site...")
                
                # Wait for user to acknowledge and manually click if needed
                await self.wait_for_user_acknowledgment()
                
                # Try to restart the process
                # Reset visit flags
                self.visit_in_progress = False
                self.go_to_site_clicked = False
                await asyncio.sleep(1)
                await self.start_process()
                
        except Exception as e:
            logger.error(f"Error in wait and click process: {e}")
            self.bot_status_messages.append(f"Error: {str(e)}")

    async def wait_for_user_acknowledgment(self):
        """Wait for user to press Enter as acknowledgment."""
        # Create a future that will be set when the user presses Enter
        future = asyncio.Future()
        
        def stdin_callback():
            input()  # Wait for Enter key
            if not future.done():
                future.set_result(None)
        
        # Add the input reader to the event loop
        loop = asyncio.get_event_loop()
        loop.add_reader(sys.stdin.fileno(), stdin_callback)
        
        try:
            # Wait for the future to be set
            await future
        finally:
            # Remove the reader when done
            loop.remove_reader(sys.stdin.fileno())
        
        return
    
    async def simulate_site_visit(self):
        """Simulate a site visit by making HTTP requests without opening a browser."""
        try:
            # Try to extract URL from last message if we don't have one
            if not self.current_url and self.last_message and hasattr(self.last_message, 'text'):
                urls = re.findall(r'(https?://\S+)', self.last_message.text)
                if urls:
                    self.current_url = urls[0]
                    logger.info(f"Extracted URL from last message: {self.current_url}")
                    self.bot_status_messages.append(f"URL: {self.current_url}")
            print("""
+------------------------------------------------------+
|       SITE VISIT BOT WITH RESPONSE TIME METRICS      |
|                                                      |
|  This bot will:                                      |
|  1. Click 'Go to Site' button in Telegram            |
|  2. Send HTTP requests directly to site (2 minutes)  |
|  3. Track bot response times and performance         |
|  4. Click 'Visited' button automatically             |
|  5. Auto-restart after "wait 1min 30" messages       |
|  6. Handle "fake attempts" with smart cooldowns      |
+------------------------------------------------------+
""")

            # Define a list of user agents to rotate through
            user_agents = [
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1',
                'Mozilla/5.0 (iPad; CPU OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64',
            ]
            
            # Select a random User-Agent
            selected_user_agent = random.choice(user_agents)
            logger.info(f"Using User-Agent: {selected_user_agent}")
            
            # Set headers to look like a real browser with more realistic parameters
            headers = {
                'User-Agent': selected_user_agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Pragma': 'no-cache',
                'Upgrade-Insecure-Requests': '1',
                'Referer': 'https://t.me/BTC_CIickersBot',  # Simulating coming from Telegram
            }
            
            # Create SSL context to handle HTTPS requests
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            
            # Track HTTP request response times
            http_response_times = []
            
            try:
                # Make the initial request with timing
                logger.info(f"Making HTTP request to: {self.current_url}")
                self.bot_status_messages.append(f"HTTP request to: {self.current_url}")
                
                # Time the request
                req_start_time = time.time()
                
                req = urllib.request.Request(self.current_url, headers=headers)
                with urllib.request.urlopen(req, timeout=10, context=ctx) as response:
                    status_code = response.getcode()
                    
                    # Calculate response time
                    req_time = time.time() - req_start_time
                    http_response_times.append(req_time)
                    
                    logger.info(f"Initial request status code: {status_code}, time: {req_time:.2f}s")
                    self.bot_status_messages.append(f"HTTP response: {status_code}, time: {req_time:.2f}s")
                    logger.info(f"Initial request status code: {status_code}, time: {req_time:.2f}s")
                    self.bot_status_messages.append(f"HTTP response: {status_code}, time: {req_time:.2f}s")
                
                # Make periodic requests to keep the connection active
                # For 2 minute wait, we'll make 4-6 requests with randomized timing
                # Randomize the number of requests (4-6) to appear more natural
                num_requests = random.randint(4, 6)
                logger.info(f"Will make {num_requests} HTTP requests with randomized timing")
                
                for i in range(num_requests):
                    if not self.visit_in_progress:
                        logger.info("Visit no longer in progress, stopping HTTP requests")
                        break
                    
                    # Randomized delay between 15-30 seconds to appear more human-like
                    delay = random.uniform(15, 30)
                    logger.info(f"Waiting {delay:.1f} seconds before next HTTP request")
                    await asyncio.sleep(delay)
                        
                    # Time the request
                    refresh_start_time = time.time()
                    
                    req = urllib.request.Request(self.current_url, headers=headers)
                    # For subsequent requests, randomize the User-Agent again
                    headers['User-Agent'] = random.choice(user_agents)
                    
                    # Add random query parameters to avoid caching
                    random_param = f"?_t={int(time.time())}&_r={random.randint(1000, 9999)}"
                    request_url = self.current_url
                    
                    # Only add random params if URL doesn't already have query parameters
                    if '?' not in request_url:
                        request_url += random_param
                    
                    logger.info(f"Making request with User-Agent: {headers['User-Agent'][:30]}...")
                    
                    try:
                        req = urllib.request.Request(request_url, headers=headers)
                        with urllib.request.urlopen(req, timeout=15, context=ctx) as refresh_response:
                            refresh_status = refresh_response.getcode()
                            # Calculate response time
                            refresh_time = time.time() - refresh_start_time
                            http_response_times.append(refresh_time)
                            
                            logger.info(f"Refresh request {i+1} status: {refresh_status}, time: {refresh_time:.2f}s")
                            self.bot_status_messages.append(f"HTTP refresh {i+1}: {refresh_status}, time: {refresh_time:.2f}s")
                    except urllib.error.URLError as e:
                        logger.error(f"Error in refresh request: {e}")
                        self.bot_status_messages.append(f"HTTP error: {str(e)}")
                    except Exception as e:
                        logger.error(f"Unexpected error in refresh request: {e}")
                        self.bot_status_messages.append(f"Error: {str(e)}")
                
                # Calculate HTTP performance metrics
                if http_response_times:
                    avg_http_time = sum(http_response_times) / len(http_response_times)
                    max_http_time = max(http_response_times)
                    min_http_time = min(http_response_times)
                    
                    logger.info(f"HTTP performance - Avg: {avg_http_time:.2f}s, Min: {min_http_time:.2f}s, Max: {max_http_time:.2f}s")
                    self.bot_status_messages.append(f"HTTP perf - Avg: {avg_http_time:.2f}s, Min: {min_http_time:.2f}s, Max: {max_http_time:.2f}s")
                
                logger.info("HTTP site visit simulation completed successfully")
                self.bot_status_messages.append("HTTP site visit completed successfully")
                
            except urllib.error.URLError as e:
                logger.error(f"HTTP request error: {e}")
                self.bot_status_messages.append(f"HTTP error: {str(e)}")
            except Exception as e:
                logger.error(f"Unexpected error in HTTP request: {e}")
                self.bot_status_messages.append(f"Error: {str(e)}")
                
        except Exception as e:
            logger.error(f"Error in site visit simulation: {e}")
            self.bot_status_messages.append(f"Error: {str(e)}")
    
    def display_performance_metrics(self):
        """Display performance metrics of the bot."""
        print("\n" + "="*60)
        print("📊 BOT PERFORMANCE METRICS 📊")
        print("="*60)
        
        # Bot response times
        if self.bot_response_times:
            avg_time = sum(self.bot_response_times) / len(self.bot_response_times)
            max_time = max(self.bot_response_times)
            min_time = min(self.bot_response_times)
            
            print(f"Bot Response Times:")
            print(f"  • Average: {avg_time:.2f} seconds")
            print(f"  • Minimum: {min_time:.2f} seconds")
            print(f"  • Maximum: {max_time:.2f} seconds")
            
            if len(self.bot_response_times) >= 3:
                # Calculate median and percentiles if we have enough data
                median = statistics.median(self.bot_response_times)
                print(f"  • Median: {median:.2f} seconds")
        else:
            print("No bot response time data collected yet.")
        
        # Show recent bot status messages
        print("\n📋 Recent Bot Status:")
        for i, msg in enumerate(self.bot_status_messages[-10:], 1):
            print(f"  {i}. {msg}")
        
        # Show active messages
        print("\n💬 Active Bot Messages:")
        for i, msg in enumerate(self.active_messages, 1):
            print(f"  {i}. {msg}")
        
        print("="*60)
        
    async def close(self):
        """Close the client connection."""
        if self.client:
            await self.client.disconnect()
        logger.info("Client disconnected")
        self.bot_status_messages.append("Bot disconnected")

async def main():
    """Main function to run the bot."""
    try:
        print("""
+------------------------------------------------------+
|       SITE VISIT BOT WITH RESPONSE TIME METRICS      |
|                                                      |
|  This bot will:                                      |
|  1. Click 'Go to Site' button in Telegram            |
|  2. Send HTTP requests directly to site (2 minutes)  |
|  3. Track bot response times and performance         |
|  4. Click 'Visited' button automatically             |
|  5. Auto-restart after "wait 1min 30" messages       |
|                                                      |
+------------------------------------------------------+
""")
        
        # Create and start the client
        bot = SiteVisitBot(api_id, api_hash, phone)
        if not await bot.start():
            logger.error("Failed to start bot client")
            return
        
        print("Bot started successfully!")
        print("Starting site visit process...")
        
        # Start the visit process
        await bot.start_process()
        
        # Keep the script running
        print("\nBot is running. Press Ctrl+C to stop.")
        display_metrics_interval = 60  # Display metrics every 60 seconds
        last_metrics_time = time.time()
        
        while True:
            await asyncio.sleep(1)
            
            # Display metrics periodically
            current_time = time.time()
            if current_time - last_metrics_time >= display_metrics_interval:
                bot.display_performance_metrics()
                last_metrics_time = current_time
            
    except KeyboardInterrupt:
        print("\nBot stopped by user")
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Error in main function: {e}")
    finally:
        if 'bot' in locals():
            await bot.close()
        logger.info("Bot execution completed")

if __name__ == "__main__":
    # Create a .env file template if it doesn't exist
    if not os.path.exists('.env'):
        logger.info("Creating .env file template")
        with open('.env', 'w') as f:
            f.write(f"# Telegram API Credentials\n")
            f.write(f"TELEGRAM_API_ID={api_id}\n")
            f.write(f"TELEGRAM_API_HASH={api_hash}\n")
            f.write(f"TELEGRAM_PHONE={phone}\n")
        logger.info("Please update the .env file with your credentials")
    
    # Run the main function
    asyncio.run(main())

