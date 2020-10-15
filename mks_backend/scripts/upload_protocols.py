import random
import string
from os import remove

import requests
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader


def main():
    for _ in range(15):
        random_clue = f'{random.randint(100, 500)}{random.choice(string.ascii_uppercase)}'
        file = random.choice(['Протокол.odt', 'Протокол.pdf'])

        # царь костылей On
        new_filename = file.split('.')[0] + random_clue + '.' + file.split('.')[1]
        new_file = f'/home/atimchenko/protocols_files/{new_filename}'
        # царь костылей Off

        if file == 'Протокол.odt':
            with open(new_file, 'w') as output_file:
                output_file.write(f'Текст протокола {new_filename}')
        elif file == 'Протокол.pdf':
            canvas = Canvas(new_file)
            logo = ImageReader('/home/atimchenko/Изображения/aorti_logo.png')

            canvas.drawImage(logo, 165, 760, mask='auto')
            canvas.drawString(250, 700, f'Text of {random_clue}')
            canvas.save()

        id_file = send_file(new_filename)
        create_protocol(id_file, new_filename.split('.')[0])

        remove(new_file)


def send_file(file_name: str):
    url = 'http://0.0.0.0:6543/protocol/upload'
    files = {'protocolFile': open(f'/home/atimchenko/protocols_files/{file_name}','rb')}
    response = requests.post(url, files=files)

    print(response.text)
    id_filestorage = response.json()['idFileStorage']
    return id_filestorage


def create_protocol(id_filestorage, protocol):
    url = 'http://0.0.0.0:6543/protocol'

    data = {
        'idFileStorage': id_filestorage,
        'meeting': random.randint(1, 6),
        'note': f'Заметка о протоколе {protocol}',
        'protocolName': f'{protocol}',
        'protocolNumber': str(random.randint(10, 110)),
        'protocolDate': f'Thu Oct 0{random.randint(1, 9)} 2020',
    }
    response = requests.post(url, json=data)


if __name__ == '__main__':
    main()
