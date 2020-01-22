var arr = [5,0,9,1,7,4,2,6,3,8];
var temp = 0;


for (var i = 0 ; i < arr.length; i++) {
	for (var e = i ; e < arr.length; e++) {
		if  (arr[i] > arr[e]) {
			temp = arr[i];
			 arr[i] = arr[e]; 
			  arr[e] = temp ;
		}
		}
		console.log(arr.toString() );
	}
