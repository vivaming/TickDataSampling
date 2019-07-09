
#THIS MACRO IS ABOUT BUILDING

#IMPORT COMMAND

import os
import re

execfile("/Users/mingzhang/Documents/R/FX/PyLollyJar/PythonStartUp.py")


TickFolder = '/Users/mingzhang/Documents/TickData/GBPUSD'



# 1. LOIOP THROUGH THE FILES UNDER THE DESTINATION FOLDER THEN
# 2. SCAN THROUGH FILES AND IDENTIFY THE FILES SIZE THEN DECIDE IF IT REQUIRES TO READ THAT FILE



# DEFINE LIST TO COLLECT FOLDER INFORMATION
FolderLocationList = list()

    for root, dirs, files in os.walk(TickFolder):
    # files = [f for f in files if not f[0] == '.']
    # dirs[:] = [d for d in dirs if not d[0] == '/']
    # for dir_ in sorted(dirs):

        for folder in sorted(dirs):
                FolderLocation = os.path.join(root, folder)
                list.append(FolderLocationList, FolderLocation)


        #  THE REGEX NEEDS TO BE ADJUSTED


FolderNameRegex = re.compile(r'/[0-9]{2}/[0-9]{2}')
SelectedFolder = list(filter(FolderNameRegex.search, FolderLocationList))


                for i in SelectedFolder:
                        for SecondLevelRoot, SecondLevelDirs, SecondLevelFiles in os.walk(i):
                                # print(root)
                                # print(files)

                                for SecondLevelFile_ in sorted(SecondLevelFiles):
                                    #print(root + '/' + file_)
                                    TickFileLocation=SecondLevelRoot + '/' + SecondLevelFile_
                                    TickFileSize=os.path.getsize(TickFileLocation)
                                    print(TickFileLocation + '-' + str(TickFileSize))

                                    if TickFileSize > 0:
                                        #TRY TO CATCH THE ERROR  - WHEN THERE IS A CORRUPTED FILE PRINT ON LOG
                                        #THEN ADD IT TO EXCEPTION LIST
                                        try:
                                            TickDataRaw = bi5_to_df(TickFileLocation, '>3I2f')
                                        except:
                                            print(TickFileLocation + " is corrupted")







