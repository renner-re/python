# regex() method findall() is passed a string, and returns all matches in it, not just the first
# if the regex has 0 or 1 group, findall() returns a list of strings
# if regex has 2 or more groups, findall() returns a list of tuples of strings
# \d is shorthand for matching digits, /w matches word characters, \s matches whitespace characters
# the uppercase shorthand characters (\D, \W, \S) match characters that are NOT digits, word characters, and spaces
# you can make your own characters classes with square brackets [aeiou]
# a ^ (caret) makes it a negative characters class, matching anything not in the brackets ^[aeiou]

import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume = '''Ebony Moore
Portland, Oregon | (707) 555-0822 | emoore@email.com
Summary
&nbsp;
Recent graduate with a bachelor's degree in computer science and exemplary data analysis and engineering experience.
Education
&nbsp;
San Diego Technical College
Bachelor of Science in computer science
Experience
&nbsp;
HCORP, Secaucus, NJ, DevOps engineer
April 2020–Current
Create workflows for source code management to ensure efficiency and cut down on human error
Develop and maintained Ci/CD methodologies to speed the development process through automation
Design and implemented disaster recovery solutions in case of breach or server crash, as well as security measures like firewalls and VPNs
Update procedure documentation to improve training procedures and create lasting records of mastered skills for each employee to help with task delegation
Consult with clients and confirmed system power requirements to update design documents, test results and designs
Stanley Systems, Secaucus, NJ, Systems engineer
May 2017–April 2020
Served as team lead for two years
Performed in-depth root cause analysis by troubleshooting network and production issues periodically
Wrote automated Unix scripts to reduce manual labor and improve efficiency by 10%
Routing Co., Secaucus, NJ, Systems Intern
June 2016–September 2016
Assisted at all levels of the engineering process, including analysis, development, documentation, integration and testing
Attended meetings with clients and kept a record of client requests and project parameters
Developed processes to monitor systems and performed data collection while adhering to maintenance regulations
Certifications
&nbsp;
Amazon Web Services (AWS) Certified DevOps Engineer
Microsoft Certified Solutions developer
Skills
&nbsp;
Organization
Time management
Verbal and written communication
Attention to detail
Systems administration'''

phoneRegex.search(resume)
# returns the phone number in 'resume'
phoneRegex.findall(resume) # will find all instances of phone numbers in 'resume'
# If the regex string you're looking at doesn't has 1 or 0 groups (parentheses) it will
# return a list of strings and each string in that list os going to be the text
# that it found matching that pattern over

phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))') # generates 3 groups 
phoneRegex.findall(resume)
# returns a list of tuples of strings in 'resume'

# Shorthand Codes for Common Character Classes
# /d - numeric digit 1-9
# /D - character that is not a numeric digit 1-9
# /w - any letter, digit, or underscore character 
# /W - any character that is not a letter, digit, or underscore
# /s - any space, tab, or newline character
# /S - any character that is not a space, tab, or newline character

lyrics = '''12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing
, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds,
3 french hens, 2 turtle doves, and 1 partridge in a pear tree'''

xmasRegex = re.compile(r'\d+\s\w+')

# Making your own character classes
vowelRegex = re.compile(r'[aeiouAEIOU]') # r'(a|e|i|o|u)
vowelRegex.findall('Robocop eats baby food.')

# Negative character classes
vowelRegex = re.compile(r'[^aeiouAEIOU]') # finds all that are not vowels
