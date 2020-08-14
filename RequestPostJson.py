import requests, json

url = 'http://svc.saltlux.ai:31781'
headers = {'Content-Type': 'application/json; charset=utf-8'}
params = {
    'key': '',
    'serviceId': '',
    'argument': {
        'filename': 'https://www.w3.org/2001/sw/sweo/public/UseCases/SaltLux-KTF/KTF.pdf'
    }
}

response = requests.post(url, headers = headers, data = json.dumps(params))

print(response.content)