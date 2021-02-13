import csv


def fileWriter(filename, fileContents):
    with open(filename, mode='a') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(fileContents)
    csvFile.close()


def fileReader(filename):
    contents = []
    with open(filename, 'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for i in csvReader:
            if i:
                contents.append(i)
    csvFile.close()
    return contents


if __name__ == "__main__":
    # ("loginDetails.txt", ["mark", "pass"])
    list = fileReader("Database/loginDetails.txt")
    print(list)
