#%% [markdown]
# # PDF Parser
# Creation date: 2020-03-18

#%% Imports
import pandas as pd # To work similar to R in Python
import csv #To load the tags metadatas
import glob #To be able to dynamically load files matching pattern.
import os # To access the OS separator char.

#%% Constants Setup
pathInputFile = "data/interim/cdc/"
pathOutputFile = "data/processed/cdc/"

startFileName = "COVID-19-geographic-disbtribution-worldwide-"
endFileName = ".csv"

#%% Import metadata to use
rawFiles = glob.glob(os.path.join(pathInputFile, startFileName+"*"+endFileName))

file = max(rawFiles)

#%% Process Data Structure
fileName = file.split(os.sep)[-1]
print("Processing file: " + fileName)

currentColumns = ["DateRep", "Cases", "Deaths", "Countries and territories", "Pop_Data.2018"]
targetColumns = ["Date", "New confirmed cases", "New deaths", "Country", "Population"]

dfImported = pd.read_csv(file, header=0, encoding='utf-8', names = currentColumns, quoting=csv.QUOTE_NONNUMERIC, index_col=False, skipinitialspace=True)

dfImported.rename(columns=dict(zip(currentColumns, targetColumns)), inplace=True)

dfImported = dfImported[["Date", "Country", "Population", "New confirmed cases", "New deaths"]]

#%% Clean data
dfImported["Country"] = dfImported["Country"].replace("Cases_on_an_international_conveyance_Japan", "Diamond Princess").str.replace("_", " ")
dfImported.fillna(0, inplace=True)

#%% Sort data (for proper cumulative sum of Totals).
dfImported.sort_values(by=['Date', 'Country'], ascending = True, inplace=True)

#%% Calculate data
dfImported.loc[dfImported["Country"]=="Diamond Princess", ['Population']] = 3711 # February 4, 2020 at 6:00 PM PT https://www.princess.com/news/notices_and_advisories/notices/diamond-princess-update.html
dfImported['Total confirmed cases'] = dfImported.groupby("Country")['New confirmed cases'].transform(pd.Series.cumsum)
dfImported['Total deaths'] = dfImported.groupby("Country")['New deaths'].transform(pd.Series.cumsum)

#%% Align data types
dfImported["Date"] = dfImported["Date"].astype(str)
dfImported["Country"] = dfImported["Country"].astype(str)
dfImported["Population"] = dfImported["Population"].astype('int64')
dfImported["Total confirmed cases"] = dfImported["Total confirmed cases"].astype('int64')
dfImported["New confirmed cases"] = dfImported["New confirmed cases"].astype('int64')
dfImported["Total deaths"] = dfImported["Total deaths"].astype('int64')
dfImported["New deaths"] = dfImported["New deaths"].astype('int64')
    
#%% Prepare to write the parsing.
outputFilename = "CDC-COVID-19.csv"
dfImported.to_csv(pathOutputFile+outputFilename, index=False, quoting=csv.QUOTE_NONNUMERIC)