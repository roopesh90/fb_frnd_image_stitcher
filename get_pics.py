# FB Frnds Image 
#Copyright (c) Dr.DmC <roopesh90nair@gmail.com>, Roopesh Nair

#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in
#the Software without restriction, including without limitation the rights to
#use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
#of the Software, and to permit persons to whom the Software is furnished to do
#so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

# Change the values according to your requirement
# Get images from Facebook
# Get access token from here
# https://developers.facebook.com/tools/explorer/?method=GET&path=me/friends
# do accept the permission, this a test app from FB fro developers,
# if you do not approve, get in touch @ roopesh90nair@live.com

import time
import urllib
import urllib2, os
import json
import re
import datetime
import socket
from urlparse import urlparse
from user_settings import User
import facebook
import gc


def get_url_data(url, params):
	try:
		opener = urllib2.build_opener()
		opener.addheaders.append(('User-Agent', user_agent))
		
		default_timeout = 5
		socket.setdefaulttimeout(default_timeout)
		
		#print params
		
		f = opener.open(url, params, timeout=default_timeout)
		
		response = f
		data= response.read()
		response.close()
		data = json.loads(data.decode('utf8'))
		
		#print data
	except ValueError:
		data = data.decode('utf8')
	except urllib2.HTTPError, e:
		data =  {'error': "Oops, timed out? HTTPError :"+str(e)}
	except urllib2.URLError, e:
		data =  {'error': "Oops, timed out? URLError :"+str(e)}
	except socket.timeout:
		data = {'error': "Timed out! socket.timeout after "+ default_timeout + "seconds\n" +str(e)}
	except Exception, e:
		data = {'error':"Something strange while html parse... @ \n"+url+"\n Error = "+str(e)}
		#error_log.append( str(jabber)+"\n Something strange while html parse... @ "+"\n"+url+"\n"+str(e)+"\n")
	finally:
		return data
	

def get_FB_frn_list( uid, method, format1, suppress_http_code, access_token, paging, url):
	jabber = 0
	domain = ""
	data = {"error":"Error"}
	try:
		if paging == False:
			url = "https://graph.facebook.com/"+uid+"/friends"
			params = urllib.urlencode({'method': method, 'format': format1, 'suppress_http_code': suppress_http_code, 'access_token': access_token, "fields":"id,name" })
		else:
			params = None
			url = url + "&method=" + method + "&suppress_http_code=" + suppress_http_code + "&access_token=" + access_token
		data = get_url_data(url, params)
		
		#print data
		
	except Exception, e:
		data = {'error':"Something strange while html parse... @ \n"+url+"\n Error = "+str(e)}
		#error_log.append( str(jabber)+"\n Something strange while html parse... @ "+"\n"+url+"\n"+str(e)+"\n")
	finally:
		return data
	
	
def get_FB_frn_img(uid, img_width,img_height):
	##sample url  = graph.facebook.com/500912531/picture?width=50&height=50
	
	img_url = "http://graph.facebook.com/"+uid+"/picture?width="+img_width+"&height="+ img_height
	urllib.urlretrieve(img_url, "images/"+uid+".jpg")


User = User()
user_agent = User.agent
uid = User.fb_uid
access_token = User.fb_access_token

content = "friends"
method = "GET"
format1 = "json"
suppress_http_code = "1"

url = "https://graph.facebook.com/"
url = url + uid + "/" + content
paging = False
continue_2_page = True

print("\n** Developer note: Is auto-garbage collection enabled? => " + str(gc.isenabled()))
if gc.isenabled() == False:
	gc.enable()
	print("** Developer note: Auto-garbage collection has been eneabled? =>" + str(gc.isenabled()))
	print("\n")
	
print("\n## \n## FB Frnds Image Stitcher\n## \n## Copyright (c) @roopesh90 <roopesh90nair@gmail.com>, Roopesh Nair\n##")
print("\n\n\t Fetching friends data from FB\n\t This might take a while\n\n\t Depending on the number \n\t of friends you have and \n\t your internet speed.")

while continue_2_page:
	data = get_FB_frn_list( uid, method, format1, suppress_http_code, access_token, paging, url)

	if data.has_key("error"):
		print data['error']
		exit()
	else:
		
		print("\n\n\tData recieved of "+str(len(data['data']))+" friends")
		if len(data['data']) > 0:
			
			print("\n\t Starting Image aquisition.......")
			for j in xrange(0, len(data['data'])):
				get_FB_frn_img(data['data'][j]['id'], "100", "100")
				print("\n" + str(j) + " Image of " + data['data'][j]['name'].encode('utf-8') + " :id = " + data['data'][j]['id'].encode('utf-8') )
			
			if data.has_key("paging"):
				if data["paging"].has_key("next"):
					print("\n\tGoing to next page => " + data['paging']['next'])
					paging = True
					url = data['paging']['next']
				else:
					continue_2_page = False
			else:
				continue_2_page = False
		else:
			print("\n\n\t No data recieved.......")
			continue_2_page = False
	

print("\n\n Finishing script")
print("\n** Developer note:  => Garbage collector : unreachable items => "+ str(gc.collect()))
hostname = os.popen("hostname").read()
if hostname == "":
	hostname = "the system\n"
print("** These will be removed by the OS automatically later \n** or when " + hostname + "** is switched off")
print(" \n Thank you")
print("\n\n Starting ImageStitcher script by @swvist")
