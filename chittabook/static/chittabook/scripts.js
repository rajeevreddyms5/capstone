
document.addEventListener('DOMContentLoaded', function() {

    // run toggle password visibility on signup page
    if (document.querySelector('#id_password') && document.querySelector('.postion-relative')) {
        togglePasswordVisibility_login();
    }

    // run toggle password visibility on login page
    if (document.querySelector('#id_password1')) {
        togglePasswordVisibility_signup();
    }

     // run toggle password visibility on reauthentication page
     if (document.querySelector('#id_password') && document.querySelector('.reauthenticate')) {
        togglePasswordVisibility_reauthentication();
    }


    // error messages on page load linked to bootstrap alert danger
    let errorElements = document.getElementsByClassName('alert-error');
    [...errorElements].forEach(el => {el.classList.add('alert-danger')});


    // load auto dismiss alert
    auto_dismiss_alert();
});


// togglepassword visiblity function for sign up page
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

// togglepassword visiblity function for login page
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


// togglepassword visiblity function for reauthentication page
function togglePasswordVisibility_reauthentication() {
    const togglePassword = document.querySelector('#togglePasswordReauthenticate');

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

// Auto dismiss alert functionality
function auto_dismiss_alert() {
    let alert_list = document.querySelectorAll('.alert')
    alert_list.forEach(function(alert) {
        new bootstrap.Alert(alert);

        let alert_timeout = alert.getAttribute('data-timeout');
        setTimeout(() => {
            bootstrap.Alert.getInstance(alert).close();
        }, +alert_timeout);
    });
}
    
