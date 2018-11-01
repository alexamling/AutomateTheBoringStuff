#! python3
# backupToZip.py
# Program intended to:
# copy the contents of its directory into a .zip file
# increment the name of the of the .zip for multiple backups

import zipfile, os


def BackupToZip():
    # Backup contents of folder into new .zip file
    os.chdir(os.getcwd())

    folder = '.'

    # figure out the proper name for the .zip file
    number = 1
    while True:
        zipFileName = os.path.basename(os.path.abspath('.')) + '_' + str(number) + '.zip'  # create new file name
        if not os.path.exists(zipFileName):  # check to see if this name is already in use
            break
        number += 1

    # create the zip file
    print('Creating %s backup...' % zipFileName)
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # walk through entire folder and compress the files
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % foldername)  # add current folder
        backupZip.write(foldername)

        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.endswith('.zip'):
                continue  # dont backup already zipped files
            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()
    print('done.')


BackupToZip()  # backup current directory
