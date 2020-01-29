/*console.log(robots[0]);
let bret = robots[0];

let plant_robot = document.querySelector('#root')
const robodisplay = () => {
		robots.forEach(item => {

	let div1 = document.createElement('div');
	let image = document.createElement('img');
	let name = document.createElement('h2');
	let username = document.createElement('h3');
	let email = document.createElement('p');

	image.setAttribute('src' , "https://robohash.org/" +item.id + "?size=200x200")


	div1.appendChild('image');
	div1.appendChild('name');
	div1.appendChild('username');
	div1.appendChild('email');
	plant_robot.appendChild('div1');
		} )


	}*/

console.log(robots)
let root = document.getElementById('root')
root.classList.add("box-grid")
function robodisplay() {
	for (robot of robots) {
		let box = document.createElement('div')
		let image = document.createElement('img')
		let name = document.createElement('name')
		let username = document.createElement('username')
		let email = document.createElement('p')

		image.setAttribute('src' , 'https://robohash.org/'+ robot.id + '?size=200x200');
		box.appendChild(image);
		root.appendChild(box);
		box.appendChild(image);
		box.appendChild(name);
		box.appendChild(username);
		box.appendChild(email);

		name.innerText = robot.name;
		username.innerText = robot.username;
		email.innerText = robot.email;
}
}