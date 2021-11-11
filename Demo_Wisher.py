import datetime as dt
import pandas
import smtplib
import random

MY_EMAIL = "" #add your g-mail here
MY_PASSWORD = "" #add your g-mail password here

#Get current day and month using datetime module
now = dt.datetime.now()
month = now.month
day = now.day

#reading data from csv file and storing it in variable named data
data = pandas.read_csv("birthdays.csv")

#Main function of the Program
if __name__ == "__main__":
    #Iterating the data
    for index, item in data.iterrows():            
        if month == item.month and day == item.day:
            person_email = item.email
            person_name = item["name"]
            #making connection with API
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                #Starting transport level security
                connection.starttls()           
                #log-in to the user g-mail account
                connection.login(MY_EMAIL, MY_PASSWORD)     
                #choose any one of the file from letter_templates folder
                file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"       
                with open(file_path) as letter_file:
                    #reading text file
                    contents = letter_file.read()       
                    #replacing the NAME with the person name from csv file
                    contents = contents.replace("[NAME]", person_name)    
                    #sending an e-mail
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=person_email,
                                    msg=f"Subject:Happy Birthday !\n\n{contents}")
           
