# Déploiement sur Koyeb

## Étapes de déploiement

1. Accédez à [Koyeb](https://app.koyeb.com)

2. Dans l'interface Koyeb:
   - Cliquez sur 'Create App'
   - Sélectionnez 'GitHub'
   - Choisissez le repository 'bot_visite_v2'

3. Configuration du déploiement:
   

4. Variables d'environnement à configurer:
   

5. Configuration avancée:
   - Build Method: Dockerfile
   - Port: 8080
   - Branch: main

## Vérification du déploiement

1. Vérifiez les logs dans Koyeb:
   - Allez dans 'Apps' > 'bot-visite-v2' > 'Logs'
   - Confirmez qu'il n'y a pas d'erreurs

2. Vérifiez le bot Telegram:
   - Le bot devrait être en ligne
   - Testez avec la commande /start

## Maintenance

1. Mises à jour:
   - Pushez sur main pour déclencher un redéploiement
   - Koyeb se met à jour automatiquement

2. Monitoring:
   - Consultez les logs régulièrement
   - Vérifiez la consommation des ressources

## Dépannage

Si le bot ne démarre pas:
1. Vérifiez les variables d'environnement
2. Consultez les logs pour les erreurs
3. Redémarrez le service si nécessaire

## Commandes utiles

Pour vérifier le statut:










<!DOCTYPE html>
<html>

<head>
  <meta charSet="utf-8" />
  <meta name="viewport" content="width=device-width" />
  <title>404: No active service</title>
  <style>
    :root {
      -moz-tab-size: 4;
      -o-tab-size: 4;
      tab-size: 4
    }

    html {
      line-height: 1.15;
      -webkit-text-size-adjust: 100%
    }

    body {
      margin: 0;
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji
    }

    hr {
      height: 0;
      color: inherit
    }

    abbr[title] {
      -webkit-text-decoration: underline dotted;
      text-decoration: underline dotted
    }

    b,
    strong {
      font-weight: bolder
    }

    code,
    kbd,
    pre,
    samp {
      font-family: ui-monospace, SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace;
      font-size: 1em
    }

    small {
      font-size: 80%
    }

    sub,
    sup {
      font-size: 75%;
      line-height: 0;
      position: relative;
      vertical-align: baseline
    }

    sub {
      bottom: -.25em
    }

    sup {
      top: -.5em
    }

    table {
      text-indent: 0;
      border-color: inherit
    }

    button,
    input,
    optgroup,
    select,
    textarea {
      font-family: inherit;
      font-size: 100%;
      line-height: 1.15;
      margin: 0
    }

    button,
    select {
      text-transform: none
    }

    [type=button],
    button {
      -webkit-appearance: button
    }

    legend {
      padding: 0
    }

    progress {
      vertical-align: baseline
    }

    summary {
      display: list-item
    }

    blockquote,
    dd,
    dl,
    figure,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    hr,
    p,
    pre {
      margin: 0
    }

    button {
      background-color: transparent;
      background-image: none
    }

    button:focus {
      outline: 1px dotted;
      outline: 5px auto -webkit-focus-ring-color
    }

    fieldset,
    ol,
    ul {
      margin: 0;
      padding: 0
    }

    ol,
    ul {
      list-style: none
    }

    html {
      font-family: Gilroy, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
      line-height: 1.5
    }

    body {
      font-family: inherit;
      line-height: inherit
    }

    *,
    :after,
    :before {
      box-sizing: border-box;
      border: 0 solid #e5e7eb
    }

    hr {
      border-top-width: 1px
    }

    img {
      border-style: solid
    }

    textarea {
      resize: vertical
    }

    input::-moz-placeholder,
    textarea::-moz-placeholder {
      opacity: 1;
      color: #9ca3af
    }

    input:-ms-input-placeholder,
    textarea:-ms-input-placeholder {
      opacity: 1;
      color: #9ca3af
    }

    input::placeholder,
    textarea::placeholder {
      opacity: 1;
      color: #9ca3af
    }

    button {
      cursor: pointer
    }

    table {
      border-collapse: collapse
    }

    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
      font-size: inherit;
      font-weight: inherit
    }

    a {
      color: inherit;
      text-decoration: inherit
    }

    button,
    input,
    optgroup,
    select,
    textarea {
      padding: 0;
      line-height: inherit;
      color: inherit
    }

    code,
    kbd,
    pre,
    samp {
      font-family: Menlo, ui-monospace, SFMono-Regular, Monaco, Consolas, Liberation Mono, Courier New, monospace
    }

    audio,
    canvas,
    embed,
    iframe,
    img,
    object,
    svg,
    video {
      display: block;
      vertical-align: middle
    }

    img,
    video {
      max-width: 100%;
      height: auto
    }

    abbr[title] {
      text-decoration: none
    }

    @font-face {
      font-family: Gilroy;
      src: local("Gilroy Regular"), local("Gilroy-Regular"), url(https://www.koyeb.com/static/fonts/Gilroy-Regular.woff2) format("woff2"), url(https://www.koyeb.com/static/fonts/Gilroy-Regular.woff) format("woff");
      font-weight: 400;
      font-style: normal;
      font-display: swap
    }

    @font-face {
      font-family: Gilroy;
      src: local("Gilroy Regular Italic"), local("Gilroy-RegularItalic"), url(https://www.koyeb.com/static/fonts/Gilroy-RegularItalic.woff2) format("woff2"), url(https://www.koyeb.com/static/fonts/Gilroy-RegularItalic.woff) format("woff");
      font-weight: 400;
      font-style: italic;
      font-display: swap
    }

    @font-face {
      font-family: Gilroy;
      src: local("Gilroy SemiBold"), local("Gilroy-SemiBold"), url(https://www.koyeb.com/static/fonts/Gilroy-Semibold.woff2) format("woff2"), url(https://www.koyeb.com/static/fonts/Gilroy-Semibold.woff) format("woff");
      font-weight: 600;
      font-style: normal;
      font-display: swap
    }

    @font-face {
      font-family: Gilroy;
      src: local("Gilroy Bold"), local("Gilroy-Bold"), url(https://www.koyeb.com/static/fonts/Gilroy-Bold.woff2) format("woff2"), url(https://www.koyeb.com/static/fonts/Gilroy-Bold.woff) format("woff");
      font-weight: 700;
      font-style: normal;
      font-display: swap
    }

    @font-face {
      font-family: Gilroy;
      src: local("Gilroy Medium"), local("Gilroy-Medium"), url(https://www.koyeb.com/static/fonts/Gilroy-Medium.woff2) format("woff2"), url(https://www.koyeb.com/static/fonts/Gilroy-Medium.woff) format("woff");
      font-weight: 500;
      font-style: normal;
      font-display: swap
    }

    .space-y-8>:not([hidden])~:not([hidden]) {
      --tw-space-y-reverse: 0;
      margin-top: calc(2rem * calc(1 - var(--tw-space-y-reverse)));
      margin-bottom: calc(2rem * var(--tw-space-y-reverse))
    }

    .space-y-10>:not([hidden])~:not([hidden]) {
      --tw-space-y-reverse: 0;
      margin-top: calc(2.5rem * calc(1 - var(--tw-space-y-reverse)));
      margin-bottom: calc(2.5rem * var(--tw-space-y-reverse))
    }

    .divide-y>:not([hidden])~:not([hidden]) {
      --tw-divide-y-reverse: 0;
      border-top-width: calc(1px * calc(1 - var(--tw-divide-y-reverse)));
      border-bottom-width: calc(1px * var(--tw-divide-y-reverse))
    }

    .divide-kgray-100>:not([hidden])~:not([hidden]) {
      --tw-divide-opacity: 1;
      border-color: rgba(18, 18, 18, var(--tw-divide-opacity))
    }

    .divide-dashed>:not([hidden])~:not([hidden]) {
      border-style: dashed
    }

    .bg-kgray-80 {
      --tw-bg-opacity: 1;
      background-color: rgba(29, 29, 29, var(--tw-bg-opacity))
    }

    .border-transparent {
      border-color: transparent
    }

    .hover\:border-kgreen-10:hover {
      --tw-border-opacity: 1;
      border-color: rgba(108, 202, 157, var(--tw-border-opacity))
    }

    .hover\:border-kgray-100:hover {
      --tw-border-opacity: 1;
      border-color: rgba(18, 18, 18, var(--tw-border-opacity))
    }

    .active\:border-kgreen-20:active {
      --tw-border-opacity: 1;
      border-color: rgba(69, 130, 101, var(--tw-border-opacity))
    }

    .active\:border-korange-10:active {
      --tw-border-opacity: 1;
      border-color: rgba(207, 154, 93, var(--tw-border-opacity))
    }

    .rounded-lg {
      border-radius: .5rem
    }

    .border-b {
      border-bottom-width: 1px
    }

    .box-border {
      box-sizing: border-box
    }

    .inline-block {
      display: inline-block
    }

    .flex {
      display: flex
    }

    .table {
      display: table
    }

    .grid {
      display: grid
    }

    .flex-col {
      flex-direction: column
    }

    .place-items-center {
      place-items: center
    }

    .place-content-center {
      place-content: center
    }

    .self-center {
      align-self: center
    }

    .justify-between {
      justify-content: space-between
    }

    .font-medium {
      font-weight: 500
    }

    .font-semibold {
      font-weight: 600
    }

    .font-bold {
      font-weight: 700
    }

    .text-m-3xl {
      font-size: 3.375rem;
      line-height: 3.687rem
    }

    .text-m-2xl {
      font-size: 2.125rem;
      line-height: 2.125rem
    }

    .text-m-xl {
      font-size: 1.5rem;
      line-height: 1.812rem
    }

    .text-m-lg {
      font-size: 1.25rem;
      line-height: 1.5rem
    }

    .text-m-lead {
      font-size: 1.125rem;
      line-height: 1.875rem
    }

    .text-m-caption {
      font-size: .812rem;
      line-height: 1.437rem
    }

    .text-m-small {
      font-size: .875rem;
      line-height: 1.25rem
    }

    .text-m-tiny {
      font-size: .687rem;
      line-height: .937rem
    }

    .mx-auto {
      margin-left: auto;
      margin-right: auto
    }

    .mr-2 {
      margin-right: .5rem
    }

    .mb-2 {
      margin-bottom: .5rem
    }

    .ml-2 {
      margin-left: .5rem
    }

    .mb-4 {
      margin-bottom: 1rem
    }

    .mb-10 {
      margin-bottom: 2.5rem
    }

    .mb-18 {
      margin-bottom: 4.5rem
    }

    .mb-28 {
      margin-bottom: 7rem
    }

    .mt-1 {
      margin-bottom: .25rem
    }

    .max-w-sm {
      max-width: 24rem
    }

    .min-h-screen {
      min-height: 100vh
    }

    .opacity-0 {
      opacity: 0
    }

    .group-link:hover .group-link-hover\:opacity-100 {
      opacity: 1
    }

    .p-10 {
      padding: 2.5rem
    }

    .p-16 {
      padding: 4rem
    }

    .pt-10 {
      padding-top: 2.5rem
    }

    .pb-10 {
      padding-bottom: 2.5rem
    }

    .relative {
      position: relative
    }

    * {
      --tw-shadow: 0 0 transparent
    }

    .shadow-2xl {
      --tw-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
      box-shadow: var(--tw-ring-offset-shadow, 0 0 transparent), var(--tw-ring-shadow, 0 0 transparent), var(--tw-shadow)
    }

    * {
      --tw-ring-inset: var(--tw-empty,
          /*!*/
          /*!*/
        );
      --tw-ring-offset-width: 0px;
      --tw-ring-offset-color: #fff;
      --tw-ring-color: rgba(59, 130, 246, 0.5);
      --tw-ring-offset-shadow: 0 0 transparent;
      --tw-ring-shadow: 0 0 transparent
    }

    .fill-current {
      fill: currentColor
    }

    .stroke-current {
      stroke: currentColor
    }

    .text-center {
      text-align: center
    }

    .text-current {
      color: currentColor
    }

    .text-white {
      --tw-text-opacity: 1;
      color: rgba(255, 255, 255, var(--tw-text-opacity))
    }

    .text-kerror-default {
      --tw-text-opacity: 1;
      color: rgba(255, 114, 114, var(--tw-text-opacity))
    }

    .text-kgreen-30 {
      --tw-text-opacity: 1;
      color: rgba(94, 177, 137, var(--tw-text-opacity))
    }

    .text-kgreen-default {
      --tw-text-opacity: 1;
      color: rgba(135, 252, 196, var(--tw-text-opacity))
    }

    .text-kgray-60 {
      --tw-text-opacity: 1;
      color: rgba(87, 89, 88, var(--tw-text-opacity))
    }

    .text-kgray-100 {
      --tw-text-opacity: 1;
      color: rgba(18, 18, 18, var(--tw-text-opacity))
    }

    .text-korange-default {
      --tw-text-opacity: 1;
      color: rgba(255, 190, 114, var(--tw-text-opacity))
    }

    .hover\:text-kgreen-default:hover {
      --tw-text-opacity: 1;
      color: rgba(135, 252, 196, var(--tw-text-opacity))
    }

    .hover\:text-korange-10:hover {
      --tw-text-opacity: 1;
      color: rgba(207, 154, 93, var(--tw-text-opacity))
    }
    .active\:text-kgreen-20:active {
      --tw-text-opacity: 1;
      color: rgba(69, 130, 101, var(--tw-text-opacity))
    }
    .active\:text-korange-10:active {
      --tw-text-opacity: 1;
      color: rgba(207, 154, 93, var(--tw-text-opacity))
    }
    .uppercase {
      text-transform: uppercase
    }
    .tracking-caption {
      letter-spacing: .1em
    }
    .tracking-tiny {
      letter-spacing: .08em
    }
    .align-middle {
      vertical-align: middle
    }
    .w-96 {
      width: 24rem
    }
    .z-20 {
      z-index: 20
    }
    .transform {
      --tw-translate-x: 0;
      --tw-translate-y: 0;
      --tw-rotate: 0;
      --tw-skew-x: 0;
      --tw-skew-y: 0;
      --tw-scale-x: 1;
      --tw-scale-y: 1;
      transform: translateX(var(--tw-translate-x)) translateY(var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
    }
    .rotate-90 {
      --tw-rotate: 90deg
    }
    @-webkit-keyframes spin {
      to {
        transform: rotate(1turn)
      }
    }
    @keyframes spin {
      to {
        transform: rotate(1turn)
      }
    }
    @-webkit-keyframes ping {
      75%,
      to {
        transform: scale(2);
        opacity: 0
      }
    }
    @keyframes ping {
      75%,
      to {
        transform: scale(2);
        opacity: 0
      }
    }
    @-webkit-keyframes pulse {
      50% {
        opacity: .5
      }
    }
    @keyframes pulse {
      50% {
        opacity: .5
      }
    }
    @-webkit-keyframes bounce {
      0%,
      to {
        transform: translateY(-25%);
        -webkit-animation-timing-function: cubic-bezier(.8, 0, 1, 1);
        animation-timing-function: cubic-bezier(.8, 0, 1, 1)
      }
      50% {
        transform: none;
        -webkit-animation-timing-function: cubic-bezier(0, 0, .2, 1);
        animation-timing-function: cubic-bezier(0, 0, .2, 1)
      }
    }
    @keyframes bounce {
      0%,
      to {
        transform: translateY(-25%);
        -webkit-animation-timing-function: cubic-bezier(.8, 0, 1, 1);
        animation-timing-function: cubic-bezier(.8, 0, 1, 1)
      }
      50% {
        transform: none;
        -webkit-animation-timing-function: cubic-bezier(0, 0, .2, 1);
        animation-timing-function: cubic-bezier(0, 0, .2, 1)
      }
    }
    @-webkit-keyframes flash-code {
      0% {
        background-color: rgba(134, 239, 172, .25)
      }
      to {
        background-color: transparent
      }
    }
    @keyframes flash-code {
      0% {
        background-color: rgba(134, 239, 172, .25)
      }
      to {
        background-color: transparent
      }
    }
    .bg-light {
      background-image: url(https://www.koyeb.com/static/images/backgrounds/grid-light.svg);
      background-repeat: no-repeat;
      background-position: 0;
      background-size: cover
    }
    .before\:title-caption:before {
      content: "";
      display: inline-block;
      vertical-align: super;
      border: 1px solid #87fcc4;
      width: 32px;
      margin-right: 1em
    }
    .scrollbar-none {
      scrollbar-width: none
    }
    .scrollbar-none::-webkit-scrollbar {
      display: none !important
    }
    .scrollbar-w-2::-webkit-scrollbar {
      height: .5rem !important;
      width: .5rem !important
    }
    .scrollbar-track-gray-lighter::-webkit-scrollbar-track {
      --tw-bg-opacity: 1 !important;
      background-color: rgba(209, 213, 219, var(--tw-bg-opacity)) !important
    }
    .scrollbar-thumb-gray::-webkit-scrollbar-thumb {
      --tw-bg-opacity: 1 !important;
      background-color: rgba(156, 163, 175, var(--tw-bg-opacity)) !important
    }
    .scrollbar-thumb-rounded::-webkit-scrollbar-thumb {
      border-radius: .25rem !important
    }
    @supports ((position:-webkit-sticky) or (position:sticky)) {
      @media (min-width:1024px) {
        .sticky\?lg\:h-screen {
          height: 100vh !important
        }
        .sticky\?lg\:h-\(screen-18\) {
          height: calc(100vh - 4.5rem)
        }
      }
    }
    @media (prefers-reduced-motion:reduce) {
      .motion-reduce\:transform-none:hover {
        transform: none !important
      }
    }
    @media (prefers-reduced-motion:no-preference) {
      .motion-safe\:hover\:-translate-y-1:hover {
        --transform-translate-y: -0.25rem !important
      }
      .motion-safe\:hover\:scale-110:hover {
        --transform-scale-x: 1.1 !important;
        --transform-scale-y: 1.1 !important
      }
    }
    .focus\:bg-gray-600:focus {
      --tw-bg-opacity: 1 !important;
      background-color: rgba(75, 85, 99, var(--tw-bg-opacity)) !important
    }
    .focus\:text-white:focus,
    .group:hover .group-hover\:text-white {
      --tw-text-opacity: 1 !important;
      color: rgba(255, 255, 255, var(--tw-text-opacity)) !important
    }
    .focus-within\:border-teal-500:focus-within {
      --tw-border-opacity: 1 !important;
      border-color: rgba(20, 184, 166, var(--tw-border-opacity)) !important
    }
    .focus-visible\:underline:focus-visible {
      text-decoration: underline !important
    }
    .focus-visible\:underline.focus-visible {
      text-decoration: underline !important
    }
    .active\:bg-blue-700:active {
      --tw-bg-opacity: 1 !important;
      background-color: rgba(29, 78, 216, var(--tw-bg-opacity)) !important
    }
    .checked\:bg-blue-600:checked {
      --tw-bg-opacity: 1 !important;
      background-color: rgba(37, 99, 235, var(--tw-bg-opacity)) !important
    }
    .checked\:border-transparent:checked {
      border-color: transparent !important
    }
    .appearance-none::-ms-expand {
      display: none !important
    }
    .bg-checkered {
      background-image: url("data:image/svg+xml,%0A%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill='%23F0F0F0' d='M0 0h8v8H0zm8 8h8v8H8z'/%3E%3C/svg%3E");
      background-size: 16px 16px
    }
    .after\:hash:after {
      content: "#"
    }
    .code-highlight {
      border-radius: .1875rem;
      padding: .0625rem .1875rem;
      margin: 0 -.1875rem
    }
    body.cursor-grabbing * {
      cursor: -webkit-grabbing !important;
      cursor: grabbing !important
    }
    .mono-active>div:not(.not-mono)>span {
      color: hsla(0, 0%, 100%, .25)
    }
    .mono>div>span {
      transition-duration: .5s;
      transition-property: background-color, border-color, color, fill, stroke
    }
    .form-tick:checked {
      background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 16 16' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M5.707 7.293a1 1 0 0 0-1.414 1.414l2 2a1 1 0 0 0 1.414 0l4-4a1 1 0 0 0-1.414-1.414L7 8.586 5.707 7.293z'/%3e%3c/svg%3e");
      border-color: transparent;
      background-color: currentColor;
      background-size: 100% 100%;
      background-position: 50%;
      background-repeat: no-repeat
    }
    @media (min-width:640px) {
      .sm\:space-y-0>:not([hidden])~:not([hidden]) {
        --tw-space-y-reverse: 0;
        margin-top: calc(0px * calc(1 - var(--tw-space-y-reverse)));
        margin-bottom: calc(0px * var(--tw-space-y-reverse))
      }
      .sm\:space-x-4>:not([hidden])~:not([hidden]) {
        --tw-space-x-reverse: 0;
        margin-right: calc(1rem * var(--tw-space-x-reverse));
        margin-left: calc(1rem * calc(1 - var(--tw-space-x-reverse)))
      }
      .sm\:flex-row {
        flex-direction: row
      }
      .sm\:items-stretch {
        align-items: stretch
      }
      .sm\:rotate-0 {
        --tw-rotate: 0deg
      }
    }
    @media (min-width:768px) {
      .md\:text-t-3xl {
        font-size: 4rem;
        line-height: 4.375rem
      }
      .md\:text-t-2xl {
        font-size: 3.375rem;
        line-height: 3.375rem
      }
      .md\:text-t-xl {
        font-size: 1.875rem;
        line-height: 2.25rem
      }
      .md\:text-t-lg {
        font-size: 1.375rem;
        line-height: 1.625rem
      }
      .md\:text-t-lead {
        font-size: 1.125rem;
        line-height: 1.875rem
      }
      .md\:text-t-caption {
        font-size: .812rem;
        line-height: 1.437rem
      }
      .md\:text-t-small {
        font-size: .875rem;
        line-height: 1.25rem
      }
      .md\:text-t-tiny {
        font-size: .687rem;
        line-height: .937rem
      }
    }
    @media (min-width:1024px) {
      .lg\:space-y-0>:not([hidden])~:not([hidden]) {
        --tw-space-y-reverse: 0;
        margin-top: calc(0px * calc(1 - var(--tw-space-y-reverse)));
        margin-bottom: calc(0px * var(--tw-space-y-reverse))
      }
      .lg\:space-x-10>:not([hidden])~:not([hidden]) {
        --tw-space-x-reverse: 0;
        margin-right: calc(2.5rem * var(--tw-space-x-reverse));
        margin-left: calc(2.5rem * calc(1 - var(--tw-space-x-reverse)))
      }
      .lg\:flex-row {
        flex-direction: row
      }
      .lg\:text-d-3xl {
        font-size: 4.625rem;
        line-height: 5.062rem
      }
      .lg\:text-d-2xl {
        font-size: 4rem;
        line-height: 4rem
      }
      .lg\:text-d-xl {
        font-size: 2.125rem;
        line-height: 2.562rem
      }
      .lg\:text-d-lg {
        font-size: 1.5rem;
        line-height: 1.812rem
      }
      .lg\:text-d-lead {
        font-size: 1.125rem;
        line-height: 1.875rem
      }
      .lg\:text-d-caption {
        font-size: .812rem;
        line-height: 1.437rem
      }
      .lg\:text-d-small {
        font-size: .875rem;
        line-height: 1.25rem
      }
      .lg\:text-d-tiny {
        font-size: .687rem;
        line-height: .937rem
      }
      .lg\:ml-20 {
        margin-left: 5rem
      }
    }
    @media (min-width:1280px) {
      .xl\:max-w-lg {
        max-width: 32rem
      }
    }
    .container {
      width: 100%
    }
    @media (min-width:640px) {
      .container {
        max-width: 640px
      }
    }
    @media (min-width:768px) {
      .container {
        max-width: 768px
      }
    }
    @media (min-width:1024px) {
      .container {
        max-width: 1024px
      }
    }
    @media (min-width:1280px) {
      .container {
        max-width: 1280px
      }
    }
    @media (min-width:1536px) {
      .container {
        max-width: 1536px
      }
    }
  </style>
</head>

<body>
  <div>
    <div class="bg-light min-h-screen">
      <div class="container p-16 mx-auto relative z-20">
        <div class="mb-18">
          <p class="text-m-2xl md:text-t-2xl lg:text-d-2xl font-semibold text-bold">404</p>
          <p class="text-m-lead md:text-t-lead lg:text-d-lead text-kgray-60">No active service</p>
        </div>
        <div
          class="flex place-items-center space-y-10 sm:space-y-0 sm:space-x-4 lg:space-x-10  mb-28 flex-col sm:flex-row sm:items-stretch text-kgreen-default">
          <div
            class="bg-kgray-80  shadow-2xl p-10 flex flex-col place-items-center place-content-center rounded-lg w-96  text-center">
            <svg class="mb-4 fill-current" width="55" height="55" viewBox="0 0 55 55" fill="none"
              xmlns="http://www.w3.org/2000/svg">
              <rect width="55" height="55" rx="9.96721"></rect>
              <path
                d="M8.16406 22.0514C8.16406 21.5009 8.61031 21.0547 9.16078 21.0547H45.8392C46.3897 21.0547 46.8359 21.5009 46.8359 22.0514V41.972C46.8359 42.5225 46.3897 42.9688 45.8392 42.9688H9.16078C8.61031 42.9688 8.16406 42.5225 8.16406 41.972V22.0514Z"
                fill="#121212"></path>
              <path
                d="M9.16078 12.0312C8.61031 12.0312 8.16406 12.4775 8.16406 13.028V17.4798C8.16406 18.0303 8.61031 18.4766 9.16078 18.4766H45.8392C46.3897 18.4766 46.8359 18.0303 46.8359 17.4798V13.028C46.8359 12.4775 46.3897 12.0312 45.8392 12.0312H9.16078ZM12.0312 16.543C11.7763 16.543 11.5271 16.4674 11.3151 16.3257C11.1031 16.1841 10.9379 15.9828 10.8403 15.7472C10.7427 15.5117 10.7172 15.2525 10.767 15.0024C10.8167 14.7524 10.9395 14.5227 11.1197 14.3424C11.3 14.1621 11.5297 14.0394 11.7798 13.9896C12.0298 13.9399 12.289 13.9654 12.5246 14.063C12.7601 14.1605 12.9614 14.3258 13.1031 14.5377C13.2447 14.7497 13.3203 14.999 13.3203 15.2539C13.3203 15.5958 13.1845 15.9237 12.9428 16.1654C12.701 16.4072 12.3731 16.543 12.0312 16.543ZM15.8984 16.543C15.6435 16.543 15.3943 16.4674 15.1823 16.3257C14.9703 16.1841 14.8051 15.9828 14.7075 15.7472C14.6099 15.5117 14.5844 15.2525 14.6341 15.0024C14.6839 14.7524 14.8067 14.5227 14.9869 14.3424C15.1672 14.1621 15.3969 14.0394 15.647 13.9896C15.897 13.9399 16.1562 13.9654 16.3917 14.063C16.6273 14.1605 16.8286 14.3258 16.9703 14.5377C17.1119 14.7497 17.1875 14.999 17.1875 15.2539C17.1875 15.5958 17.0517 15.9237 16.8099 16.1654C16.5682 16.4072 16.2403 16.543 15.8984 16.543ZM19.7656 16.543C19.5107 16.543 19.2614 16.4674 19.0495 16.3257C18.8375 16.1841 18.6723 15.9828 18.5747 15.7472C18.4771 15.5117 18.4516 15.2525 18.5013 15.0024C18.5511 14.7524 18.6738 14.5227 18.8541 14.3424C19.0344 14.1621 19.2641 14.0394 19.5141 13.9896C19.7642 13.9399 20.0234 13.9654 20.2589 14.063C20.4945 14.1605 20.6958 14.3258 20.8374 14.5377C20.9791 14.7497 21.0547 14.999 21.0547 15.2539C21.0547 15.5958 20.9189 15.9237 20.6771 16.1654C20.4354 16.4072 20.1075 16.543 19.7656 16.543Z"
                fill="#121212"></path>
            </svg>
            <p class="uppercase font-bold text-white  mb-2">Your Browser</p>
            <p
              class="text-m-caption md:text-t-caption lg:text-d-caption uppercase font-semibold tracking-caption font-bold">
              WORKING</p>
          </div><svg class="self-center transform rotate-90 sm:rotate-0" width="40" height="16" viewBox="0 0 40 16"
            fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M31.7241 0.827585L29.0345 3.86207L31.7241 6.34483L8.27586 6.34483L11.0345 3.58621L8.27586 0.827586L-3.31604e-07 8.41379L8.27586 16L11.0345 13.2414L8.27586 10.4828L31.7241 10.4828L28.9655 13.2414L31.7241 16L40 8.41379L31.7241 0.827585Z"
              fill="#121212" fill-opacity="0.2"></path>
          </svg>
          <div
            class="bg-kgray-80  shadow-2xl p-10 flex flex-col place-items-center place-content-center rounded-lg w-96 text-kgreen-default text-center">
            <svg class="mb-4 fill-current" width="55" height="55" viewBox="0 0 55 55" fill="none"
              xmlns="http://www.w3.org/2000/svg">
              <rect width="55" height="55" rx="9.96721"></rect>
              <path d="M27.4591 17.504L46.6928 28.5785V19.3369L27.4468 8.25L8.25 19.3492V28.6031L27.4591 17.504Z"
                fill="#121212"></path>
              <path
                d="M43.6163 39.7159L46.6928 37.9066V32.2335L27.4468 21.1343L8.25 32.2335V37.9312L11.3264 39.7159L27.4468 30.3882L43.6163 39.7159Z"
                fill="#121212"></path>
              <path
                d="M27.4582 43.5059L32.343 46.324L40.3668 41.7089L27.4459 34.252L14.5742 41.7089L22.597 46.324L27.4582 43.5059Z"
                fill="#121212"></path>
            </svg>
            <p class="uppercase font-bold text-white  mb-2">Koyeb Edge Network</p>
            <p
              class="text-m-caption md:text-t-caption lg:text-d-caption uppercase font-semibold tracking-caption font-bold">
              WORKING</p>
          </div><svg class="self-center transform rotate-90 sm:rotate-0	" width="40" height="16" viewBox="0 0 40 16"
            fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M31.7241 0.827585L29.0345 3.86207L31.7241 6.34483L8.27586 6.34483L11.0345 3.58621L8.27586 0.827586L-3.31604e-07 8.41379L8.27586 16L11.0345 13.2414L8.27586 10.4828L31.7241 10.4828L28.9655 13.2414L31.7241 16L40 8.41379L31.7241 0.827585Z"
              fill="#121212" fill-opacity="0.2"></path>
          </svg>
          <div
            class="bg-kgray-80 shadow-2xl p-10 flex flex-col place-items-center place-content-center rounded-lg w-96 text-korange-default text-center">
            <svg class="mb-4 fill-current " width="55" height="55" viewBox="0 0 55 55" fill="none"
              xmlns="http://www.w3.org/2000/svg">
              <rect width="55" height="55" rx="9.96721"></rect>
              <path
                d="M44.71 28.1445C45.3815 28.1445 45.8609 27.4941 45.662 26.8527L42.0664 15.2539C41.9157 14.5622 41.5458 13.9377 41.0116 13.4731C40.4774 13.0086 39.8075 12.729 39.1016 12.6758H15.8984C14.6094 12.6758 13.5137 13.5137 12.9336 15.2539L9.33797 26.8527C9.13915 27.4941 9.61852 28.1445 10.29 28.1445H44.71Z"
                fill="#121212"></path>
              <path
                d="M8.16406 41.0352C8.16406 41.377 8.29987 41.7049 8.54162 41.9467C8.78337 42.1884 9.11124 42.3242 9.45312 42.3242H45.5469C45.8888 42.3242 46.2166 42.1884 46.4584 41.9467C46.7001 41.7049 46.8359 41.377 46.8359 41.0352V31.7194C46.8359 31.1689 46.3897 30.7227 45.8392 30.7227H9.16078C8.61031 30.7227 8.16406 31.1689 8.16406 31.7194V41.0352ZM39.4883 32.3984C39.7364 32.1765 40.0577 32.0538 40.3906 32.0538C40.7236 32.0538 41.0448 32.1765 41.293 32.3984C41.5358 32.6364 41.6748 32.9608 41.6797 33.3008C41.6797 33.6427 41.5439 33.9705 41.3021 34.2123C41.0604 34.454 40.7325 34.5898 40.3906 34.5898C40.0487 34.5898 39.7209 34.454 39.4791 34.2123C39.2374 33.9705 39.1016 33.6427 39.1016 33.3008C39.1064 32.9608 39.2454 32.6364 39.4883 32.3984ZM14.6094 35.8789H40.3906C40.7325 35.8789 41.0604 36.0147 41.3021 36.2565C41.5439 36.4982 41.6797 36.8261 41.6797 37.168C41.6797 37.5099 41.5439 37.8377 41.3021 38.0795C41.0604 38.3212 40.7325 38.457 40.3906 38.457H14.6094C14.2675 38.457 13.9396 38.3212 13.6979 38.0795C13.4561 37.8377 13.3203 37.5099 13.3203 37.168C13.3203 36.8261 13.4561 36.4982 13.6979 36.2565C13.9396 36.0147 14.2675 35.8789 14.6094 35.8789Z"
                fill="#121212"></path>
            </svg>
            <p class="uppercase font-bold text-white  mb-2">Application</p>
            <p
              class="text-m-caption md:text-t-caption lg:text-d-caption uppercase font-semibold tracking-caption font-bold">
              ERROR</p>
          </div>
        </div>
        <div class="divide-y divide-kgray-100 divide-dashed">
          <div class="flex flex-col space-y-10 lg:space-y-0 lg:flex-row justify-between pb-10">
            <div class="max-w-sm xl:max-w-lg">
              <p class="text-m-xl md:text-t-xl lg:text-d-xl font-semibold mb-10">No service is active (yet)</p>
              <p class="text-kgray-60">Your request landed on a Koyeb Edge location. The Koyeb serverless platform didn't find any active service to route the request to. 🙃 </p>
            </div>
            <div class="max-w-sm xl:max-w-lg">
              <p class="text-m-xl md:text-t-xl lg:text-d-xl font-semibold mb-10">What can I do?</p>
              <p class="text-m-lead md:text-t-lead lg:text-d-lead text-kgray-100 mb-2">If you&#x27;re a visitor:</p>
              <p class="text-kgray-60 mb-4">If you have followed a link leading you here, you can try to contact the owner of the application and let them know there is an error.</p>
              <p class="text-m-lead md:text-t-lead lg:text-d-lead text-kgray-100 mb-2">If you&#x27;re the owner of the
                application:</p>
              <div class="text-kgray-60">If you just deployed a service on this path, it will be accessible once the service is detected as healthy. This error is temporary and your application should be up and running in less than a minute.</p><p class="mt-1">This page might also be displayed if your app is not composed of any active public service on this path. Check the <a class="text-kgreen-30" href="https://www.koyeb.com/docs">documentation</a> for more details.</div>
            </div>
          </div>
          <div class="pt-10">
            <p>High-performance serverless hosting by
              <!-- --> <a href="https://www.koyeb.com" class="text-kgreen-30">Koyeb</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div id="debug_info" style="display: none;"> </div>
</body>

</html>

## Notes importantes

- Le bot tourne 24/7
- Les redémarrages sont automatiques
- Les sessions Telegram sont persistantes
- Les logs sont conservés pendant 7 jours
