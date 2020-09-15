from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time

profile = webdriver.FirefoxProfile()
profile.set_preference('permissions.default.image', 2)
profile.set_preference("browser.download.folderList",2)
profile.set_preference("browser.download.manager.showWhenStarting",False)
profile.set_preference("browser.download.dir","C:\\Users\\PC\\repos\\TennisMatchPredictor\\WebScrapping\\CSV")
profile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain, application/octet-stream, application/binary, text/csv, application/csv, application/excel, text/comma-separated-values, text/xml, application/xml")
driver = webdriver.Firefox(profile)
f = open("playersID.txt",'w+')
f.close()
f = open("playersID.txt",'a')

for id in range(1,11094):
    t = time.time()
    url = "https://www.ultimatetennisstatistics.com/playerProfile?playerId=" + str(id)
    driver.get(url)

    driver.find_element_by_id("matchesPill").click()
    EC.presence_of_element_located((By.CLASS_NAME, "infos"))
    EC.text_to_be_present_in_element((By.CLASS_NAME, "infos"), "Showing")
    playerMatches = driver.find_element_by_class_name("infos").get_attribute("innerText").split()[5]
    if playerMatches == "0":
      continue
    driver.find_elements_by_class_name("dropdown-toggle")[12].click()
    driver.find_elements_by_class_name("dropdown-item-button")[3].click()

    EC.text_to_be_present_in_element((By.CLASS_NAME, "infos"), "Showing 1 to " + str(playerMatches) + " of " + str(playerMatches) + "entries")

    playerName = driver.find_element_by_tag_name("h3").get_attribute("innerText")[:-1]              # added [:-1] to remove the extra space at the end of the player's name
    driver.execute_script("downloadCsv(\"matchesTable\", \"" + playerName + ".csv\", [\"^id$\",\"tournamentEventId\",\"winner_id\",\"loser_id\",\"country_code\",\"hasStats\"])")
    time.sleep(1)
    f.write(str(id) + "," + playerName + "\n")
    print("Player: " + str(id) + "/11094 - " + str(round(time.time()-t,2)) + "s")

f.close()
driver.close()
driver.quit()
