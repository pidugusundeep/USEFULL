import pafy   
import requests
import sys
import os
from pprint import pprint
import datetime


URL = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults="+sys.argv[2]+"&q="+sys.argv[1]+"&videoLicense=creativeCommon&type=video&key=APIKEY"

r = requests.get(url = URL) 
  
data = r.json() 

if(len(data['items']) > 0):
    directory  = str(datetime.datetime.now()).split(" ")[0]+"__"+sys.argv[2]+"__"+sys.argv[1]
    if not os.path.exists(directory):
        os.makedirs(directory)

    for eachItem in data['items']:
        pprint(eachItem['id']['videoId'] + "   <::>   " +eachItem['snippet']['title'])
        url = "https://www.youtube.com/watch?v="+eachItem['id']['videoId']
        video = pafy.new(url) 
        best = video.getbest() 
        print(best.resolution, best.extension) 
        best.download(filepath=directory+"/")
