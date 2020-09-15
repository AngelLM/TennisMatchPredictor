from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import re
import time

profile = webdriver.FirefoxProfile()
profile.set_preference('permissions.default.image', 2)
driver = webdriver.Firefox(profile)

for id in range(1,20):
    t = time.time()
    dateList=""
    tournamentList=""
    surfaceList=""
    roundList=""
    winList=""
    rankList=""
    eloList=""
    oponentNameList=""
    oponentRankList=""
    oponentEloList=""

    f = open("prueba.txt",'w+')
    f.close()
    f = open("prueba.txt",'a')

    # url = "https://www.ultimatetennisstatistics.com/playerProfile?playerId=" + str(id)
    # profile = webdriver.FirefoxProfile()
    # profile.set_preference('permissions.default.image', 2)
    # driver = webdriver.Firefox(profile)

    url = "https://www.ultimatetennisstatistics.com/playerProfile?playerId=60"
    driver.get(url)


    driver.find_element_by_id("matchesPill").click()
    EC.presence_of_element_located((By.CLASS_NAME, "infos"))
    EC.text_to_be_present_in_element((By.CLASS_NAME, "infos"), "entries")
    playerMatches = driver.find_element_by_class_name("infos").get_attribute("innerText").split()[5]
    if playerMatches == "0":
      continue

    driver.find_elements_by_class_name("dropdown-toggle")[12].click()
    driver.find_elements_by_class_name("dropdown-item-button")[3].click()

    filterMenuButton = driver.find_elements_by_class_name("dropdown-toggle")[13]
    filterMenuButton.click()
    filters = filterMenuButton.find_element_by_xpath("./..").find_element_by_class_name("dropdown-menu").find_elements_by_tag_name("li")
    filtersValues = [True, True, True, False, True, True, False, True, False, False, False, False, False]

    for i in range(12):
        if (filtersValues[i]==True and not(filters[i].find_element_by_tag_name("input").get_attribute("checked")=="true")) or (filtersValues[i]==False and filters[i].find_element_by_tag_name("input").get_attribute("checked")=="true"):
            filters[i].click()

    EC.text_to_be_present_in_element((By.CLASS_NAME, "infos"), "Showing 1 to " + str(playerMatches) + " of " + str(playerMatches) + "entries")

    playerName = driver.find_element_by_tag_name("h3").get_attribute("innerText")[:-1]              # added [:-1] to remove the extra space at the end of the player's name
    matchesTable = driver.find_element_by_id("matchesTable").find_element_by_tag_name("tbody")
    matches = matchesTable.find_elements_by_tag_name("tr")

    noMatches = 1

    for match in matches:
        matchDetails = match.find_elements_by_tag_name("td");
        dateList=(matchDetails[0].get_attribute("innerText"))
        tournamentList=(matchDetails[1].get_attribute("innerText"))
        surfaceList=(matchDetails[2].get_attribute("innerText"))
        roundList=(matchDetails[3].get_attribute("innerText"))

        if matchDetails[4].get_attribute("innerText").find("W")>1:
            winList=("W")
            rankingsA = (" " + re.sub(r"\([^)]*\)","",matchDetails[5].find_elements_by_class_name("rankings-badge")[0].get_attribute("innerText")) + " ").split("\n")
            rankingsB = (" " + re.sub(r"\([^)]*\)","",matchDetails[5].find_elements_by_class_name("rankings-badge")[1].get_attribute("innerText")) + " ").split("\n")
        else:
            winList=("L")
            rankingsA = (" " + re.sub(r"\([^)]*\)","",matchDetails[5].find_elements_by_class_name("rankings-badge")[1].get_attribute("innerText")) + " ").split("\n")
            rankingsB = (" " + re.sub(r"\([^)]*\)","",matchDetails[5].find_elements_by_class_name("rankings-badge")[0].get_attribute("innerText")) + " ").split("\n")

        if rankingsA[0].find("Rank")!=-1:
            rankList=(rankingsA[0].strip()[5:])
        else:
            rankList=("-1")

        if rankingsA[1].find("Elo")!=-1:
            eloList=(rankingsA[1].strip()[4:])
        else:
            eloList=("-1")

        if rankingsB[0].find("Rank")!=-1:
            oponentRankList=(rankingsB[0].strip()[5:])
        else:
            oponentRankList=("-1")

        if rankingsB[1].find("Elo")!=-1:
            oponentEloList=(rankingsB[1].strip()[4:])
        else:
            oponentEloList=("-1")

        oponentNameList=(re.sub(r"\([^)]*\)","",matchDetails[5].find_element_by_tag_name("a").get_attribute("innerText")).strip())
        # print("Player: " + str(id) + "/11094        Match:" + str(noMatches) + "/" + str(playerMatches))
        # noMatches = noMatches + 1
        f.write(str(dateList) + ", " + str(tournamentList) + ", " +  str(surfaceList) + ", " + str(roundList) + ", " + str(winList) + ", " + str(playerName) +", " + str(rankList) + ", " + str(eloList) + ", " +  str(oponentNameList)+ ", " + str(oponentRankList) + ", " + str(oponentEloList) + "\n")
    # for j in range(len(dateList)):
    #     f.write(str(dateList[j]) + ", " + str(tournamentList[j]) + ", " +  str(surfaceList[j]) + ", " + str(roundList[j]) + ", " + str(winList[j]) + ", " + str(playerName) +", " + str(rankList[j]) + ", " + str(eloList[j]) + ", " +  str(oponentNameList[j])+ ", " + str(oponentRankList[j]) + ", " + str(oponentEloList[j]) + "\n")
    f.close()

    print(str(id)+": "+str(time.time()-t))
driver.close()
driver.quit()
