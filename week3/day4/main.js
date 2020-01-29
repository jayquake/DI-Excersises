let root = document.getElementById('root');
root.style.backgroundColor= 'goldenrod';
let button1= document.createElement('button' ,'click me!');
button1.innerText='click me';
button1.style.width='100px';
button1.style.height='100px';
root.appendChild(button1)

document.body.classList.add('boxes');

let outerbox = document.createElement('div')
outerbox.style.border= 'solid black 1px'
outerbox.style.width='500px';
outerbox.style.height='500px';
outerbox.style.position='relative'
outerbox.classList.add(container)
root.appendChild(outerbox)



let innerbox = document.createElement('div')
innerbox.style.border= 'solid black 1px'
innerbox.style.width='100px';
innerbox.style.height='100px';
innerbox.style.height
innerbox.classList.add('animate')
innerbox.setAttribute('id','animate')
console.log(root)