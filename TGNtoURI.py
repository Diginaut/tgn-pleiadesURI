import re
from pathlib import Path
import xml.etree.ElementTree as ET
import datetime

##############
### Import ###
##############

print('Status: Program started', datetime.datetime.now())
key = ''
isXML = True
isPath = True

try:

    ###########################
    ### Importpath xml file ###
    ###########################

    # Test if path contains xmlFile
    while isXML:
        # Import file
        importFile = Path(input('Enter path to import file: '))

        if '.xml' in str(importFile):
            isXML = False
        else:
            print('No xml File detected, please try again. For further information see README.md.')


    ###########################
    ### Exportpath xml file ###
    ###########################

    # Test if folder path or file path
    while isPath:
        # Export path
        exportFolder = Path(input('Enter path to output folder: '))

        if '.xml' in str(exportFolder):
            print('Please enter a folder path, not a file path. For further information see README.md.')
        else:
            isPath = False


    # Export file
    exportFile = input('Enter output filename: ')
    # if filename does not contain data format, add .xml
    if '.xml' not in str(exportFile):
        exportFile += '.xml'


    # Open xml file
    tree = ET.parse(importFile)
    root = tree.getroot()

except FileNotFoundError as fnfError:
    print(fnfError)
except ValueError as valueError:
    print(valueError)

else:

    #################
    ### Parse xml ###
    #################

    # find all name-nodes
    for element in root.findall('.//*[@key]'):
        # test if key = tgn no
        if 'tgn' in element.get('key', ''):
            # extract getty no from key attribute
            # '\d' does not work?!
            key = re.search(r'(tgn,)(.*)', element.get('key', '')).group(2)
            # create getty URI
            key = 'http://vocab.getty.edu/tgn/' + key

            # add getty URI als ref attribute
            element.set('ref', key)


# matches places; match function not supported
# //name[matches(@key, \'tgn.*\')]

# matches key value of places
# //name[matches(@key, 'tgn.*')]/string(@key)

    ###########################
    ### Export new xml file ###
    ###########################

    try:

        tree.write(exportFolder / exportFile)
        print('Status: ' + exportFile + ' exported ', datetime.datetime.now())

    except FileNotFoundError as fnfError:
        print(fnfError)