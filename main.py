import vk
import ya_disk

from _token import access_token
from _token import user_id
from _token import TOKEN


if __name__ == '__main__':
    vk_ = vk.vk(access_token, user_id)
    ya = ya_disk.ya_disk(token=TOKEN, count_photos=5)
    ya._create_folder()
    response = vk_.get_photos_info()
    if response:
        ya.info_loading(response)
