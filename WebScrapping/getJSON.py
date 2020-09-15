# -*- coding: utf-8 -*-
# Documentación módulo request:    https://es.python-requests.org/es/latest/user/quickstart.html

import requests
# La petición que se quiere hacer, que obtenemos de las peticiones que hace el propio navegador
# mientras hacemos una prueba de navegación. 
# Hay que refinar los parámetros.
# Un parámetro importante es el rowCount, que indica el número de filas a obtener
# La respuesta se puede guardar, y formatearla mediante esta utilidad: https://jsonformatter.curiousconcept.com/
url = 'https://www.ultimatetennisstatistics.com/matchesTable?playerId=85&current=1&rowCount=1000&sort%5Bdate%5D=desc&searchPhrase=&season=&fromDate=&toDate=&level=&bestOf=&surface=&indoor=&speed=&round=&result=&opponent=&tournamentId=&tournamentEventId=&outcome=&score=&countryId=&bigWin=false&_=1600193836659'
headers = {'Accept': 'application/json'}
response = requests.get(url, headers=headers)
print(response.text)