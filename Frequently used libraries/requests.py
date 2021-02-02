# Install requests library first
import requests

target = ".....(some url)..."
response = requests.get(url=target)  # Get the url's information and store the response to response element.


text = response.text # Get URL's information as text format. (HTML)
json = response.json() # Get URL's information as json format

***
json.dumps() => Encoding: Convert the Python element to json type
json.loads() => Decoding: Convert json type to pythin type 
***
