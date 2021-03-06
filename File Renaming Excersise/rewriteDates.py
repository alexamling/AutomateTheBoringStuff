#! python3
# rewriteDates.py
# This program is designed to:
# - Read through the name each file in the current directory
# - Identify dates in the American format MM-DD-YY
# - Rewrite the dates in European format DD-MM-YY

import shutil, os, re

# Regex for finding American Dates
americanDate = re.compile(r'''
    ^(.*?)                      # all text before the date
    ((0|1)?\d)-                  # the month
    ((0|1|2|3)?\d)-              # the day
    ((19|20)\d\d)                # the year
    (.*?)$                      # all text after the date
    ''', re.VERBOSE)

# Loop through all files in current directory
for americanFile in os.listdir('.'):
    # identify American dates
    match = americanDate.search(americanFile)

    # skip those without dates
    if match is None:
        continue

    # separate the sections of the date
    prefix = match.group(1)
    month = match.group(2)
    day = match.group(4)
    year = match.group(6)
    suffix = match.group(8)

    # build european date
    europeanFile = prefix + day + '-' + month + '-' + year + suffix

    # get absolute file path
    workingDirAbsolutePath = os.path.abspath('.')
    americanFile = os.path.join(workingDirAbsolutePath, americanFile)
    europeanFile = os.path.join(workingDirAbsolutePath, europeanFile)

    # Rename files
    print('Renaming "%s" to "%s"...' % (americanFile, europeanFile))
    # shutil.move(americanFile, europeanFile) # commented for testing purposes