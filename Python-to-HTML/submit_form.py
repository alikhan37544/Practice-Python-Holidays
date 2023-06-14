import cgi

# Get form data from the request
form = cgi.FieldStorage()

# Get values by field name
name = form.getvalue("name")
age = form.getvalue("age")
email = form.getvalue("email")

# Do something with the form data
# For example, print the values
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Email: {email}")
