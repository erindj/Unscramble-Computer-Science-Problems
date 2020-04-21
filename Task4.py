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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
#We create two sets, by definition a set cannot contain duplicate numbers
outgoing_calls = set()
not_telemarketers = set()

for call in calls:
    outgoing_calls.add(call[0])
    not_telemarketers.add(call[1])
for text in texts:
    not_telemarketers.add(text[0])
    not_telemarketers.add(text[1])

# Subtract not_telemarketers set to outgoing_calls to get the result
possible_telemarketers = sorted(outgoing_calls - not_telemarketers)

print('These numbers could be telemarketers: ')
for numbers in possible_telemarketers:
    print(numbers)