 fb_frnd_image_stitcher
======================

# Broken because of FB's new TOS 

**Only friends who installed this app are returned in API v2.0 and higher. total_count in summary represents the total number of friends, including those who haven't installed the app. [Learn More](https://developers.facebook.com/docs/apps/changelog#v2_0)**

## A Friendship day Hack

> "Sometime the road through life isn't always a straight line. "
- Daniel Long

A BIG Thank you to all my Friends for being there, It does mean a lot to me. 

This is an Inspired script from [@swvist](https://github.com/swvist)'s [Imagegrid generator script](https://gist.github.com/2692786)

It involves two parts:
#### 1. FB Frnds Image Extractor
- Gets images from Facebook

#### 2. Imagegrid generator script by [@swvist](https://github.com/swvist)

#### Prerequisites

- python3
- virtualenv==13.1.2
 
### Execution/Setup Instructions:
1. Get your access token and fb user id from here : [https://developers.facebook.com/tools/explorer/145634995501895](https://developers.facebook.com/tools/explorer/145634995501895)
2. do accept the permission, this a test app from FB for developers,
3. Modifiy values in the `user_settings.py` file the script running
    - `fb_uif`             : Your user id on facebook
    - `fb_access_token`    : Access token to FB Graph API to Download images to local images folder
4. cd to the root of the project folder in the terminal
5. run the command to create a virtualenv for the project: `$ virtualenv venv`
6. run the command to switch to virtualenv:
` $ source venv/bin/activate `
7. install required libraries/packages to the virtualenv using pip as follows:
` $ pip install -r requirements.pip `
8. **Thats it**. Done. Just run the shell script as `bash base_shell.sh` and give it time...

**If you have any queries or doubts, put it up on issues. Will get back as soon as possible! :)**

Packages used:
- time
- urllib, urllib2
- os, 
- json
- re
- datetime
- socket
- python Garbage Collection (gc)
- random
- Image

PS: all these packages can be used by installing using pip using `requirements.pip ` (recommended)


- **Note 1**    : The Final stitched Imagegrid generated will be a square. If the images fall short to fill the square, the rest will be kept Blank
- **Note 2**    : Am working on a Completion script to fill in blanks
