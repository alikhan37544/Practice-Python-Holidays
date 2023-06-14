document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission
    
    // Get form data
    var formData = new FormData(this);
    
    // Create an HTTP request
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "submit_form.py", true);
    
    // Set the content type header to send form data
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    
    // Define the callback function when the request completes
    xhr.onload = function() {
      if (xhr.status === 200) {
        console.log(xhr.responseText);
        // You can add code here to handle the response from the Python file
      }
    };
    
    // Send the form data
    xhr.send(new URLSearchParams(formData));
  });
  