import requests


city="london"

#this would give a sample data of the city that was used in the variable
urlx="https://samples.openweathermap.org/data/2.5/weather?q="+city+"&appid=b6907d289e10d714a6e88b30761fae22"

#send the request to URL using GET Method
r = requests.get(url = urlx)
output=r.json()

#parse the valuable information from the return JSON
print ("Raw JSON \n")
print (output)
print ("\n")

#fetch and print latitude and longitude
citylongitude=output['coord']['lon']
citylatitude=output['coord']['lat']
print ("Longitude: "+str(citylongitude)+" , "+"Latitude: "+str(citylatitude))
