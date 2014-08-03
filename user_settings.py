## User Settings
## Modifiy values below to get friends images
## fb_uif             : Your user id on facebook
## fb_access_token    : Access token to FB Graph API to Download images
##                        to local images folder
## Refer              : Goto https://developers.facebook.com/tools/explorer/145634995501895
##                      accept permissions and get your access token ans facebook id to 
##                      the below fields
## images_folder_path : To Download images from FB to stitch
## agent              : User agent to mimic a browser request to FB
##                      to get images without hassels

import os
PATH = lambda root, *a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))
IMAGES_ROOT = PATH(ROOT, 'images/')

class User:
    def __init__(self):
        self.agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31"
        self.fb_uid = "100002134446846"
        self.fb_access_token = "CAACEdEose0cBAN1i6CkiZBNtCVxgSmAhmT0TlEQZCIbrnahrfSwxR2xOUwa0zoRmrepQjSLL22ZA9iz7gzD6E3HDxtwqt3H8nEOF3dF0AW62vGCfJZANnTtN8lCd2jW0caBlDjZADOuvIhi73DufKPaPNWeBaKnJY71PZA361MgLQ3gKg0gngCqqb95dJ2bBJdhYfC0JPoswZDZD"
        self.images_folder_path=IMAGES_ROOT
