document.addEventListener('DOMContentLoaded', function () {
    
    // activate dropdown on sidebar onclick of each dropdown_on_sidebar
    const dropdowns = document.querySelectorAll("#dropdown_on_sidebar");
    dropdowns.forEach((dropdown) => {
        dropdown.addEventListener("click", function () {
            const icon = dropdown.querySelector("i");
        if (icon.classList.contains("fa-chevron-down")) {
            icon.classList.remove("fa-chevron-down");
            icon.classList.add("fa-chevron-up");
        } else {
            icon.classList.remove("fa-chevron-up");
            icon.classList.add("fa-chevron-down");
        }
            })
    })
})