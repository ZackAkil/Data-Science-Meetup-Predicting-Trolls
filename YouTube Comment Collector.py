#!/usr/bin/python

# Usage example:
# python comment_threads.py --channelid='<channel_id>' --videoid='<video_id>' --text='<text>'
import urllib
import json
import httplib2
import os
import sys
import csv
import copy

keyFile = open('key.txt', 'r')
apiKey = keyFile.readline()
keyFile.close()

def getComments(id,maxResults):
    comments = []
    url = "https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults="+str(maxResults)+"&videoId="+id+"&key="+apiKey
    response = urllib.urlopen(url)
    data = json.loads(response.read())

    for c in data['items']:
        comment = {
        'text':c['snippet']['topLevelComment']['snippet']['textDisplay'].encode('utf-8'),
        'replies':c['snippet']['totalReplyCount']
        }
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
                # 'favourites': c['statistics']['favoriteCount'].encode('utf-8'),
                'views': c['statistics']['viewCount'].encode('utf-8'),
                'commentCount': c['statistics']['commentCount'].encode('utf-8')
                })
    return vids

vids = getPopularVideos(50)

# for i in ids:
#     getComments(i,100)
commentData = []

for v in vids:
    print(v['title'])
    coms = getComments(v['id'],100)
    for c in coms:
        record = copy.deepcopy(v)
        record['comment'] = c['text']
        record['replies'] = c['replies']
        commentData.append(record)
        print(record)

keys = commentData[0].keys()

with open('utube.csv', 'w') as csvfile:

    writer = csv.DictWriter(csvfile, fieldnames=keys)

    writer.writeheader()

    for c in commentData:
        writer.writerow(c)
    # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    # writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
