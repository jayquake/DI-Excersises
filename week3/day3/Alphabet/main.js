const root = document.getElementById('root');
root.classList.add('box')
const abcs = 'abcdefghijklmnopqrstuvwxyz'.split('');	
 root.style.display= 'flex' ;
 root.style.justifyContent= 'space-between' ;

	for (a of abcs) {
		let box = document.createElement('div');
		box.innerText= a;
		box.style.border = 'solid 5px black';
		box.style.padding = '10px';
		box.style.fontSize = '40px';
 		box.style.background= 'goldenrod';
		box.setAttribute('draggable','true') ;
		
		box.addEventListener('dragend', function(e) {
			let x = e.clientX;
			let y = e.clientY;
			box.style.left = x + 'px';
			box.style.top = y + 'px';
			console.log(x&y);
			
			box.style.position= 'absolute';
		})
		root.appendChild(box);
}

