# Python-LoopThroughcsvFileandWriteIntoNewFile

## Start File
![image](https://user-images.githubusercontent.com/52837649/90966207-c12a6180-e49d-11ea-99ce-f0dbed2fbe18.png)

## Task
* Create a Python application that reads the data on Udemy csv file
* Store the contents of the Title, Price, Subscriber Count, Number of Reviews, and Course Length into Python Lists
* Zip these lists together into a single tuple
* Write the contents of the extracted data into a CSV

## Finished File
![image](https://user-images.githubusercontent.com/52837649/90966659-fc7b5f00-e4a2-11ea-8b06-ee9ab180d3d7.png)

## Code 
```
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
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left", "Percent of Reviews", "Length of Course"])
    writer.writerows(cleaned_csv)
```


