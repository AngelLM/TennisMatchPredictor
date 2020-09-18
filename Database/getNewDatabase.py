import csv
import time

tic = time.time()

with open("output.csv",'rt') as input_file:
    reader = csv.reader(input_file)
    headers = next(reader, None)
    rows = sorted((r for r in reader if len(r) > 1), key=lambda r: int(r[0]))

Players=[]
newrows=[]

for row in rows:
    if row[1] not in Players:
        Players.append(row[1])
    if row[6] not in Players:
        Players.append(row[6])

    newrows.append([row[0],                         # Match Date                0
                    row[1],                         # Player A Name             1
                    row[6],                         # Player B Name             2
                    1 if row[11]=="Grass" else 0,   # Match Surface: Grass      3
                    1 if row[11]=="Clay" else 0,    # Match Surface: Clay       4
                    1 if row[11]=="Carpet" else 0,  # Match Surface: Carpet     5
                    1 if row[11]=="Hard" else 0,    # Match Surface: Hard       6
                    row[2],                         # Player A Rank             7
                    row[3],                         # Player A Points           8
                    round(float(row[4]),4) if row[4]!="" else "",         # Player A Age              9
                    1 if row[5]=="R" else 0,        # Player A Right-Handed     10
                    1 if row[5]=="L" else 0,        # Player A Left-Handed      11
                    0,                              # Player A Win Streak       12
                    0,                              # Player A Lose Streak      13
                    0,                              # Player A Grass Win Ratio  14
                    0,                              # Player A Clay Win Ratio   15
                    0,                              # Player A Carpet Win Ratio 16
                    0,                              # Player A Hard Win Ratio   17
                    row[7],                         # Player B Rank             18
                    row[8],                         # Player B Points           19
                    round(float(row[9]),4) if row[9]!="" else "",         # Player B Age              20
                    1 if row[10]=="R" else 0,       # Player B Right-Handed     21
                    1 if row[10]=="L" else 0,       # Player B Left-Handed      22
                    0,                              # Player B Win Streak       23
                    0,                              # Player B Lose Streak      24
                    0,                              # Player B Grass Win Ratio  25
                    0,                              # Player B Clay Win Ratio   26
                    0,                              # Player B Carpet Win Ratio 27
                    0,                              # Player B Hard Win Ratio   28
                    1                               # Player A Wins             29
                    ])

for player in Players:
    winStreak = 0
    loseStreak = 0
    grassMatchesW = 0
    grassMatchesTotal = 0
    clayMatchesW = 0
    clayMatchesTotal = 0
    carpetMatchesW = 0
    carpetMatchesTotal = 0
    hardMatchesW = 0
    hardMatchesTotal = 0

    for row in newrows:
        if row[1] == player or row[2] == player:
            if row[1] == player:                    # Player Won
                row[12] = winStreak
                row[13] = loseStreak
                row[14] = round((grassMatchesW/grassMatchesTotal),4) if grassMatchesTotal>0 else 0
                row[15] = round((clayMatchesW/clayMatchesTotal),4) if clayMatchesTotal>0 else 0
                row[16] = round((carpetMatchesW/carpetMatchesTotal),4) if carpetMatchesTotal>0 else 0
                row[17] = round((hardMatchesW/hardMatchesTotal),4) if hardMatchesTotal>0 else 0

                winStreak += 1
                loseStreak = 0
                if row[3] == 1:
                    grassMatchesW+=1
                    grassMatchesTotal+=1
                if row[4] == 1:
                    clayMatchesW+=1
                    clayMatchesTotal+=1
                if row[5] == 1:
                    carpetMatchesW+=1
                    carpetMatchesTotal+=1
                if row[6] == 1:
                    hardMatchesW+=1
                    hardMatchesTotal+=1

            if row[2] == player:                    # Player Lost
                row[23] = winStreak
                row[24] = loseStreak
                row[25] = round((grassMatchesW/grassMatchesTotal),4) if grassMatchesTotal>0 else 0
                row[26] = round((clayMatchesW/clayMatchesTotal),4) if clayMatchesTotal>0 else 0
                row[27] = round((carpetMatchesW/carpetMatchesTotal),4) if carpetMatchesTotal>0 else 0
                row[28] = round((hardMatchesW/hardMatchesTotal),4) if hardMatchesTotal>0 else 0

                winStreak = 0
                loseStreak += 1
                if row[3] == 1:
                    grassMatchesTotal+=1
                if row[4] == 1:
                    clayMatchesTotal+=1
                if row[5] == 1:
                    carpetMatchesTotal+=1
                if row[6] == 1:
                    hardMatchesTotal+=1

with open("mydatabase.csv",'wt') as output_file:
    output_file = csv.writer(output_file, lineterminator='\n')
    output_file.writerow(['Match_Date','Player_A_Name','Player_B_Name','Match_Surface_Grass','Match_Surface_Clay','Match_Surface_Carpet','Match_Surface_Hard','Player_A_Rank','Player_A_Points','Player_A_Age','Player_A_RightHanded','Player_A_LeftHanded','Player_A_Win_Streak','Player_A_Lose_Streak','Player_A_Grass_Win_Ratio','Player_A_Clay_Win_Ratio','Player_A_Carpet_Win_Ratio','Player_A_Hard_Win_Ratio','Player_B_Rank','Player_B_Points','Player_B_Age','Player_B_RightHanded','Player_B_LeftHanded','Player_B_Win_Streak','Player_B_Lose_Streak','Player_B_Grass_Win_Ratio','Player_B_Clay_Win_Ratio','Player_B_Carpet_Win_Ratio','Player_B_Hard_Win_Ratio','Player_A_Wins'])
    output_file.writerows(newrows)

print("Terminado en " + str(time.time()-tic) + " segundos.")
