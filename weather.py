"""import requests

city=input('enter city name ')
url=f"https://wttr.in/{city}?format=3"
response=requests.get(url=url)
if response.status_code==200: #الرقم 200 يعني الاستجابة response تمت بصورة صحيحة
    print (f'weather informatin: {response.text}')
else:
    print("faild to get weather data")"""

import requests
url=f"https://official-joke-api.appspot.com/random_joke"
response=requests.get(url=url)
if response.status_code==200: #الرقم 200 يعني الاستجابة response تمت بصورة صحيحة
    joke=response.json()
    print(f"{joke['setup']}")
    print(f"{joke['punchline']}")
    print(joke)
else:
    print("faild to get weather data")

