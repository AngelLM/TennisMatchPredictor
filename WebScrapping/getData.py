from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options

import time
import re
import sys,  traceback
import os

# Cierra todas las instancias del driver y cierra todos los procesos firefox.exe
def cerrarWebdriver(driver):
    try:
        driver.close()
        driver.quit()
        os.system("taskkill /f /im firefox.exe /T") 
    except:
        print("Cerrando el webdriver...")
    finally:    
        print("Webdriver cerrado.")
          
    
#Creacion de una instancia de firefox (visible)                           
#profile = webdriver.FirefoxProfile()
#profile.set_preference('permissions.default.image', 2)
#driver = webdriver.Firefox(profile)

dir_datos = "data"
try:
    os.rmdir(dir_datos)
    print ("Se elimina la carpeta '/"+dir_datos)
except FileNotFoundError:
    print ("No existe la carpeta '/"+dir_datos)
try:
    os.mkdir(dir_datos)
    print ("Se crea la carpeta '/"+dir_datos)
except:
    print("Ha ocurrido un error al crear la carpeta '/"+dir_datos)
    sys.exit()
    
#Creacion de una instancia de firefox (no visible)
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
#driver=webdriver.Remote("http://127.0.0.1:4444",desired_capabilities=options.to_capabilities())

fErrores = open(os.path.join(dir_datos,"errores.txt"),'w+')
fErrores.close()

fEstadisticas = open(os.path.join(dir_datos,"estadisticas.txt"),'w+')
fEstadisticas.close()


fErrores = open(os.path.join(dir_datos,"errores.txt"),'w')
fEstadisticas = open(os.path.join(dir_datos,"estadisticas.txt"),'w')

#for id in range(84,11094):    
for id in range(85,11094):

    #Control de excepciones: 
    # - Si hay problemas con algun jugador, continua con el siguiente. Guarda el id del jugador problematico en errores.txt(se borra en cada ejecucion)
    # - Si el usuario pulsa Ctrl+C, el programa se cierra
    try:

        t_jugador=time.time()
        total_partidos=0
        date=""
        tournament=""
        surface=""
        round=""
        win=""
        rank=""
        elo=""
        oponentName=""
        oponentRank=""
        oponentElo=""

        f = open(os.path.join(dir_datos,str(id) + ".txt"),'w+')
        f.close()
        f = open(os.path.join(dir_datos,str(id) + ".txt"),'w+')

        
        url = "https://www.ultimatetennisstatistics.com/playerProfile?playerId=" + str(id)
        driver.get(url)
        

        driver.find_element_by_id("matchesPill").click()
        # EC.text_to_be_present_in_element((By.CLASS_NAME, "infos"), "Showing 1 to ")
        EC.presence_of_element_located((By.CLASS_NAME, "infos"))
        EC.text_to_be_present_in_element((By.CLASS_NAME, "infos"), "Showing")
        
        innerText_attr=driver.find_element_by_class_name("infos").get_attribute("innerText")
        playerMatches = innerText_attr.split()[5]
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
            date = matchDetails[0].get_attribute("innerText")
            tournament = matchDetails[1].get_attribute("innerText")
            surface = matchDetails[2].get_attribute("innerText")
            round = matchDetails[3].get_attribute("innerText")

            if len(matchDetails[5].find_elements_by_class_name("rankings-badge"))!=2: # Check if there is Rank/Elo info for both players, if there is not, continue with the following match
                continue

            if matchDetails[4].get_attribute("innerText").find("W")>1:
                win = "W"
                rankingsA = (" " + re.sub(r"\([^)]*\)","",matchDetails[5].find_elements_by_class_name("rankings-badge")[0].get_attribute("innerText")) + " ").split("\n")
                rankingsB = (" " + re.sub(r"\([^)]*\)","",matchDetails[5].find_elements_by_class_name("rankings-badge")[1].get_attribute("innerText")) + " ").split("\n")
            else:
                win = "L"
                rankingsA = (" " + re.sub(r"\([^)]*\)","",matchDetails[5].find_elements_by_class_name("rankings-badge")[1].get_attribute("innerText")) + " ").split("\n")
                rankingsB = (" " + re.sub(r"\([^)]*\)","",matchDetails[5].find_elements_by_class_name("rankings-badge")[0].get_attribute("innerText")) + " ").split("\n")

            rankExists = False
            eloExists = False
            for ranking in rankingsA:
                if ranking.find("Rank")!=-1:
                    rank=ranking.strip()[5:]
                    rankExists = True
                elif ranking.find("Elo")!=-1:
                    elo = ranking.strip()[4:]
                    eloExists = True
            if rankExists==False:
                rank = "-1"
            if eloExists==False:
                elo = "-1"

            rankExists = False
            eloExists = False
            for ranking in rankingsA:
                if ranking.find("Rank")!=-1:
                    oponentRank=ranking.strip()[5:]
                    rankExists = True
                elif ranking.find("Elo")!=-1:
                    oponentElo=ranking.strip()[4:]
                    eloExists = True
            if rankExists==False:
                oponentRank = "-1"
            if eloExists==False:
                oponentElo = "-1"

            oponentName=re.sub(r"\([^)]*\)","",matchDetails[5].find_element_by_tag_name("a").get_attribute("innerText")).strip()

            #print("Player: " + str(id) + "/11094        Match:" + str(noMatches) + "/" + str(playerMatches))
            noMatches = noMatches + 1
            total_partidos = total_partidos + 1
            f.write(date + ", " + tournament + ", " +  surface + ", " + round + ", " + win + ", " + playerName +", " + rank + ", " + elo + ", " +  oponentName + ", " + oponentRank + ", " + oponentElo + "\n")
        f.close()
        #print("***** Estadisticas del jugador " + str(id)+" ******")
        t_jugador=time.time()-t_jugador
        print("Número de partidos del jugador "+ str(id) + ": "+str(total_partidos))
        #print("Tiempo ejecucion: "+str(t_jugador))
        fEstadisticas.write(str(id)+", "+str(total_partidos)+", "+str(t_jugador)+"\n")
    except KeyboardInterrupt:
        print("El usuario ha solicitado el fin de la ejecución")
        cerrarWebdriver(driver)
        sys.exit()
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Se ha producido un error con el jugador "+str(id))
        #print("Descripcion del error:", exc_type)
        #print("Valor:", exc_value)
        fErrores.write(str(id) + ", "+str(exc_type)+ ", "+str(exc_value)+"\n")
        traceback.print_tb(exc_traceback, limit=1, file=fErrores)
        fErrores.write("\n")
        
fErrores.close()
fEstadisticas.close()

cerrarWebdriver(driver)
sys.exit()
