import json

import requests
from progress.bar import FillingSquaresBar

class ya_disk:
    def __init__(self, token, count_photos):
        self.token = token
        self.count_photos = count_photos
        self.headers = {
                'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'
            }
        self.ya_folder = "VK YA photos new folder!!!"

    def _create_folder(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': self.ya_folder}
        response = requests.put(url=url, headers=self.headers, params=params)
        if response.status_code == 201:
            print('Success!')

    def from_url_upload(self, file_name, url_vk):
        self._create_folder()
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        file_path = self.ya_folder + '/' + file_name
        params = {"url": url_vk, "path": file_path}
        response = requests.post(url=url, headers=self.headers, params=params)
        return response

    def create_json(self, photo_info):
        with open('photo_info.json', 'w') as f:
            json.dump(photo_info, f, ensure_ascii=False, indent=2)

    def info_loading(self, response):
        cnt_photos = 0
        files_names = []
        total_info = []
        new_result = []
        size_dict = {'s': 1, 'm': 2, 'o': 3, 'p': 4, 'q': 5, 'r': 6, 'x': 7, 'y': 8, 'z': 9, 'w': 10}
        bar = FillingSquaresBar('Processing...', max=5)
        for element in response['response']['items']:
            size = max(element['sizes'], key=lambda x: size_dict[x["type"]])
            number_of_likes = element['likes']['count']
            date_of_load = element['date']
            new_result.append({'likes': number_of_likes,
                               'name': date_of_load,
                               'size': size})
        for i in new_result:
            if cnt_photos < self.count_photos:
                 info = {'file_name': f"{i['likes']}.jpg",
                            'size': f'{i["size"]}'}
                 file_name = f"{i['likes']}.jpg"
                 if file_name not in files_names:
                     files_names.append(file_name)
                     total_info.append(info)
                     self.from_url_upload(file_name,  f"{i['size']['url']}")
                     cnt_photos += 1
                     bar.next()
                 else:
                     info = {'file_name': f"{i['likes']}_{i['name']}.jpg",
                                'size': f'{i["size"]}'}
                     file_name = f"{i['likes']}_{i['name']}.jpg"
                     files_names.append(file_name)
                     total_info.append(info)
                     self.from_url_upload(file_name,  f"{i['size']['url']}")
                     cnt_photos += 1
                     bar.next()
        bar.finish()
        print('Uploaded files:')
        for el in files_names:
            print(el)
        self.create_json(total_info)







