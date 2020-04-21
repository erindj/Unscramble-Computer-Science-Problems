"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

unique_set = set()

for n in calls:
    outgoing_calls = n[0]
    incoming_calls = n[1]
    unique_set.add(outgoing_calls)
    unique_set.add(incoming_calls)

for n in texts:
    outgoing_texts = n[0]
    incoming_texts = n[1]
    unique_set.add(outgoing_texts)
    unique_set.add(incoming_texts)


print(f'There are {len(unique_set)} different telephone numbers in the records.')