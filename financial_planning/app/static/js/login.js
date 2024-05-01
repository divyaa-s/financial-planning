document.getElementById("login-form").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent the form from submitting by default

  // Get the values from the input fields
  var email = document.querySelector('input[type="email"]').value;
  var password = document.querySelector('input[type="password"]').value;

  // You can add your authentication logic here
  // For demonstration purposes, let's just log the values to the console
  console.log("Email:", email);
  console.log("Password:", password);

  // Here you can implement your authentication logic
  // For now, let's assume login is successful and redirect to a dashboard page
  window.location.href = "dashboard.html";
});
