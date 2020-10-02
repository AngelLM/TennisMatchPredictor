import csv
import time
import random


def emptyItemInList(list):
    for item in list:
        if item == "":
            return True
    return False

def ComputeSurfaceWinRatio(list, player):
    if list[3] == "1":
        if player==1:
            return list[14]
        else:
            return list[25]
    elif list[4] == "1":
        if player==1:
            return list[15]
        else:
            return list[26]
    elif list[5] == "1":
        if player==1:
            return list[16]
        else:
            return list[27]
    elif list[6] == "1":
        if player==1:
            return list[17]
        else:
            return list[28]
    else:
        return "NoSurface"

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
            surfaceWinRatioA = ComputeSurfaceWinRatio(row,1)
            surfaceWinRatioB = ComputeSurfaceWinRatio(row,2)
            if surfaceWinRatioA!="NoSurface":
                if random.random()>0.5:
                    newrows_parameters.append([row[7],              # Player A Rank             7
                                            row[8],                 # Player A Points           8
                                            row[9],                 # Player A Age              9
                                            row[10],                # Player A Right-Handed     10
                                            row[11],                # Player A Left-Handed      11
                                            row[12],                # Player A Win Streak       12
                                            row[13],                # Player A Lose Streak      13
                                            surfaceWinRatioA,       # Player A Surface Win Ratio
                                            row[18],                # Player B Rank             18
                                            row[19],                # Player B Points           19
                                            row[20],                # Player B Age              20
                                            row[21],                # Player B Right-Handed     21
                                            row[22],                # Player B Left-Handed      22
                                            row[23],                # Player B Win Streak       23
                                            row[24],                # Player B Lose Streak      24
                                            surfaceWinRatioB        # Player B Surface Win Ratio
                                            ])
                    newrows_results.append("1")
                    ganaA+=1
                else:
                    newrows_parameters.append([row[18],             # Player B Rank             18
                                            row[19],                # Player B Points           19
                                            row[20],                # Player B Age              20
                                            row[21],                # Player B Right-Handed     21
                                            row[22],                # Player B Left-Handed      22
                                            row[23],                # Player B Win Streak       23
                                            row[24],                # Player B Lose Streak      24
                                            surfaceWinRatioB,       # Player B Surface Win Ratio
                                            row[7],                 # Player A Rank             7
                                            row[8],                 # Player A Points           8
                                            row[9],                 # Player A Age              9
                                            row[10],                # Player A Right-Handed     10
                                            row[11],                # Player A Left-Handed      11
                                            row[12],                # Player A Win Streak       12
                                            row[13],                # Player A Lose Streak      13
                                            surfaceWinRatioA        # Player A Surface Win Ratio
                                            ])
                    newrows_results.append("0")
                    ganaB+=1

with open("mydatabase_params.csv",'wt') as output_file:
    output_file = csv.writer(output_file, lineterminator='\n')
    output_file.writerow(['Player_A_Rank','Player_A_Points','Player_A_Age','Player_A_RightHanded','Player_A_LeftHanded','Player_A_Win_Streak','Player_A_Lose_Streak','Player_A_Surface_Win_Ratio','Player_B_Rank','Player_B_Points','Player_B_Age','Player_B_RightHanded','Player_B_LeftHanded','Player_B_Win_Streak','Player_B_Lose_Streak','Player_B_Surface_Win_Ratio'])
    output_file.writerows(newrows_parameters)

with open("mydatabase_results.csv",'wt') as output_file:
    output_file = csv.writer(output_file, lineterminator='\n')
    output_file.writerow(['Player_A_Wins'])
    output_file.writerows(newrows_results)

print("Gana A: " + str(ganaA) + " --- Gana B: " + str(ganaB))
print("Terminado en " + str(time.time()-tic) + " segundos.")
