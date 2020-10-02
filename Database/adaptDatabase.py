import csv
import time
import random


def emptyItemInList(list):
    for item in list:
        if item == "":
            return True
    return False




tic = time.time()

with open("mydatabase.csv",'rt') as input_file:
    reader = csv.reader(input_file)
    headers = next(reader, None)

    newrows_parameters=[]
    newrows_results=[]

    ganaA=0
    ganaB=0

    for row in reader:
        if not emptyItemInList(row):
            if random.random()>0.5:
                newrows_parameters.append([row[3],              # Match Surface: Grass      3
                                        row[4],                 # Match Surface: Clay       4
                                        row[5],                 # Match Surface: Carpet     5
                                        row[6],                 # Match Surface: Hard       6
                                        row[7],                 # Player A Rank             7
                                        row[8],                 # Player A Points           8
                                        row[9],                 # Player A Age              9
                                        row[10],                # Player A Right-Handed     10
                                        row[11],                # Player A Left-Handed      11
                                        row[12],                # Player A Win Streak       12
                                        row[13],                # Player A Lose Streak      13
                                        row[14],                # Player A Grass Win Ratio  14
                                        row[15],                # Player A Clay Win Ratio   15
                                        row[16],                # Player A Carpet Win Ratio 16
                                        row[17],                # Player A Hard Win Ratio   17
                                        row[18],                # Player B Rank             18
                                        row[19],                # Player B Points           19
                                        row[20],                # Player B Age              20
                                        row[21],                # Player B Right-Handed     21
                                        row[22],                # Player B Left-Handed      22
                                        row[23],                # Player B Win Streak       23
                                        row[24],                # Player B Lose Streak      24
                                        row[25],                # Player B Grass Win Ratio  25
                                        row[26],                # Player B Clay Win Ratio   26
                                        row[27],                # Player B Carpet Win Ratio 27
                                        row[28]                # Player B Hard Win Ratio   28
                                        ])
                newrows_results.append("1")
                ganaA+=1
            else:
                newrows_parameters.append([row[3],              # Match Surface: Grass      3
                                        row[4],                 # Match Surface: Clay       4
                                        row[5],                 # Match Surface: Carpet     5
                                        row[6],                 # Match Surface: Hard       6
                                        row[18],                # Player B Rank             18
                                        row[19],                # Player B Points           19
                                        row[20],                # Player B Age              20
                                        row[21],                # Player B Right-Handed     21
                                        row[22],                # Player B Left-Handed      22
                                        row[23],                # Player B Win Streak       23
                                        row[24],                # Player B Lose Streak      24
                                        row[25],                # Player B Grass Win Ratio  25
                                        row[26],                # Player B Clay Win Ratio   26
                                        row[27],                # Player B Carpet Win Ratio 27
                                        row[28],                # Player B Hard Win Ratio   28
                                        row[7],                 # Player A Rank             7
                                        row[8],                 # Player A Points           8
                                        row[9],                 # Player A Age              9
                                        row[10],                # Player A Right-Handed     10
                                        row[11],                # Player A Left-Handed      11
                                        row[12],                # Player A Win Streak       12
                                        row[13],                # Player A Lose Streak      13
                                        row[14],                # Player A Grass Win Ratio  14
                                        row[15],                # Player A Clay Win Ratio   15
                                        row[16],                # Player A Carpet Win Ratio 16
                                        row[17]                # Player A Hard Win Ratio   17
                                        ])
                newrows_results.append("0")
                ganaB+=1

with open("mydatabase_params.csv",'wt') as output_file:
    output_file = csv.writer(output_file, lineterminator='\n')
    output_file.writerow(['Match_Surface_Grass','Match_Surface_Clay','Match_Surface_Carpet','Match_Surface_Hard','Player_A_Rank','Player_A_Points','Player_A_Age','Player_A_RightHanded','Player_A_LeftHanded','Player_A_Win_Streak','Player_A_Lose_Streak','Player_A_Grass_Win_Ratio','Player_A_Clay_Win_Ratio','Player_A_Carpet_Win_Ratio','Player_A_Hard_Win_Ratio','Player_B_Rank','Player_B_Points','Player_B_Age','Player_B_RightHanded','Player_B_LeftHanded','Player_B_Win_Streak','Player_B_Lose_Streak','Player_B_Grass_Win_Ratio','Player_B_Clay_Win_Ratio','Player_B_Carpet_Win_Ratio','Player_B_Hard_Win_Ratio'])
    output_file.writerows(newrows_parameters)

with open("mydatabase_results.csv",'wt') as output_file:
    output_file = csv.writer(output_file, lineterminator='\n')
    output_file.writerow(['Player_A_Wins'])
    output_file.writerows(newrows_results)

print("Gana A: " + str(ganaA) + " --- Gana B: " + str(ganaB))
print("Terminado en " + str(time.time()-tic) + " segundos.")
