# example/urls.py
from django.urls import path

from example import views


urlpatterns = [
    path('', views.index),
    path('tweet-gen/', views.tweet_gen),
    path('thread/', views.thread_gen),
    path('reply/', views.reply_gen),
    path('quote/', views.quoted_retweet_gen),
    path('rewrite/', views.tweet_rewrite),
]