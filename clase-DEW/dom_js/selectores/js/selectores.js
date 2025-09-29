/***********************************************************
 * METODOS DE ACCESO AL DOM
 *
 *
 * getElementById
 * getElementByClassName
 * getElementByTagName
 *
 * querySelector
 * querySelectorAll
 *
 ***********************************************************/

let noticias = document.getElementById('noticias');

console.log(`Hay ${noticias.childElementCount} noticias`);

let ultimaNoticia = document.createElement('p');
ultimaNoticia.textContent = 'Noticia 2';

noticias.appendChild(ultimaNoticia);

console.log(`Ahora hay ${noticias.childElementCount} noticias`);
