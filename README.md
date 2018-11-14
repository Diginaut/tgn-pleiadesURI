# tgn-Pleiades

This repository hosts code for different automated data manipulation for [Getty Thesaurus of Geographic Names® Online ID's](http://www.getty.edu/research/tools/vocabularies/tgn/) in xml files. For every script there is a version for manipulating a single xml file or for manipulating all xml files within a selected folder.

Please note that all programs require python3 and the following libraries: re, pathlib from Path, xml.etree.ElementTree, datetime, os and csv.

## Content
1. TGN key to URI
2. TGN key to URI (folder)
3. Add Pleiades URI
4. Add Pleiades URI (folder)

## How to
### Linux
Check for the installed Python version:
```
$ python3 --version
```
If not installed:
```
$ sudo apt-get update
$ sudo apt-get install python3.6
```
To run one of the scripts on Linux just start it in the terminal and follow the instructions. If the repository is in the 'Downloads' directory use:
```
$ python3 /home/user/Downloads/tgn-Pleiades/programName.py
```

### Windows
Check for installed Python version:
```
$ python --version
```
If not installed see [Python Download](https://www.python.org/downloads/windows/).

To run one of the scripts on Windows just start it in the command prompt (cmd) and follow the instructions. If the repository is in the 'Downloads' directory use:
```
$ python C:\Users\User\Downloads\tgn-Pleiades\programName.py
```

### macOS
Check for the installed Python version:
```
$ python3 --version
```
If not installed:
```
$ xcode-select --install
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew doctor
$ brew install python3
$ python3 --version
```

To run one of script on macOS just start it in the mac terminal and follow the instructions. If the repository is in Downloads use:
```
$ python3 Users/user/Downloads/programName.py
```

## TGN key to URI
In the selected xml file the script adds a *@ref* attribute (Getty URI) to every node with a *@key* attribute according to its [Getty Thesaurus of Geographic Names® Online ID](http://www.getty.edu/research/tools/vocabularies/tgn/ ).

### Example
#### Linux
Enter path to xml file:
```
> Status: Program started 2018-11-05 16:10:01.258239
> Enter path to import file: /home/user/Dokumente/myProject/file.xml
```
Enter folder where to save manipulated xml. Please note that the folder has to be created in advanced.
```
> Enter path to output folder: /home/user/Dokumente/myProject/output
```
Enter file name for manipulated xml:
```
> Enter output filename: manipulatedFile.xml
> Status: manipulatedFile.xml exported  2018-11-05 16:16:39.904738
```

#### Windows
```
Status: Program started 2018-11-05 16:10:01.258239
> Enter path to import file: C:\Users\User\Documents\myProject\file.xml
```
Enter folder where to save manipulated xml. Please note that the folder has to be created in advanced.
```
> Enter path to output folder: C:\Users\User\Documents\myProject\output\file.xml
```
Enter file name for manipulated xml:
```
> Enter output filename: manipulatedFile.xml
> Status: manipulatedFile.xml exported  2018-11-05 16:16:39.904738
```

#### macOS
Enter path to xml file:
```
> Status: Program started 2018-11-05 16:10:01.258239
> Enter path to import file: Users/user/Dokumente/myProject/file.xml
```
Enter folder where to save manipulated xml. Please note that the folder has to be created in advanced.
```
> Enter path to output folder: Users/user/Dokumente/myProject/output
```
Enter file name for manipulated xml:
```
> Enter output filename: manipulatedFile.xml
> Status: manipulatedFile.xml exported  2018-11-05 16:16:39.904738
```

## TGN key to URI (folder)
For every xml file in the selected folder this script adds a *@ref* attribute (Getty URI) to every node with a *@key* attribute according to its [Getty Thesaurus of Geographic Names® Online ID](http://www.getty.edu/research/tools/vocabularies/tgn/ ).

### Example
#### Linux
Enter path to folder with xml files:
```
> Status: Program started 2018-11-05 16:10:01.258239
> Enter input folder: /home/user/Dokumente/myProject/input
```
Enter folder where to save manipulated xml files. Please note that the folder has to be created in advanced and it should be different from the input folder. Otherwise the original xml files will be overwritten.
```
> Enter different output folder: /home/user/Dokumente/myProject/output
> Status: manipulatedFile1.xml exported  2018-11-05 16:16:39.904738
> Status: manipulatedFile2.xml exported  2018-11-05 16:16:39.904738
> Status: manipulatedFile3.xml exported  2018-11-05 16:16:39.904738
```

#### Windows
Enter path to folder with xml files:
```
> Status: Program started 2018-11-05 16:10:01.258239
> Enter input folder: C:\Users\User\Documents\myProject\input
```
Enter folder where to save manipulated xml files. Please note that the folder has to be created in advanced and it should be different from the input folder. Otherwise the original xml files will be overwritten.
```
> Enter different output folder: C:\Users\User\Documents\myProject\output
> Status: manipulatedFile1.xml exported  2018-11-05 16:16:39.904738
> Status: manipulatedFile2.xml exported  2018-11-05 16:16:39.904738
> Status: manipulatedFile3.xml exported  2018-11-05 16:16:39.904738
```


#### macOS
Enter path to folder with xml files:
```
> Status: Program started 2018-11-05 16:10:01.258239
> Enter input folder: Users/user/Dokumente/myProject/input
```
Enter folder where to save manipulated xml files. Please note that the folder has to be created in advanced and it should be different from the input folder. Otherwise the original xml files will be overwritten.
```
> Enter different output folder: Users/user/Dokumente/myProject/output
> Status: manipulatedFile1.xml exported  2018-11-05 16:16:39.904738
> Status: manipulatedFile2.xml exported  2018-11-05 16:16:39.904738
> Status: manipulatedFile3.xml exported  2018-11-05 16:16:39.904738
```

## Add Pleiades URI
On the basis of a concordance csv file (for further information see [pleiades-tgn](https://github.com/ryanfb/pleiades-tgn) from Ryan Baumann) the script adds (if possible) a *@ref* attribute with the [Pleiades](https://pleiades.stoa.org/) URI in a selected xml file.
### Example
#### Linux
For the concordance file there is a default path set to the file within the repository. You can change the path ('y') or use the default ('n').
```
> Status: Program started 2018-11-05 16:38:51.321148
> Do you want to change the default path to csv file? (y/n) y
```
If necessary set new path:
```
> Enter path to csv file: /home/user/Dokumente/csvFile.csv
```

```
> Enter path to import file: /home/user/Dokumente/file.xml
> Enter path to output folder: /home/user/Dokumente/output

> Enter output filename: manipulatedFile.xml

> Status: manipulatedFile.xml exported  2018-11-05 16:16:39.904738
```

#### Windows
For the concordance file there is a default path set to the file within the repository. You can change the path ('y') or use the default ('n').
```
> Status: Program started 2018-11-05 16:38:51.321148
> Do you want to change de default path to csv file? (y/n) y
```
If necessary set new path:
```
> Enter path to csv file: C:\Users\User\Documents\myProject\csvFile.csv
```

```
> Enter path to import file: C:\Users\User\Documents\myProject\file.xml
> Enter path to output folder: C:\Users\User\Documents\myProject\output

> Enter output filename: manipulatedFile.xml

> Status: manipulatedFile.xml exported  2018-11-05 16:16:39.904738
```

#### macOS
For the concordance file there is a default path set to the file within the repository. You can change the path ('y') or use the default ('n').
```
> Status: Program started 2018-11-05 16:38:51.321148
> Do you want to change the default path to csv file? (y/n) y
```
If necessary set new path:
```
> Enter path to csv file: Users/user/Dokumente/csvFile.csv
```

```
> Enter path to import file: Users/user/Dokumente/file.xml
> Enter path to output folder: Users/user/Dokumente/output

> Enter output filename: manipulatedFile.xml

> Status: manipulatedFile.xml exported  2018-11-05 16:16:39.904738
```



## Add Pleiades URI (folder)
On the basis of a concordance csv file (for further information see [pleiades-tgn](https://github.com/ryanfb/pleiades-tgn)) the script adds (if possible) a *@ref* attribute with the Pleiades URI for every xml file within the selected folder.

### Example
#### Linux
```
> Status: Program started 2018-11-05 16:38:51.321148
> Do you want to change de default path to csv file? (y/n) y
> Enter path to csv file: /home/user/Dokumente/csvFile.csv

> Enter path to import folder: /home/user/Dokumente/input
> Enter path to output folder: /home/user/Dokumente/output

> Status: manipulatedFile1.xml exported  2018-11-05 16:16:39.904738
> Status: manipulatedFile2.xml exported  2018-11-05 16:16:39.904738
> Status: manipulatedFile3.xml exported  2018-11-05 16:16:39.904738
```

#### Windows
```
> Status: Program started 2018-11-05 16:38:51.321148
> Do you want to change de default path to csv file? (y/n) y
> Enter path to csv file: C:\Users\User\Documents\myProject\csvFile.csv

> Enter path to import folder: C:\Users\User\Documents\myProject\input
> Enter path to output folder: C:\Users\User\Documents\myProject\output

> Status: manipulatedFile1.xml exported  2018-11-05 16:16:39.904738
> Status: manipulatedFile2.xml exported  2018-11-05 16:16:39.904738
> Status: manipulatedFile3.xml exported  2018-11-05 16:16:39.904738
```

#### macOS
```
> Status: Program started 2018-11-05 16:38:51.321148
> Do you want to change de default path to csv file? (y/n) y
> Enter path to csv file: Users/user/Dokumente/csvFile.csv

> Enter path to import folder: Users/user/Dokumente/input
> Enter path to output folder: Users/user/Dokumente/output

> Status: manipulatedFile1.xml exported  2018-11-05 16:16:39.904738
> Status: manipulatedFile2.xml exported  2018-11-05 16:16:39.904738
> Status: manipulatedFile3.xml exported  2018-11-05 16:16:39.904738
```
