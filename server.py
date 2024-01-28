from flask import Flask
import random

app = Flask(__name__)

random_num = random.randint(0, 10)


@app.route("/")
def home_page():
    return '<h1>Guess a number between 0 and 9: </h1>' \
           '<img src="https://media.giphy.com/media/BmmfETghGOPrW/giphy.gif">' \
           '<h3>Note: Write your number after the url (i.e. 127.0.0.1:5000/your number)'


@app.route("/<int:num>")
def final_page(num):
    if num < random_num:
        return '<h1 style="color:blue;" >Too Low! Try again!</h1>' \
               '<img src="https://media.tenor.com/u-2k8TCqbCcAAAAC/really-low-neil-degrasse-tyson.gif">'
    elif num > random_num:
        return '<h1 style="color:green;" >Too HIgh! Try again!</h1>' \
               '<img src="https://media.tenor.com/km6qbyrUioQAAAAC/jimmy-mcmillan-too-damn-high.gif">'
    elif num == random_num:
        return '<h1 style="color:green;" >HA HA! You got me!</h1>' \
               '<img src="https://media.tenor.com/gw9yu6moHqsAAAAC/you-got-me-good.gif">'


if __name__ == "__main__":
    app.run(debug=True)
