import datetime
import re
import sys

def output_data(data): #used to loop through all users and print their data to the command line.
    for username in data:
        print('%s %d %s' % (username, data[username]["session"], data[username]["seconds"]))

def stack_cleanout(stack, end_time, data, time_format): #used for any remaining times in the stack that do not have an end
    for username in stack:
        for start_time in stack[username]: #if not it will pop the items off the list and use the last time on the log as an end time 
            amount_seconds = seconds(start_time, end_time, time_format)
            data = update_data(username, amount_seconds, data)
    return data

def update_data (username, seconds, data): # once the seconds are calculated the data dictionairy will need to be updated for the final data to be displayed
    data[username]["session"] = int(data[username]["session"]) + 1
    data[username]["seconds"] = int(data[username]["seconds"]) + int(seconds)
    return data

def seconds(start_time, end_time, time_format): # used to calculate the difference between two times in seconds
    difference = datetime.datetime.strptime(end_time, time_format) - datetime.datetime.strptime(start_time, time_format)
    seconds = difference.total_seconds()
    return seconds

def new_user(username, stack, data): #check if the user is new, if not they are added to the final data with values set at 0 and will be set an empty list in the stack dictionary
    if username not in stack:  
        data[username] = {"session": 0, "seconds": 0}
        stack[username] = []
    return data, stack
    
def start_or_end(line, data, time_format, stack, first_time): #checks if the log is a start or end session using regular expressions
    time = line[0:8]
    start_RE = re.findall(r"\b Start", line)
    end_RE = re.findall(r"\b End", line)
    if end_RE:
        X = re.split("\s", line)
        username = X[1] #find the username using regular expressions.
        data, stack = new_user(username, stack, data)
        try:
            start_time = stack[username].pop() #get a time from the users stack
        except IndexError:
            start_time = first_time #if fails it means that there is no time in the stack and the first time from the log will be used
        amount_seconds = seconds(start_time, time, time_format)
        data = update_data(username, amount_seconds, data)
    elif start_RE:
        X = re.split("\s", line)
        username = X[1]
        data, stack = new_user(username, stack, data)
        stack[username].append(time) # append to users stack
    return data, stack

def validate(line): #check the integrity of each log line
    integrity = False
    line = line.rstrip()
    X = re.split("\s", line)
    if len(X) == 3:
        if re.search("Start", X[2]) != None or re.search("End", X[2]) != None:
            if re.search("\d{2}:\d{2}:\d{2}", X[0]) != None:
                integrity = True
    return integrity

def main():
    data = {}
    stack = {}
    time_format = "%H:%M:%S"
    first_time = "" 
    last_time = "" 

    filename = sys.argv[1] #get the file name from the command line

    file = open(filename) # opening file in read only format

    for line in file:
        integrity = validate(line)
        if integrity == True:
            if first_time == "":
                first_time = line[0:8] #setting first time
                last_time = line[0:8] #setting last time
                data, stack = start_or_end(line, data, time_format, stack, first_time) #processing the log line
            else:
                last_time = line[0:8] #updating last time
                data, stack = start_or_end(line, data, time_format, stack, first_time) #processing the log line
            
    data = stack_cleanout(stack, last_time, data, time_format) #cleaning out all remaining sessions in the stack

    output_data(data) #output the data onto the command line

if __name__ == "__main__":
    sys.exit(main())

