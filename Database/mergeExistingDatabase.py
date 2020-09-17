import csv
import sys

arguments = sys.argv
filePath = arguments[1]
firstFileNumber = int(arguments[2])
lastFileNumber = int(arguments[3])

with open('output.csv', mode='w') as output_file:
    output_file = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    output_file.writerow(['match_date','winner_name', 'winner_rank', 'winner_points', 'winner_age', 'winner_hand', 'loser_name', 'loser_rank', 'loser_points', 'loser_age', 'loser_hand', 'surface'])
    for i in range(firstFileNumber, lastFileNumber+1):
        filename = filePath + str(i) + ".csv"
        with open(filename) as input_file:
            csv_reader = csv.reader(input_file, delimiter=',')
            firstRow = True
            for row in csv_reader:
                if firstRow:
                    firstRow=False
                    continue
                output_file.writerow([row[5], row[10], row[45], row[46], row[14], row[11], row[18], row[47], row[48], row[22], row[19], row[2]])
