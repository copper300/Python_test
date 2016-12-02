str1 = ''
str2 = 'geeks'

# repr is used to print the string along with the quotes
print repr(str1 and str2) # Return str1
print repr(str2 and str1) # Return str1
print repr(str1 or str2) # Return str2
print repr(str2 or str1) # Return str2

str1 = 'for'

print repr(str1 and str2) # Retrun str2
print repr(str2 and str1) # Return str1
print repr(str1 or str2) # Return str1
print repr(str2 or str1) # Return str2

line = "Geek1 \nGeek2 \nGeek3"
print(line.split())
print(line.split(' ',1))

# Python program to demonstrate the use of formatting using %

# Initialize variable as a string
variable = '15'
string = "Variable as string = %s" % (variable)
print string

# Convert the variable to integer
# And perform check other formatting options
variable = int(variable)
string = "Variable as integer = %d" % (variable)
print string
print("Variable as float = %f" % (variable))
print("Variable as hexadecimal = %X" % (variable))
print("Variable as octal = %o" % (variable))

# A Python program to demonstrate working of re.match().
import re

# Let use a regular expression to match a date string
# in the form of Month name of followed by day number
regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "I was born on June 24")
if match != None:
    # We reach here when the expression "([a-zA-Z]+) (\d+)"
    # matches the date string.

    # This will print [14, 21), since it matches at index 14
    # and ends at 21.
    print("Match at index %s, %s" % (match.start(), match.end()))
    # We use group() method to get all the matches and
    # captured groups. The groups contain the matched values.
    # In particular:
    #   match.group(0) always returns the fully matched string
    #   match.group(1) match.group(2), ... return the capture
    #   groups in order from left to right in the inpu string
    #   match.group() is equivalent to match.group(0)

    # So this will print "June 24"
    print("Full match: %s" % (match.group(0)))
    # So this will print "June"
    print("Month: %s" % (match.group(1)))
    # So this will print "24"
    print("Day: %s" % (match.group(2)))

# A Python program to demonstrate working
# of re.match()

# a sample function that uses regular expressions
# to find month and day of a date.
def findMonthAndDate(string):
    regex = r"([a-zA-Z]+) (\d+)"
    match = re.match(regex, string)
    if match == None:
        print("Not a valid date")
        return

    print ("Given Data: %s" % (match.group()))
    print ("Month: %s" % (match.group(1)))
    print("Day: %s" % (match.group(2)))

# Driver Code
findMonthAndDate("June 24")
print("")
findMonthAndDate("I was born on June 24")

# A Python program to demonstrate working of
# findall()
# A sample text string where regular expression
# is searched.
string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""

# A sample regular expression to find digits.
regex = "\d+"
match = re.findall(regex, string)
print(match)
