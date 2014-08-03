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
        ## To be adjusted by user
        self.fb_uid = "YOUR_FB_ID"
        self.fb_access_token = "YOUR_FB_ACCESS_TOKEN"
        
        #You need not modify anything below this line.
        self.agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31"
        self.images_folder_path=IMAGES_ROOT
        self.root_folder_path=PATH(ROOT, '')
        
        
