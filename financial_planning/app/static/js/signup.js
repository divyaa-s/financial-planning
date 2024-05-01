document.addEventListener('DOMContentLoaded', function() {
  // Add event listener to the form submit event
  document.getElementById("signup-form").addEventListener("submit", function(event) {
      event.preventDefault(); // Prevent the form from submitting by default

      // Get the values from the input fields
      var fullName = document.querySelector('input[type="text"]').value;
      var phoneNumber = document.querySelector('input[type="tel"]').value;
      var email = document.querySelector('input[type="email"]').value;
      var password = document.querySelector('input[type="password"]').value;

      // Here you can add your signup logic
      // For demonstration purposes, let's just log the values to the console
      console.log("Full Name:", fullName);
      console.log("Phone Number:", phoneNumber);
      console.log("Email:", email);
      console.log("Password:", password);

      // Here you can implement your actual signup logic
      // For now, let's assume signup is successful and redirect to a dashboard page
      window.location.href = "{% url 'dashboard'%}";
  });
});

// Function to redirect to the login page
function redirectToLogin() {
  window.location.href = "{% url 'login'%}";
}
