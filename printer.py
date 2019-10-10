import csv 
import platform

def printFile(notSolved):

    if platform.system() == 'Windows': 
        newline=''
    else: 
        newline=None

    with open("output.csv", 'w', newline=newline) as output_file: 
        output_writer = csv.writer(output_file)
            
        for y in notSolved:
            output_writer.writerow(y)

            

def readFile():
    with open('output.csv', mode='r') as csv_file: 
        csv_reader = csv.reader(csv_file)
        grid = []
        for row in csv_reader:
            for col in row:
                grid.append(col)

        print(grid)