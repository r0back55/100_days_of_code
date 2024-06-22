import smtplib
import pandas as pd
import datetime as dt
import random


# Email credentials
MY_EMAIL = ""
PASSWORD = ""


# Get today's date
date = dt.datetime.now()
date_d = date.day
date_m = date.month


# Read the birthdays from the CSV file
data_frame = pd.read_csv("./birthdays.csv")


# Iterate through each row in the DataFrame
for index, row in data_frame.iterrows():
    to_address = row['email']

    # Check if today matches the birthday
    if row["month"] == date_m and row["day"] == date_d:

        # Select a random letter template
        num = random.randint(1, 3)
        with open(f"./letter_templates/letter_{num}.txt") as letter:
            letter_content = letter.read()

            # Replace the placeholder in the letter template with the current name
            new_letter = letter_content.replace("[NAME]", row["name"])

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=to_address,
                msg=f'Subject: Happy Birthday!\n\n{new_letter}')

        print("Letter sent!")
