import yagmail
import pandas
from news_feed import NewsFeed

df = pandas.read_excel("people.xlsx")


def send_mail():
    for index, row in df.iterrows():
        news_data_raw = NewsFeed(country=row['location'], category=row['interests'])
        news_data = news_data_raw.get_info()

        email = yagmail.SMTP(user="autopyt0@gmail.com", password="python_pro_course_1")
        email.send(to=row['email'], subject=f"This is your Daily {(row['interests']).title()} News \n",
                   contents=f"Hello, {(row['name']).title()}, here is your news. \n\n {news_data}")


send_mail()

