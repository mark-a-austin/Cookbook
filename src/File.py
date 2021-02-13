import csv

def fileWriter(filename, fileContents):
    with open(filename, mode = 'a') as csvFile:
        csvWriter = csv.writer(csvFile, )