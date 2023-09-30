from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__) 


# Create a new instance of the Flask class called "app"
@app.route('/play/<int:x>/<color>')  
def playground(x = 5, color = "blue"):
    print(f"color is----> {type(color)}")
    return render_template("index.html", x = x, color = color)

@app.route('/')
def hello():
    return "hello"





if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.