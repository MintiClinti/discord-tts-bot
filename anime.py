import requests

url = "https://jikan1.p.rapidapi.com/character/1/pictures"

headers = {
    'x-rapidapi-key': "3dddb91d33msh5fd837f6078b0efp1147e8jsn44499f7409d8",
    'x-rapidapi-host': "jikan1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)
response.json()


print(response.text[0])