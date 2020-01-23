/*Number Gane */

function playTheGame(){
	if  (!confirm('Are you sure you to play this Game?' )) {
		alert("No Problem , Goodbye.")
		return;
	}




		for (var i = 0; i < 3 ; i++) {
			if (i  > 3 || i == 3) {
				alert('You Lose!! ');
				return;
			}


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
				alert("Incorrect");
				return;
			}

			test(myNumber, computerNumber)




			function test(myNumber, computerNumber){
				if (myNumber == computerNumber) {
					alert("You Won!!!");
					return;
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


