from flask.views import MethodView
from wtforms import Form, StringField, SubmitField

from flask import Flask, render_template, request

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template("index.html")


class CaloriesCalcPage(MethodView):
    def get(self):
        return render_template("calc.html")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calorie_calc', view_func=CaloriesCalcPage.as_view('calc_page'))

app.run(debug=True)