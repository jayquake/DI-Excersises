const rootDiv = document.getElementById('root')
rootDiv.classList.add('box')
root.setAttribute('draggable' ,'true')
/*
root.addEventListener('drag', function(e){
	root.style.background = 'purple'
})*/
/*
root.addEventListener('dragstart', function(e){
	root.style.background = 'pink'
})*/
root.addEventListener('dragend', function(e){
	root.style.background = 'gold'
	let x = e.clientX
	let y = e.clientY
	root.style.top = y +'px'
	root.style.left = x +'px'
	console.log(x&&y)
})


root.addEventListener('click', function (e) {
	root.style.background = 'red'
})

root.addEventListener('mouseover', function (e) {
	root.style.background = 'blue'
})

root.addEventListener('mouseenter', function (e) {
	root.style.background = 'green'
})
root.addEventListener('mouseleave', function (e) {
	root.style.background = 'goldenrod'
})
root.addEventListener('mouseup', function (e) {
	root.style.background = 'yellow'
})

p.addEventListener('mouseenter', function(e){
	createPTag(
		)
})






/*Button*/
/*
let but = document.createElement('button')
but.innerText = 'Click Me'
but.setAttribute('class' ,'a');

let int = document.createElement('input');
int.setAttribute('type' ,'text');
int.setAttribute('placeholder', 'enter your email');
int.setAttribute('id' , 'emailInput')

but.addEventListener('click', function (e) {
	let myinput = document.getElementById('emailInput');
	console.log(myinput.value)
})
int.addEventListener('keypress' , function (e) {
	if (e.keyCode == 13) {
	console.log(e.target.value)
	}
})
int.addEventListener('keypress', myfunc);

function myfunc (event){
console.log(event);
}
rootDiv.appendChild(but);
rootDiv.appendChild(int);
*/

