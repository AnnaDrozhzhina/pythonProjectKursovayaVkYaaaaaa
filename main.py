import vk
import ya_disk

from _token import access_token
from _token import owner_id
from _token import ya_token


if __name__ == '__main__':
    vk_ = vk.vk(access_token, owner_id)
    ya = ya_disk.ya_disk(token=ya_token, count_photos=5)
    ya._create_folder()
    response = vk_.get_photos_info()
    if response:
        ya.info_loading(response)
