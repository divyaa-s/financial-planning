document.addEventListener('DOMContentLoaded', function() {
    var changePasswordBtn = document.getElementById('change-password-btn');
    var changePasswordForm = document.getElementById('change-password-form');
    var responseMessages = document.getElementById('response-messages');

    // Show the change password form when the button is clicked
    changePasswordBtn.addEventListener('click', function() {
        changePasswordForm.style.display = 'block';
    });

    // Submit the form using AJAX when it's submitted
    changePasswordForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission
        
        var formData = new FormData(changePasswordForm);

        // Send the form data using AJAX
        fetch('/change_password/', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Password changed successfully
                responseMessages.textContent = 'Your password was successfully updated!';
                changePasswordForm.reset(); // Clear the form
                changePasswordForm.style.display = 'none'; // Hide the form
            } else {
                // Display error message
                responseMessages.textContent = data.error || 'Failed to change password. Please try again.';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            responseMessages.textContent = 'An error occurred while processing your request. Please try again later.';
        });
    });
});
