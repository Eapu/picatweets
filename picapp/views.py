from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import tweepy
from tweepy import OAuthHandler
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

 
def index(request):


    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    
    search_tweets = api.search(q="#IncendiosForestales OR #IFF OR #incendioForestal OR #Bosques ", lang="es", count=200, include_rts = True,  tweet_mode = 'extended')
    search_tweets_noRT = api.search(q="#IncendiosForestales OR #IFF OR #incendioForestal OR #Bosques -filter:retweets", lang="es", count=200, include_rts = True,  tweet_mode = 'extended')
    user_metions = api.mentions_timeline(tweet_mode = 'extended') 

    return render(request, 'picapp/index.html', {'search_tweets': search_tweets, 'search_tweets_noRT':search_tweets_noRT,'user_metions':user_metions})


def index2(request):
    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    more_tweets1 = api.search(q="#afforestation OR #deforestation OR #ClimateAction  -filter:retweets", lang="es", count=200, include_rts = True,  tweet_mode = 'extended')
    more_tweets2 = api.search(q="#climatechange OR #biodiversity OR #amenazas OR #deforestación -filter:retweets", lang="es", count=200, include_rts = True,  tweet_mode = 'extended')
    more_tweets3 = api.search(q="#trees OR #IFF OR #forest OR #amenazas OR #woods -filter:retweets", lang="es", count=200, include_rts = True,  tweet_mode = 'extended')

    return render(request, 'picapp/index2.html', {'more_tweets1': more_tweets1, 'more_tweets2':more_tweets2,'more_tweets3':more_tweets3})


