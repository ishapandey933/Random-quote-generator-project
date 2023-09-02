import random
from flask import Flask

app = Flask(__name__)

# Define a list of quotes
quotes = [
    "The best way to predict your future is to create it. - Abraham Lincoln",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",  "The purpose of our lives is to be happy. — Dalai Lama", 
 "Life is what happens when you're busy making other plans. — John Lennon",
"Get busy living or get busy dying. — Stephen King",
"You only live once, but if you do it right, once is enough. — Mae West",
"Many of life’s failures are people who did not realize how close they were to success when they gave up.– Thomas A. Edison",
"If you want to live a happy life, tie it to a goal, not to people or things.– Albert Einstein",
"Never let the fear of striking out keep you from playing the game.– Babe Ruth",
"Money and success don’t change people; they merely amplify what is already there. — Will Smith",
"Your time is limited, so don’t waste it living someone else’s life. Don’t be trapped by dogma – which is living with the results of other people’s thinking. – Steve Jobs"
]

@app.route('/')
def random_quote():
    # Generate a random index
    random_index = random.randint(0, len(quotes)-1)
    
    # Get a random quote from the list
    quote = quotes[random_index]

    # Return the quote in HTML format
    return f'<h1>{quote}</h1>'

if __name__ == '__main__':
    app.run()
