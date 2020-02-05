let gameCanvas = document.getElementById('gameCanvas');
gameCanvas.style.width = '500px';
gameCanvas.style.height = '700px';
gameCanvas.style.border = '2px solid lightgrey';
gameCanvas.style.background = 'lightgrey';


let draw= gameCanvas.getContext("2d");
draw.fillStyle = 'goldenrod';

let mygamepeice = document.createElement('div');
mygamepeice.style.width='200px';
mygamepeice.style.height='200px';
mygamepeice.style.background='red';

let Game = function (options) {
	this.face = options.face;
	
	// body...
}
