/*you must create a secret word of at least 8 [ a string] letters and two similar letters. ecret Word : "Unregistered"
We will only be able to see in the console from the beginning of the game the first and last letter of the game,
 the other letters of the word will be replaced by “stars”,like this J********t no like this 
 J, * , * , * ,  * , * , * , * , * , * , TWe will only have 10 attempts [loop] to find this word by guessing letter by 
 letter, use prompt() for user input that will ask for a "single letter" and not a number.
When the player finds a similar letter (like ‘a’ in the word ‘javascript’ Ja*a*******t ) it will have to replace
 the corresponding stars in a single move.
A message will announce the player his victory and stop the game.

Good Luck*/
/*the first and last letter is in the array is being displayed using 
.push  */
console.log('firstLast()')
const myword = 'unregistered';
var firstLast = []; 
var whattoshow = [];
for (var i = 0; i < myword.length; i++) {
	firstLast.push(myword[i])
	if (i == 0 ) {
		whattoshow.push(myword[i])
	}
	else if (i== myword.length-1){
		whattoshow.push( myword[i])
	}
	else{
		whattoshow.push('*')
	}
}
console.log(whattoshow)

function guessing_Game (char){
	
	for (var i = 0; i < firstLast.length; i++) {
		if (firstLast[i] == char){
			whattoshow[i]=firstLast[i];
		}
	}
	console.log(whattoshow.join(""))		
}

function askuser( ){
	for (var i = 0; i < 10; i++) {
		let userguess = prompt("Take a guess");
		guessing_Game(userguess)
		if (1 <= 10 ) {}
	}
}
askuser()
	/*for (var i = 0; i < Things.length; i++) {
		Things[i]
	}