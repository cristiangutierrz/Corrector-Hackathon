'use strict';

window.addEventListener('load', function () {
  // Fer algo quan la pagina carregui
});

if ( window.history.replaceState ) {
  // Evita prompt del navegador quan es fa refresc amb POST actiu
  window.history.replaceState( null, null, window.location.href );
}

let out = document.getElementsByClassName("editable")[0]
console.log(out.innerHTML)

function showwords(params, ctx, idx) {
  console.log(params) 
  console.log(ctx.style)
  console.log(idx)

  // ctx.innerHTML = params[0]
  // ctx['style']="text-decoration: none; color:rgb(17, 127, 0); font-weight: 600"  ;

  document.getElementsByClassName(idx)[1].showModal(); 
}

function correctword(ctx, idx, parent) {

  // document.getElementsByClassName(idx)[1].remove();
  ctx.parentNode.parentNode.parentNode.style="text-decoration: none; color:rgb(17, 127, 0); font-weight: 600"  ; 
  ctx.parentNode.parentNode.parentNode. innerHTML = ctx.innerHTML + " "
}

function closeModal(ctx) {
  console.log(ctx.parentNode)
  ctx.parentNode.close()
}