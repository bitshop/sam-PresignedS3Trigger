import requests
import pprint

# Configuration:
# filename = file to upload
filename='app.py'

# url = GET API for presigning
url = "https://vqdrwi0ee1.execute-api.us-east-1.amazonaws.com/Prod/PreSign"

# Get presign response
result = requests.get(url).json()

# Print some debug information
pp = pprint.PrettyPrinter(indent=4)
print ("Result from URL:")
pp.pprint(result)

print ("Send to: {}".format(result['url']))

# Get URL information for upload:
presign = result['url']
#Upload file to S3 using presigned URL
r = requests.post(presign['url'], data=presign['fields'], files={ 'file': open(filename, 'rb')})
# Expect a 204 (no response) for a successful upload

print(r.status_code)