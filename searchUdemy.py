import os
import csv

udemy_csv = os.path.join("resources","Udemy_Web_Course.csv")

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

with open(udemy_csv, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])
        percent = round(int(row[6])/int(row[5]),2)
        review_percent.append(percent)
        new_length = row[9].split(" ")
        length.append(float(new_length[0]))

# Zip lists together
cleaned_csv = zip(title, price, subscribers, reviews, review_percent, length)

# Set the variable for output file
output_file = os.path.join("resources", "Cleaned_Udemy_Web_Course.csv")

# Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left", "Percent of Reviews", "Length of Course"])

    writer.writerows(cleaned_csv)