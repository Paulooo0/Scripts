import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response1 = requests.get('https://itunes.apple.com/search?entity=song&limit=1&term=' + sys.argv[1])
print(json.dumps(response1.json(), indent=2))


response2 = requests.get('https://itunes.apple.com/search?entity=song&limit=50&term=' + input('Your band: ').lower().strip())
object = response2.json()
for result in object['results']:
    print(result['trackName'])
