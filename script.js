let name = document.querySelector('#name');
let login = document.querySelector('#login');
let password = document.querySelector('#password');
let submit = document.querySelector('#submit');

let users = {};

function User(name,login,password) {
	this.name = name;
	this.login = login;
	this.password = password;
}

function creatId(user) {
	return Object.keys(user).length;
}

submit.addEventListener('click', () => {
	const nameUser = name.value;
	const loginUser = login.value;
	const passwordUser = password.value;

	const user = new User(nameUser,loginUser,passwordUser);
    
    const userId = 'User' + creatId(users);

    users[userID] = user;

    console.log(users);
    


})