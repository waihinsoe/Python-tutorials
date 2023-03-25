# key = 'be9bc7caae8086ac9a66968a57eae6dd'
import json
from textwrap import indent
import requests
url = 'https://api.openweathermap.org/data/2.5/weather?appid=be9bc7caae8086ac9a66968a57eae6dd&q='
city = input('please enter your city name : ')
newUrl = url+city
jsonData = requests.get(newUrl).json()
print(jsonData["clouds"])

# coord weather   base      
# main      
# visibility
# wind      
# clouds    
# dt        
# sys       
# timezone  
# id        
# name      
# cod 