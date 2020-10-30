from flask import Flask  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# import statements, maybe some other routes
@app.route('/success')
def success():
    return "success"
# app.run(debug=True) should be the very last statement! 

@app.route


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.


