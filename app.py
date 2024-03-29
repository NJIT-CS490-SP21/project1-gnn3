import os
from dotenv import load_dotenv, find_dotenv
import random
import requests 
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")

def foo():
    clientid = "b072122b54d34dd4b763ec520350c4bc"
    load_dotenv(find_dotenv())
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': clientid,
        'client_secret':os.getenv('clientsecret'),
    })
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)}
    lst = ['70wm2qxYZ4i2KqcyyH2GyT', '7KMqksf0UMdyA0UCf4R3ux', '4Ti0EKl2PVEms2NRMVGqNe']
    id = lst[random.randint(0, 2)]

    BASE_URL = 'https://api.spotify.com/v1/artists/'+ id +'/top-tracks?market=US'
    response = requests.get(BASE_URL, headers=headers)
    response = response.json()
    y = len(response['tracks'])-1
    x = random.randint(0, y)
    i = response['tracks'][x]['album']['images'][1]['url']
    a = response['tracks'][x]['album']['name']
    p = response['tracks'][x]['preview_url']
    n = response['tracks'][x]['name']
    lst = []
    for elm in range(len(response['tracks'][x]['artists'])):
        lst.append((response['tracks'][x]['artists'][elm]['name']))
    lst2=[]
    for elm in lst:
        for elm2 in elm.split(' '):
            lst2.append(elm2)
    for name in n.split(' '):
        lst2.append(name)
    
    BASE_URL = 'https://api.genius.com/search?q='
    for item in lst2:
        BASE_URL = BASE_URL+item+'%20'
    
    genius_token = os.getenv('genius_token')
    headers = {
        'Authorization': 'Bearer {token}'.format(token=genius_token)}

   
    response = requests.get(BASE_URL, headers=headers)
    response = response.json()
    n=n.lower()
    lyric= 0
    for what in (response['response']['hits']):
        if n== what['result']['full_title'].lower().split('by')[0].strip(' '):
            path=what['result']['path']
            page_url = "http://genius.com" + path
            lyric = requests.get(page_url)
            lyric = str(page_url)
            
            break
        
    return render_template("index.html", im=i, p=p, n=n, Lst=lst, a=a, Lenght=len(lst),lyric=lyric)
app.run(port=int(os.getenv('PORT', 8080)),
       host=os.getenv('IP', '0.0.0.0'), debug=True)
   
   

            
           
            
       
    
      
  