#! python3
# contactInformationExtractor - finds phone numbers and emails within text on  the clipboard

import re
import pyperclip

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?   # area code
    (\s|-|\.)?           # separator
    (\d{3})              # first 3 digits
    (\s|-|\.)            # separator
    (\d{3})              # last 4 digits
    )''', re.VERBOSE)


# TODO: Create Email Regex

# TODO: Find Matches in Clipboard Text

# TODO: Copy Results into Clipboard
