import smtplib
import datetime as dt
import random


my_email = ""
password = ""
to_address = ""

date = dt.datetime.now()
day_of_week = date.weekday()
print(day_of_week)

if day_of_week == 5:

    with open("./quotes.txt") as quotes:
        quote_list = quotes.read().split("\n")
        random_quote = random.choice(quote_list)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_address,
            msg=f'Subject: Monday Motivation!\n\n{random_quote}')
