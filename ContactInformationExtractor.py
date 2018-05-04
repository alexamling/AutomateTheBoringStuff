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


