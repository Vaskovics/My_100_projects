import pandas
import datetime as dt
import smtplib
import random

NAME_HOLDER = "[NAME]"
##################### Extra Hard Starting Project ##################

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month

for birth in data_dict:
    if day == birth["day"] and month == birth["month"]:
        birthday = birth
name = birthday["name"]
email = birthday["email"]

# 3. If step 2 is true, pick a random letter from letter templates and replace the
# [NAME] with the person's actual name from birthdays.csv


with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
    letter_contents = letter_file.read()

new_letter = letter_contents.replace(NAME_HOLDER, name)

# 4. Send the letter generated in step 3 to that person's email address.
my_email = "v.vaskovics@gmail.com"
password = "Vitya2010"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=email,
                        msg=f"Subject: Happy Birthday\n\n{new_letter}")




