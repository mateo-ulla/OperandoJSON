import requests, json, random
from datetime import datetime

numposts = input('Ingrese el numero de Posts a crear, entre 1 y 1000: ')

if not numposts.isdigit() or int(numposts) < 1 or int(numposts) > 1000:
    numposts = input('Ingrese el NUMERO de Posts a crear: ')

numposts = int(numposts)

for i in range(1, numposts + 1):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{i}')
    if response.status_code == 200:
        data = response.json()
        now = datetime.now()
        data["fecha"] = now.strftime("%d/%m/%Y %H:%M:%S")
        url_img = f'https://picsum.photos/id/{random.randint(0,1000)}/1366/768'
        data["img"] = url_img
        json_string = json.dumps(data)
        with open(f'Post{i}.json', 'w') as file:
            file.write(json_string)
        print(data)