from flask import request, Flask, render_template, redirect, url_for
from peewee import *
from models import *
from playhouse.shortcuts import model_to_dict, dict_to_model


app = Flask(__name__)


@app.route("/")
def get_main_page():
    return render_template('main.html')


@app.route("/food_list")
def get_food_page():
    foods = []
    for food in Food.select():
        foods.append(model_to_dict(food))

    return render_template('food_list.html', foods=foods)


@app.route('/add_food', methods=["POST"])
def add_food():
    name = request.form['name']
    Food.create(name=name)
    return redirect('/food_list')


if __name__ == "__main__":
    app.run(use_reloader=True)
