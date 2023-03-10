import requests
import json
api_ley='AIzaSyBT3E-vm38GLIIt4FuJjtD1HqR_nskTNCY'
url='https://www.googleapis.com/books/v1/volumes?q=isbn:978-3-16-148410-0&key='+api_ley

response=requests.get(url)
data=response.json()
print(data['items'][0]['volumeInfo'])