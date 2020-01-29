const myword = 'hello';
var tall = []; 
for (var i = 0; i < myword.length; i++) {
	tall.push(myword[i])
	}
console.log(tall[0].toUpperCase()+ myword.slice(1))