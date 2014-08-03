fb_frnd_image_stitcher
======================

##A Friendship day Hack

> "Sometime the road through life isn't always a straight line. "
- Daniel Long

A BIG Thank you to all my Friends for being there, It does mean a lot to me. 

This is an Inspired script from [@swvist](https://github.com/swvist)'s [Image stitching script](https://gist.github.com/2692786)

It involves two parts:
###1. FB Frnds Image Extractor
- Gets images from Facebook
###2. Image Stitching script by [@swvist](https://github.com/swvist)

##Execution Instructions:
- Get your access token and fb user id from here : [https://developers.facebook.com/tools/explorer/145634995501895](https://developers.facebook.com/tools/explorer/145634995501895)
- do accept the permission, this a test app from FB for developers,
- Modifiy values in the `user_settings.py` file the script running
- `fb_uif`             : Your user id on facebook
- `fb_access_token`    : Access token to FB Graph API to Download images to local images folder
- Install the Packages below
- **Thats it**. Done. Just run the shell script as `bash base_shell.sh` and give it time...

** If you have any queries or doubts, put it up on issues. Will get back as soon as possible! :)**

Packages used:
1. time
2. urllib, urllib2
3. os, 
4. json
5. re
6. datetime
7. socket
8. Facebook python driver (facebook)
9. python Garbage Collection (gc)
10. random
11. Image

PS: all these packages can be used by installing using pip (recommended)

- Note 1: The Final stitched image will be a square. If the images fall short to fill the square, the rest will be kept Blank
