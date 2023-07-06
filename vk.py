import requests
# from pprint import pprint

class vk:

   def __init__(self, access_token, owner_id, version='5.131'):
       self.token = access_token
       self.id = owner_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

   def get_photos_info(self):
       url = 'https://api.vk.com/method/photos.get'
       params = {'owner_id': self.id,
                 'album_id': 'wall',
                 'rev': 1,
                 'extended': 1,
                 'photo_sizes': 1}
       photo_inf = requests.get(url, params={**self.params, **params}).json()
       return photo_inf


