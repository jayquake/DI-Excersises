/*Function to*/
function runme(){
	document.getElementById("real").style.display = "none";
	document.getElementById("game").style.display="block";
	player = document.getElementById("gametime");
  	player.play();	
  	
}
document.querySelector('#audio1').addEventListener('play', setHalfVolume);

function setHalfVolume() { 
    document.getElementById("audio1")= 50% ;
}