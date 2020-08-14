import os
import base64
import requests
import json

# audio_path = "./004KI025(16kh).wav"
audio_path = "./001KI001(8kh).wav"
audio_file = open(audio_path, 'rb')
bytebuffer = bytearray(audio_file.read())
audio_file.close()

audio_base64_encoding = base64.b64encode(bytebuffer)
print(audio_base64_encoding)

# data = { "key" : "927f7543-ec5a-4370-b256-92cec0d021a2", "serviceId" : "01694219846", "argument" : {"audioData" : audio_base64_encoding } }
# URL = 'http://svc.saltlux.ai:31781'
# response = requests.post(URL, data=data)
# print(json.loads(response.text))