#!/usr/bin/python

# Usage example:
# python comment_threads.py --channelid='<channel_id>' --videoid='<video_id>' --text='<text>'
import urllib
import json
import httplib2
import os
import sys
import csv

keyFile = open('key.txt', 'r')
apiKey = keyFile.readline()
keyFile.close()

def getComments(id,maxResults):
    comments = []
    url = "https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults="+str(maxResults)+"&videoId="+id+"&key="+apiKey
    response = urllib.urlopen(url)
    data = json.loads(response.read())

    for c in data['items']:
        comment = c['snippet']['topLevelComment']['snippet']['textDisplay'].encode('utf-8')
        # print(comment)
        comments.append(comment)
    return comments

def getPopularVideos(maxResults):
    vids = []
    url = "https://www.googleapis.com/youtube/v3/videos?part=snippet%2C+statistics&maxResults="+str(maxResults)+"&chart=mostPopular&regionCode=GB&key="+apiKey
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    for c in data['items']:
        # print(c)
        if('commentCount' in c['statistics']):
            vids.append({
                'id': c['id'].encode('utf-8'),
                'title': c['snippet']['title'].encode('utf-8'),
                'likes': c['statistics']['likeCount'].encode('utf-8'),
                'dislikes': c['statistics']['dislikeCount'].encode('utf-8'),
                'favourites': c['statistics']['favoriteCount'].encode('utf-8'),
                'views': c['statistics']['viewCount'].encode('utf-8'),
                'comments': c['statistics']['commentCount'].encode('utf-8')
                })
    return vids

vids = getPopularVideos(5)

# for i in ids:
#     getComments(i,100)

for v in vids:
    print(v['title'])

keys = vids[0].keys()

with open('utube.csv', 'w') as csvfile:

    writer = csv.DictWriter(csvfile, fieldnames=keys)

    writer.writeheader()

    for v in vids:
        writer.writerow(v)
    # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    # writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
