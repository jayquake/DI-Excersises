/*Function to*/
/*function runme(){
	document.getElementById("landingPage").style.display = "none";
	document.getElementById("real").style.display="block";
	player = document.getElementById("player");
  	player.play();	
  	
}*/

function startgame(){
	player.pause()
	document.getElementById("real").style.display = "none";
	document.getElementById("game").style.display="block";
	gametime = document.getElementById("gametime");
  	gametime.play();	
}

let main = document.getElementById('landingPage');




//-------------------------------------------------------------------------

var width = window.innerWidth;
var height = window.innerHeight;


function position() {
	if(document.getElementById("person"))
		document.getElementById("person").remove();



	let p_x = Math.floor(Math.random()*width)-110; 
	let p_y = Math.floor(Math.random()*height)-110; 

	if(p_x<=0)
		p_x = 20;
	if(p_y<=0)
		p_y = 20;

	let person = document.createElement("img");
	person.style.top = p_y+"px";
	person.style.left = p_x+"px";
	person.src = "Untitled.xcf";  
	person.style.width = "100px";
	person.style.height = "100px";
	person.style.position = "absolute";
	person.id = "person";
	//person.onclick = ; // we need to put here the function 


	document.body.appendChild(person);

}


function mouse_down()
{
	document.body.style.cursor = "url(ddd.png), auto"; 
}

function mouse_up()
{
	document.body.style.cursor = "url(lalala.png), auto"; 
}


function Play()
{
	setInterval(function(){ position(); }, 1000);
}


</script>