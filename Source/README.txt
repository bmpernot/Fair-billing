Language used:
Python 2.7.17 on Ubuntu

How to execute:
enter the command line
navigate to the same folder which the program and log file is in
python Fair_Billing.py LogFile

Assumptions:
- The fields within log will always be white space separated.
- Each new line in the text file is a separate log entry.
- Start and end time values are only set using the first and last valid log entries.

Testing:
Black Box Testing:
Test_1:
The data that was given in the scenario.
Expected outcome:
ALICE99 4 240
CHARLIE 3 37
Actual outcome:
ALICE99 4 240
CHARLIE 3 37

Test_2:
Testing that only valid lines are used.
Expected outcome:
ALICE99 1 50
Actual outcome:
ALICE99 1 50

Test_3:
Test with only a single start and no end.
Expected outcome:
ALICE99 1 0
Actual outcome:
ALICE99 1 0

Test_4:
Test with only a single end and no start.
Expected outcome:
CHARLIE 1 0
Actual outcome:
CHARLIE 1 0

Test_5:
Test with only ends.
Expected outcome:
CHARLIE 2 92
ALICE99 4 377
Actual outcome:
CHARLIE 2 92
ALICE99 4 377

Test_6:
Test with only starts.
Expected outcome:
ALICE99 3 329
CHARLIE 2 99
Actual outcome:
ALICE99 3 329
CHARLIE 2 99

Test_7:
Test that the checks if the username accepts values with spaces.
Expected outcome:
Nothing as the entry is not valid
Actual outcome:
Nothing as the entry is not valid

Test_8:
Test that it will deny the input if the time is null.
Expected outcome:
Nothing as the entry is not valid
Actual outcome:
Nothing as the entry is not valid

Test_9:
Test that it will deny the input if the username is null.
Expected outcome:
Nothing as the entry is not valid
Actual outcome:
Nothing as the entry is not valid

Test_10:
Test that it will deny the input if the start/end is null.
Expected outcome:
Nothing as the entry is not valid
Actual outcome:
Nothing as the entry is not valid

Test_11:
Test all previous tests combine.
Expected outcome:
ALICE99 9 950
CHARLIE 6 818
Actual outcome:
ALICE99 9 950
CHARLIE 6 818

Unit Testing:
A variety of unit tests were created for the majority of the 
functions used in the program. All unit tests that were created passed. 