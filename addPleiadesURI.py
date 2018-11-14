import re
from pathlib import Path
import xml.etree.ElementTree as ET
import datetime
import csv


# Classes

class GettyEntry:
    def __init__(self, gettyURL, pleiadesURL):
        self.gettyURL = gettyURL
        self.pleiadesURL = pleiadesURL


# Attributes

initKey = ''
importedCSV = []
choiceIsCorr = True
isXML = True
isPath = True

# Status
print('Status: Program started', datetime.datetime.now())

try:
    ##################################
    ### Importpath concordance csv ###
    ##################################

    # Change Path to tgn-pleiades concordance?
    choice = input('Do you want to change de default path to csv file? (y/n) ')
    while choiceIsCorr:
        if 'y' in choice:
            # Set new for csvFile
            CSVfile = Path(input('Enter path to csv file: '))

            choiceIsCorr = False

        elif 'n' in choice:
            CSVfile = Path('/home/diginaut/OneDrive/Dokumente/Uni/DigitaleMethodik/WS_18-19/Praxisprojekt/Pelagios/pleiades-tgn-master/pleiades-tgn.csv')
            choiceIsCorr = False

        elif not ('y' or 'n') in choice:
            print('Please enter \'y\' for yes or \'n\' for no.')


    ###########################
    ### Importpath xml file ###
    ###########################

    while isXML:
        # Import file
        importFile = str(input('Enter path to import xml file: '))

        if '.xml' in str(importFile):
            isXML = False
        else:
            print('No xml File detected, please try again. For further information see README.md.')


    ###########################
    ### Exportpath xml file ###
    ###########################

     # Test if folder path or file path
    while isPath:
        # Export
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

    # import csvFile
    with open (CSVfile, 'r', encoding='utf-8') as csvFile:
        csvFile = csv.reader(csvFile)
        # save ID's in list
        for line in csvFile:
            entry = GettyEntry(line[0], line[1])
            importedCSV.append(entry)


except FileNotFoundError as fnfError:
    print(fnfError)
except ValueError as valueError:
    print(valueError)

else:

    #####################
    ### Parse xmlFile ###
    #####################

    for element in root.findall('.//*[@key]'):
        # test if key = tgn no
        if 'tgn' in element.get('key', ''):
            # extract getty no from key attribute
            # '\d' does not work, match-function not supported
            key = re.search(r'(tgn,)(.*)', element.get('key', '')).group(2)
            # create getty URI
            key = 'http://vocab.getty.edu/tgn/' + key

            # compair getty URI with csvFile
            for entry in importedCSV:
                # if getty URI is in csv add getty URI and pleiades URI
                if key in entry.gettyURL:
                    # add pleiadesURL
                    element.set('ref', entry.pleiadesURL)


##########################
### Export new xmlFile ###
##########################
try:
    tree.write(exportFolder / exportFile)
    print('Status: ' + exportFile + ' exported ', datetime.datetime.now())

except FileNotFoundError as fnfError:
    print(fnfError)






















