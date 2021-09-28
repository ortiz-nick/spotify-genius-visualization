import config
import requests

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': config.SPOTIFY_CLIENT_ID,
    'client_secret': config.SPOTIFY_CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer BQCZjEv1AXGSuhME68pLaegB1u-LbPEKf1N-r5Z5eluuNOvoRYNEJzxUOo8QzYm9E_E2JTmsLkqB_C4XEA7FfX3u9XtAGxQ61fdpxFRPqvs5KGKkQUm3g27PsnNSfOMMrV7kHsB9oDUKTe5Z0rS_cg'.format(token=access_token)
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'


# actual GET request with proper header
response = requests.get(BASE_URL + 'me/player/recently-played?limit=10', headers=headers)

print(response)

json_response = response.json()

trackName = []
trackArtist = []

for i in json_response['items']:
		# print(i["track"]['name'], ' --- ',  i["track"]['artists'][0]['name'])
		trackName.append(i["track"]['name'])
		trackArtist.append(i["track"]['artists'][0]['name'])

zip_iterator = zip(trackName, trackArtist)
trackDetails = dict(zip_iterator)
