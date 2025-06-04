# Character Counting Program

import pprint # helps clean output

message = 'It was a bright cold day in April and the clocks were striking thirteen.'
count = {}
for character in message.upper(): # sets all characters in message to uppercase
    count.setdefault(character, 0) # if a key does not exist for character, create it and set it to 0
    count[character] = count[character] + 1 # increase the character count by 1 for each character

pprint.print(count)

