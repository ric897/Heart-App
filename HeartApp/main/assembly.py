import requests













def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

def handle(file):
    headers = {'authorization': "e72231891f984135a0e02e75d0265e09"}
    response = requests.post('https://api.assemblyai.com/v2/upload',
                            headers=headers,
                            data=read_file(file))

    url = response.json()['upload_url']
    
    endpoint = "https://api.assemblyai.com/v2/transcript"
    json = { "audio_url": str(url) }
    headers = {
        "authorization": "e72231891f984135a0e02e75d0265e09",
        "content-type": "application/json"
    }
    response = requests.post(endpoint, json=json, headers=headers)
    print(response.json())


