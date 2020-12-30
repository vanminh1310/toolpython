import requests
import json

url = 'https://app.nanonets.com/api/v2/OCR/Model/f5fd3cab-c8a8-4acd-b17d-9a739d5f5ad3/LabelFile/'

data = {'file': open('/home/vanminh/Documents/ITS/img/510.png', 'rb')}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth('Ylb1YSLOhtTSIx1yt2dyLZuQepALVwSt', ''), files=data)
a = response.text
json_str = json.dumps(a)
print(response.text)
resp = json.loads(json_str)
print(resp)
print(str(resp['ocr_text']))