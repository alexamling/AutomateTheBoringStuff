#! python3
# contactInformationExtractor - finds phone numbers and emails within text on  the clipboard

import re
import pyperclip

# phone Regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # area code
    (\s|-|\.)?          # separator
    (\d{3})             # first 3 digits
    (\s|-|\.)           # separator
    (\d{4})             # last 4 digits
    )''', re.VERBOSE)

# email Regex
emailRegex = re.compile(r'''(
    (.*)                # name
    (\@)                # @ symbol
    (\w*)               # domain name
    (\.)                # . symbol
    (\w*)               # domain ending
)''', re.VERBOSE)

# find matches on the clipboard
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall((text)):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# copy Results into Clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No contact information found')


