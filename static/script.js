'use strict';

window.addEventListener('load', function () {
  // Fer algo quan la pagina carregui
});

if ( window.history.replaceState ) {
  // Evita prompt del navegador quan es fa refresc amb POST actiu
  window.history.replaceState( null, null, window.location.href );
}