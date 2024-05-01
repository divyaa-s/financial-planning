// JavaScript code to handle select button clicks
document.addEventListener('DOMContentLoaded', function() {
    // Get all select buttons
    const selectButtons = document.querySelectorAll('.select-button');

    // Add event listener to each button
    selectButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Get the scheme name from the parent element
            const schemeName = this.parentNode.querySelector('h2').innerText;

            // Show an alert when a scheme is selected
            alert(`You have selected the ${schemeName} scheme.`);
        });
    });
});
