from flask.views import MethodView
from wtforms import Form, StringField, SubmitField

from flask import Flask, render_template, request

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template("index.html")


class CaloriesCalcFormPage(MethodView):
    def get(self):
        calc_form = CaloriesCalcForm()
        return render_template("calc.html", calcform=calc_form)


class ResultsPage(MethodView):

    def post(self):
        calcform = CaloriesCalcForm(request.form)
        weight = float(calcform.weight.data)
        height = float(calcform.height.data)

        # the_bill = Bill(amount, period)
        #
        # name_1 = calcform.name1.data
        # name_1_dates_in_house = float(calcform.days_in_house_1.data)
        # flatmate_1 = Flatmates(name_1, name_1_dates_in_house)
        #
        # name_2 = calcform.name2.data
        # name_2_dates_in_house = float(calcform.days_in_house_2.data)
        # flatmate_2 = Flatmates(name_2, name_2_dates_in_house)
        #
        # return render_template("results.html", name1=flatmate_1.name, amount1=flatmate_1.pays(the_bill, flatmate_2),
        #                        name2=flatmate_2.name, amount2=flatmate_2.pays(the_bill, flatmate_1))


class CaloriesCalcForm(Form):
    weight = StringField("Weight:", default=80)
    height = StringField("Height (sm):", default=170)
    age = StringField("Age:", default=30)
    city = StringField("City:", default='New-York')
    age = StringField("Country:", default='USA')

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calorie_calc', view_func=CaloriesCalcFormPage.as_view('calc_page'))

app.run(debug=True)