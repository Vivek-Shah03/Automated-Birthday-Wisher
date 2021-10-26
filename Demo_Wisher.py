import datetime as dt
import pandas
import smtplib
import random
import pywhatkit

MY_EMAIL = "" #add your g-mail here
MY_PASSWORD = "" #add your g-mail password here

now = dt.datetime.now()
month = now.month
day = now.day

data = pandas.read_csv("birthdays.csv")


if __name__ == "__main__":
    for index, item in data.iterrows():
        if month == item.month and day == item.day:
            person_email = item.email
            person_name = item["name"]
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
                with open(file_path) as letter_file:
                    contents = letter_file.read()
                    contents = contents.replace("[NAME]", person_name)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=person_email,
                                    msg=f"Subject:Happy Birthday !\n\n{contents}")
            pywhatkit.sendwhatmsg(f"+91{item['num']}", contents, 19, 40)
