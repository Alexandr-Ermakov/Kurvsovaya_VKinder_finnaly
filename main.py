import sys
import os
sys.path.append(os.path.abspath('./user_data'))
sys.path.append(os.path.abspath('./dbase'))
sys.path.append(os.path.abspath('./vk'))
from vk.vk_api import VkApi
from vk.get_token import get_token_link

if __name__ == "__main__":
    print('-'*20)
    token_link = get_token_link()
    print(token_link)
    print('-'*20)

    result = VkApi(
        '528de295b4f20d6797301d4dcc151d6d23a67500c4a29a1f48d762406ad12c7ef3e35f6e815c09ab4ff2e')

    result.app()