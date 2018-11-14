import re
from pathlib import Path
import xml.etree.ElementTree as ET
import datetime
import csv
import os

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

##############################
### Import concordance CSV ###
##############################

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
            CSVfile = Path('../pleiades-tgn-master/leiades-tgn.csv')
            choiceIsCorr = False

        elif not ('y' or 'n') in choice:
            print('Please enter \'y\' for yes or \'n\' for no.')


    ############################
    ### Importpath xml files ###
    ############################

    # Test if path contains xmlFile
    while isPath:
        # Import
        importFolder = Path(input('Enter input folder: '))

        if '.xml' in str(importFolder):
            print('Please enter a folder path, not a file path. For further information see README.md.')
        else:
            isPath = False

    isPath = True

    # Save filenames
    files = os.listdir(importFolder)


    ###########################
    ### Exportpath xml file ###
    ###########################

    # Export
    while isPath:
        exportFolder = Path(input('Enter different output folder: '))

        if '.xml' in str(exportFolder):
            print('Please enter a folder path, not a file path. For further information see README.md.')
        elif importFolder == exportFolder:
            print('Please enter different folder.')
        else:
            isPath = False


    ##################
    ### Import CSV ###
    ##################

    # import csvFile
    with open(CSVfile, 'r', encoding='utf-8') as csvFile:
        csvFile = csv.reader(csvFile)
        # save ID's in list
        for line in csvFile:
            entry = GettyEntry(line[0], line[1])
            importedCSV.append(entry)


    ### for every xmlFile in directory
    for XMLfile in files:

        if '.xml' in str(XMLfile):
            # open xmlFile
            tree = ET.parse(importFolder / XMLfile)
            root = tree.getroot()

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
                            # add getty URI als ref attribute
                            element.set('ref', entry.pleiadesURL)


            ##########################
            ### Export new xmlFile ###
            ##########################

            exportFile = exportFolder / XMLfile

            tree.write(exportFile)
            print('Status: ' + XMLfile + ' exported', datetime.datetime.now())

except FileNotFoundError as fnfError:
    print(fnfError)
except ValueError as valueError:
    print(valueError)






















