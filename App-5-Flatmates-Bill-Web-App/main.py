from flask.views import MethodView
from wtforms import Form, StringField, SubmitField

from flatmates.flat import Bill, Flatmates

from flask import Flask, render_template, request

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template("index.html")


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template("bill_form_page.html",  billform=bill_form)


class ResultsPage(MethodView):

    def post(self):
        billform = BillForm(request.form)
        amount = float(billform.amount.data)
        period = billform.periods.data
        the_bill = Bill(amount, period)

        name_1 = billform.name1.data
        name_1_dates_in_house = float(billform.days_in_house_1.data)
        flatmate_1 = Flatmates(name_1, name_1_dates_in_house)

        name_2 = billform.name2.data
        name_2_dates_in_house = float(billform.days_in_house_2.data)
        flatmate_2 = Flatmates(name_2, name_2_dates_in_house)

        return render_template("results.html", name1=flatmate_1.name, amount1=flatmate_1.pays(the_bill, flatmate_2),
                               name2=flatmate_2.name, amount2=flatmate_2.pays(the_bill, flatmate_1))

class BillForm(Form):
    amount = StringField("Bill Amount:", default=200)
    periods = StringField("Periods:", default="March 2200")

    name1 = StringField("User 1 name:", default="Max")
    days_in_house_1 = StringField("Days in house:", default=20)

    name2 = StringField("User 2 name:", default="Tom")
    days_in_house_2 = StringField("Days in house:", default=15)

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/result_page', view_func=ResultsPage.as_view('result_page'))

app.run(debug=True)