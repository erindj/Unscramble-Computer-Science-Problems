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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
"""
Part A
"""

#Part A
#The set will be our container for the prefixes
prefixes_of_calles_by_Bangalore = set()
#initializing two variables which we will need to solve Part B
total_number_of_calls_by_Bangalore = 0
total_numbers_of_calls_by_Bangalore_to_Bangalore = 0


for numbers in calls:
  if '(080)' in numbers[0]:
        #Icrementing total_number_of_calls_by_Bangalore so we can get the total number of calls by Bangalore numbers
        total_number_of_calls_by_Bangalore += 1
        #Adding prefixes of fixed lines to the set
        if '(0' in numbers[1]:
              fixed_numbers = numbers[1]
              prefixes_for_fixed_numbers = str(fixed_numbers.split(')')[0]+')')
              prefixes_of_calles_by_Bangalore.add(prefixes_for_fixed_numbers)
        #Adding prefixes of mobile phones to the set
        if '7' in numbers[1][0] or '8' in numbers[1][0] or '9' in numbers[1][0] :
              mobile_numbers = numbers[1]
              prefixes_for_mobile_numbers = mobile_numbers[0:4]
              prefixes_of_calles_by_Bangalore.add(prefixes_for_mobile_numbers)
        #Adding prefixes of telemarketers to the set, which not relevant 
        if '140' in numbers[1][0:3]:
              telemarketers_numbers = numbers[1]
              prefixes_telemarkters = telemarketers_numbers[0:3]
              prefixes_of_calles_by_Bangalore.add(prefixes_telemarkters)
        if '(080)' in numbers[1]:
              #Incrementing total_numbers_of_calls_by_Bangalore_to_Bangalore to get the total calls from Bangalore numbers to Bangalore numbers
              total_numbers_of_calls_by_Bangalore_to_Bangalore += 1
              

print("The numbers called by people in Bangalore have codes: ")
for prefixes in sorted([*prefixes_of_calles_by_Bangalore]):
  print(prefixes)

#Part B
#Calculating the percentage utilizing values we got from itaration
percentage_of_Bangalore_calls_towards_Bangalore = round((total_numbers_of_calls_by_Bangalore_to_Bangalore/total_number_of_calls_by_Bangalore)*100, 2)

print(f"{percentage_of_Bangalore_calls_towards_Bangalore} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")