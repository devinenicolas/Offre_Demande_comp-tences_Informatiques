import requests

import json

  
# api-endpoint
URL = "https://authentification-candidat.pole-emploi.fr/connexion/oauth2/access_token/"
  
 
# defining a params dict for the parameters to be sent to the API
PARAMS = {Content-Type: application/x-www-form-urlencoded,

grant_type:authorization_code,
code:[authorization code],
client_id:[PAR_offreetdemandedecompe_1419c80c16f05e95859ad4a3ef8e5c1a85b845ec37c784a9a2301797b37ae787],
client_secret:[5e720543fc0ceb46167a2f0678d095da6686abdb7be238bc2ba2ca82f3d6eebe],
redirect_uri:[http://devine.fr]}
  
# sending get request and saving the response as response object
r = requests.post(url = URL, params = PARAMS)
  
# extracting data in json format
data = r.json()
  

# printing the output
print(data)

print(r.url)



