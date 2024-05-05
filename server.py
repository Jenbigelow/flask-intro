"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

BADNESS =['sad', 'awful']

@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page. <a href= '/hello'>Hello!</a></html>"


@app.route('/hello')
def say_hello():
        
    """Say hello and prompt for user's name."""
# loop through AWESOMENESS to generate HTML options
# for adjective in AWESOMENESS
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
          <label for="adjective-select">Choose an adjective:</label>

          <select name="adjective" id="adjective-select">
          <option value="">--Please choose an option--</option>
          <option value="{AWESOMENESS[0]}">{AWESOMENESS[0]}</option>
          <option value="{AWESOMENESS[1]}">{AWESOMENESS[1]}</option>
          <option value="{AWESOMENESS[2]}">{AWESOMENESS[2]}</option>
          <option value="{AWESOMENESS[3]}">{AWESOMENESS[3]}</option>
          <option value="{AWESOMENESS[4]}">{AWESOMENESS[4]}</option>
          <option value="{AWESOMENESS[5]}">{AWESOMENESS[5]}</option>

</select>
</form>
        <form action="/diss">
          What's your name? <input type="text" name="bad_person">
          <input type="submit" value="Submit">
          <label for="adjective-select">Choose an adjective:</label>

          <select name="negative_adjective" id="bad_adjective-select">
          <option value="">--Please choose an option--</option>
          <option value="{BADNESS[0]}">{BADNESS[0]}</option>
          <option value="{BADNESS[1]}">{BADNESS[1]}</option>


</select>

        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
  
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("adjective")

    # compliment = choice(AWESOMENESS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/diss')
def diss_person():
      
    """Get user by name."""

    player = request.args.get("bad_person")
    diss = request.args.get("negative_adjective")

    # compliment = choice(AWESOMENESS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0", port=5001)
