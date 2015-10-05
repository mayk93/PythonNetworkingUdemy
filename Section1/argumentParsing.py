'''
Basic argument parsing with the sys module.
'''
import sys

arguments = sys.argv
if len(arguments) >= 4:
    try:
        start = int(arguments[len(arguments)-2])
        end = int(arguments[len(arguments)-1])
    except Exception as e:
        print("Invalid start and end. Exception: "+str(e))
        start = 1
        end = 1
else:
    start = 1
    end = 1
if (start < 0 or start >= len(arguments)) or (end < 0 or end >= len(arguments)):
    print("Bad start or end.")
    print("Please check the last two arguments are greater than 0 and less than the number of previour arguments.")
    sys.exit()
if start > end:
    start,end=end,start

print("Start: "+str(start))
print("End: "+str(end))
print("Script called with arguments: "+str(arguments[start:end]))
