document.addEventListener('DOMContentLoaded', function () {
    
    // activate dropdown on sidebar onclick of each dropdown_on_sidebar
    const dropdowns = document.querySelectorAll("#dropdown_on_sidebar");
    dropdowns.forEach((dropdown) => {
        dropdown.addEventListener("click", function () {
            const icon = dropdown.querySelector("i");
            const items = dropdown.nextElementSibling;
        if (icon.classList.contains("fa-chevron-down")) {
            icon.classList.remove("fa-chevron-down");
            icon.classList.add("fa-chevron-up");
            if (items.style.display) {
                items.style.display = "block";
            }
        } else {
            icon.classList.remove("fa-chevron-up");
            icon.classList.add("fa-chevron-down");
            items.style.display = "none";
        }
            })
    })


    // script for proper closing of profile modal
    $(function () {
        $('#modalClose').on('click', function () {
            $('#staticBackdrop').hide();
        })
    })
    $(function () {
        $('#btn-modalClose').on('click', function () {
            $('#staticBackdrop').hide();
        })
    })


    // script for proper closing of contact modal
    $(function () {
        $('#contact_modalClose').on('click', function () {
            $('#contactModal').hide();
        })
    })
    $(function () {
        $('#contact_modalClose1').on('click', function () {
            $('#contactModal').hide();
        })
    })

    // for sidebar closing on mobile devices
    $(".sidebar ul li").on('click', function () {   // on click of the sidebar list element, the list element will be highlighted
        $(".sidebar ul li.active").removeClass('active');
        $(this).addClass('active'); // if the screen is small, the sidebar will be closed on click of the sidebar list element
        if ($(window).width() <= 768) {
            $('.sidebar').removeClass('active');
        }

    });

    $('.open-btn').on('click', function () {    // on click of the open button, the sidebar will be opened
        $('.sidebar').addClass('active');

    });


    $('.close-btn').on('click', function () {    // on click of the close button, the sidebar will be closed
        $('.sidebar').removeClass('active');

    })

    $('.dashboard-content').on('click touchstart', function () {    // on click of the dashboard content, the sidebar will be closed
        if ($(window).width() <= 768) {
            $('.sidebar').removeClass('active');
        }
    });

    // javascript for changing of text color to red if amount is negative and green if positive in element with id sidebar_balance_color
    
    // get all elements with class sidebar_balance_color
    const elements = document.querySelectorAll('#sidebar_balance_color');
    elements.forEach(function(element) {
        const amount = element.getAttribute('data-color');
        if (amount < 0) {
            element.classList.remove('bg-dark');
            element.classList.add('bg-danger');
        } else {
            element.classList.remove('bg-dark');
            element.classList.add('bg-success');
        }
    });
})