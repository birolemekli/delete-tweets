
# -*- coding: utf-8 -*-

import tweepy

CONSUMER_KEY= "****"
CONSUMER_SECRET="****"
ACCESS_TOKEN="****"
ACCESS_TOKEN_SECRET="****"

#%% Api connection

def auth_login(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

#%%
def getPost(api,username):
    for status in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode="extended").items():
        post.append(status)

#%%
def deletePost(year):
    for i in range(len(app)):
        if app[i].created_at.year<year:
            api.destroy_status(id=app[i].id)
            
#%%
if __name__=="__main__":
    post=[]
    username="@username"
    year=1
    api=auth_login(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    getPost(api,username)
    deletePost(year)
    
    

