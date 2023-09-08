
document.addEventListener('DOMContentLoaded', function() {

    // toggle password visibility
    togglePasswordVisibility_signup();
    togglePasswordVisibility_login();

});


// togglepassword visiblity function
function togglePasswordVisibility_signup() {
    const togglePassword = document.querySelector('#togglePasswordSignup');

    const password1 = document.querySelector('#id_password1');
    const password2 = document.querySelector('#id_password2');

    const label = document.getElementById('togglePasswordLabel');

    togglePassword.addEventListener('click', function (e) {
        
        const type1 = password1.getAttribute('type') === 'password' ? 'text' : 'password';
        password1.setAttribute('type', type1);

        const type2 = password2.getAttribute('type') === 'password' ? 'text' : 'password';
        password2.setAttribute('type', type2);

        // toggle the eye slash icon
        this.classList.toggle('fa-eye-slash');

        label.innerHTML = label.innerHTML === 'Hide' ? 'Show' : 'Hide';
});
}


function togglePasswordVisibility_login() {
    const togglePassword = document.querySelector('#togglePasswordLogIn');

    const password = document.querySelector('#id_password');

    const label = document.getElementById('togglePasswordLabel');

    togglePassword.addEventListener('click', function (e) {
        
        const type1 = password.getAttribute('type') === 'password' ? 'text' : 'password';
        password.setAttribute('type', type1);

        // toggle the eye slash icon
        this.classList.toggle('fa-eye-slash');

        label.innerHTML = label.innerHTML === 'Hide' ? 'Show' : 'Hide';
});
}
