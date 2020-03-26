#%% [markdown]
# # PDF Parser
# Creation date: 2020-03-18

#%% Imports
import pandas as pd # To work similar to R in Python
import csv #To load the tags metadatas
import glob #To be able to dynamically load files matching pattern.
import os # To access the OS separator char.

#%% Constants Setup
pathInputFile = "data/raw/cdc/"
pathOutputFile = "data/interim/cdc/"

startFileName = "COVID-19-geographic-disbtribution-worldwide-"
endFileName = ".xlsx"

#%% Import metadata to use
rawFiles = glob.glob(os.path.join(pathInputFile, startFileName+"*"+endFileName))

#%% Process Data Structure
for file in rawFiles:
    fileName = file.split(os.sep)[-1]
    print("Processing file: " + fileName)

    dfImported = pd.read_excel(file, header=0, encoding='utf-8', parse_dates=["DateRep"])
    dfImported.drop(["Day", "Month", "Year"], axis=1, inplace=True)
    
    #%% Prepare to write the parsing.
    outputFilename = fileName.split(".")[-2] + ".csv"
    dfImported.to_csv(pathOutputFile+outputFilename, index=False, quoting=csv.QUOTE_NONNUMERIC)