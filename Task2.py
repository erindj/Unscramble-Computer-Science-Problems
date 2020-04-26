"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
#Initialize a dicitionary which will contain phone numbers as keys and call durations as values
phone_calls_duration = {}

for numbers in calls:
    caller = numbers[0]
    reciever = numbers[1]
    duration = int(numbers[3])

    if caller not in phone_calls_duration.keys():
        phone_calls_duration[caller] = duration
    else:
        phone_calls_duration[caller] += duration
       
    
    if reciever not in phone_calls_duration.keys():
        phone_calls_duration[reciever] = duration
    else:
        phone_calls_duration[reciever] += duration
        

phone_calls_duration



#Get the max value of the values in phone_calls_duration dictionary
longest_time_on_the_phone = max(phone_calls_duration.values()) 
#Iterate through the dictionary to extract the key 
phone_number = str([num for num, caller in phone_calls_duration.items() if caller == longest_time_on_the_phone])[2:-2]


print(f"{phone_number} spent the longest time, {longest_time_on_the_phone} seconds, on the phone during September 2016.")

