#!/usr/bin/python

# Usage example:
# python comment_threads.py --channelid='<channel_id>' --videoid='<video_id>' --text='<text>'
import urllib
import json
import httplib2
import os
import sys

apiKey = ""

def getComments(id,maxResults):
    comments = []
    url = "https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults="+str(maxResults)+"&videoId="+id+"&key="+apiKey
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    if ('error' not in data):
        for c in data['items']:
            comment = c['snippet']['topLevelComment']['snippet']['textDisplay'].encode('utf-8')
            print(comment)
            comments.append(comment)
    return comments

def getPopularVideos(maxResults):
    ids = []
    url = "https://www.googleapis.com/youtube/v3/videos?part=snippet%2C+statistics&maxResults="+str(maxResults)+"&chart=mostPopular&regionCode=IN&key="+apiKey
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    for c in data['items']:
        print(c)
        ids.append(c['id'].encode('utf-8'))
    return ids


ids = getPopularVideos(5)
for i in ids:
    getComments(i,100)
