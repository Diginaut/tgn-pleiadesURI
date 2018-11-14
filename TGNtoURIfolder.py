import re
from pathlib import Path
import xml.etree.ElementTree as ET
import datetime
import os


key = ''
isPath = True

try:

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

except FileNotFoundError as fnfError:
    print(fnfError)
except ValueError as valueError:
    print(valueError)

else:
    ##############
    ### Import ###
    ##############

    for file in files:
        if '.xml' in file:
            try:
                tree = ET.parse(importFolder / file)
                root = tree.getroot()

            except FileNotFoundError as fnfError:
                print(fnfError)

            else:

                #################
                ### Parse xml ###
                #################

                # find all name-nodes
                for element in root.findall('.//*[@key]'):
                    # test if key = tgn no
                    if 'tgn' in element.get('key', ''):
                        # extract getty no from key attribute
                        key = re.search(r'(tgn,)(.*)', element.get('key', '')).group(2)
                        # create getty URI
                        key = 'http://vocab.getty.edu/tgn/' + key

                        # add getty URI als ref attribute
                        element.set('ref', key)


                ###########################
                ### Export new xml file ###
                ###########################
                try:
                    # write new xml document
                    exportFile = str(exportFolder / file)

                except FileNotFoundError as fnfError:
                    print(fnfError)

                else:

                    tree.write(exportFile)
                    print('Status: ' + file + ' exported', datetime.datetime.now())