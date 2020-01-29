
/*	let list = document.createElement('ul')
	let li2 = document.createElement('li')
	let li3 = document.createElement('li')*/
let root = document.getElementById('root');
let list =document.getElementById('shopping_list');
let addItem = () => {
	var item = prompt("What do you need?");
	let li1 = document.createElement('li');
	let textNode = document.createTextNode(item);
	li1.appendChild(textNode);
	list.appendChild(li1);
}


let clear_list = () => {
	document.getElementById('shopping_list').innerHTML = '';
}
document.body.style.backgroundImage = "url('bg.jpg')","center" ;
document.body.style.backgroundSize = "100";
document.body.style.fontSize = "3em	" ;