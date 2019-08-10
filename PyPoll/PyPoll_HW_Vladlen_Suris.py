# This code was purely done in VSCode with importing of CVS instead of Pandas
## Decided to loop for PyPoll unlike PyBank

import os
import csv

electionData = os.path.join("C:\\Users\\Vlad\\Documents\\Data Analytics BootCamp\\Python HW\\PyPoll\\election_data.csv")

Candidates = []
numVotes = []
percentVotes = []
totalVotes = 0

with open(electionData, newline = "") as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ",")
    csvHeader = next(csvReader)

    for row in csvReader:
        totalVotes += 1
    
        if row[2] not in Candidates:
            Candidates.append(row[2])
            index = Candidates.index(row[2])
            numVotes.append(1)
        else:
            index = Candidates.index(row[2])
            numVotes[index] += 1
    
    for votes in numVotes:
        percentage = (votes/totalVotes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percentVotes.append(percentage)
    
    winner = max(numVotes)
    index = numVotes.index(winner)
    winningCandidate = Candidates[index]

print('Election Results')
print('--------------------------')
print(f'Total Votes: {str(totalVotes)}')
print("--------------------------")
for i in range(len(Candidates)):
    print(f'{Candidates[i]}: {str(percentVotes[i])} ({str(numVotes[i])})')
print('--------------------------')
print(f'Winner: {winningCandidate}')
print('--------------------------')

with open('C:\\Users\\Vlad\\Documents\\Data Analytics BootCamp\\Python HW\\PyPoll\\ElectionResults.txt','w+') as text_file:
    text_file.write('ElectionResults')
    text_file.write('\n')
    text_file.write('--------------------------')
    text_file.write('\n')
    text_file.write('Total Votes: ' + str(totalVotes))
    text_file.write('\n')
    for i in range(len(Candidates)):
        line = str(f'{Candidates[i]}: {str(percentVotes[i])} ({str(numVotes[i])})')
        text_file.write('{}\n'.format(line))
    text_file.write('--------------------------')
    text_file.write('\n')
    text_file.write(str(f'Winner: {winningCandidate}'))