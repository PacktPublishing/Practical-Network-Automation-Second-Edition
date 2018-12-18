 #use the city of london as a reference
 $city="london"
 $urlx="https://samples.openweathermap.org/data/2.5/weather?q="+$city+"&appid=b6907d289e10d714a6e88b30761fae22"
 $stuff = Invoke-RestMethod -Uri $urlx -Method Get

 #write raw json
$stuff

 #write the output of latitude and longitude
 write-host ("Longitude: "+$stuff.coord.lon+" , "+"Latitude: "+$stuff.coord.lat)
