document.getElementById("dataForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission

    // Get form data
    var name = document.getElementById("name").value;
    var age = document.getElementById("age").value;
    var email = document.getElementById("email").value;
    var subscribe = document.getElementById("subscribe").checked;

    // Create data object
    var data = {
        name: name,
        age: age,
        email: email,
        subscribe: subscribe
    };

    // Send data to Python server
    fetch("/submit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(responseData) {
        // Display response message
        var responseDiv = document.getElementById("response");
        responseDiv.innerHTML = responseData.message;
    })
    .catch(function(error) {
        console.log(error);
    });
});
