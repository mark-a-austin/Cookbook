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
        count = 0
        for i in csvReader:
            if i and count != 0:
                contents.append(i)
            count += 1
    csvFile.close()
    return contents


if __name__ == "__main__":
    list = fileReader("../Database/accounts.csv")
    print(len(list))
    print(list)
