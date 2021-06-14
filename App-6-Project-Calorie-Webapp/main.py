from flask.views import MethodView
from wtforms import Form, StringField, SubmitField, RadioField

from flask import Flask, render_template, request

from temperature import Temperature
from calorie import Calorie

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template("index.html")


class CaloriesCalcFormPage(MethodView):
    def get(self):
        calc_form = CaloriesCalcForm()
        return render_template("calc.html", calcform=calc_form)

    def post(self):
        calcform = CaloriesCalcForm(request.form)
        weight = float(calcform.weight.data)
        height = float(calcform.height.data)
        age = float(calcform.age.data)
        city = calcform.city.data
        country = calcform.country.data
        the_temperature = Temperature(country, city).get()

        if isinstance(the_temperature, str):
            required_cal = "Incorrect city or country or other error."
        else:
            required_cal = f"The user required: {Calorie(weight, height, age, the_temperature).calculate()}"

        return render_template("calc.html", calcform=calcform, required_calories=required_cal)


class CaloriesCalcForm(Form):
    weight = StringField("Weight:", default=80)
    height = StringField("Height (sm):", default=170)
    age = StringField("Age:", default=30)
    city = StringField("City:", default='New-York')
    country = StringField("Country:", default='USA')
    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calorie_calc', view_func=CaloriesCalcFormPage.as_view('calc_page'))

app.run(debug=True)