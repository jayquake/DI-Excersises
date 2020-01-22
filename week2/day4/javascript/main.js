

function playTheGame()
{
	
	if (confirm('Are you sure you to play this Game?' )) {
	} else(alert("No Problem , Goodbye."))


	
	for (var i = 0; i < 4 ; i++) {

		var myNumber = Number(prompt(" Type a number between 1 and 10"));
		var computerNumber = Math.floor(Math.random()* 11)
		if (isNaN (myNumber)) {
			alert( "Sorry Not a number, Goodbye");
			return;
		}
		else if (myNumber <= 0 || myNumber > 10 ) {
			alert("Sorry that's not a good number,Goodbye");
			return;
		}
		
		else if   (myNumber == null) {
			alert("No problem, Goodbye");
			return;
		}

		test(myNumber, computerNumber)




		function test(myNumber, computerNumber){
			if (myNumber == computerNumber) {
				alert("You Won!!!");
			}
			else if (myNumber > computerNumber) {
				alert("Your number is bigger Try again");
			}
			else if (myNumber < computerNumber) {
				alert("Your number is smaller Try again");
			}
		}
	}

	playTheGame()

}


