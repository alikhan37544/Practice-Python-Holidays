/* script.js */
window.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');
    
    form.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form submission
      
      // Get form values
      var name = document.getElementById('name').value;
      var age = document.getElementById('age').value;
      var email = document.getElementById('email').value;
      var subscribe = document.getElementById('subscribe').checked;
      
      // Display form values
      console.log('Name:', name);
      console.log('Age:', age);
      console.log('Email:', email);
      console.log('Subscribe:', subscribe);
      
      // You can perform further processing with the form data here
    });
  });
  