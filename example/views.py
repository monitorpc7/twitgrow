# example/views.py
from datetime import datetime
import json

from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from hugchat import hugchat
from hugchat.login import Login

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current modified time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

email = 'vvsimkrxropxmhs@karenkey.com'
passwd = 'Passw0rd!'

@api_view(['POST', 'GET'])
def tweet_gen(request):
    sign = Login(email, passwd)
    cookies = sign.login()
    
    tweet = request.POST.get('tweet')
    tone = request.POST.get('tone')

    tweet = '''
    {}
    '''.format(tweet)

    # Create a ChatBot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"
    result = chatbot.chat('''generate a {} and more human like 20-word reply for the following tweet present after "Tweet :". reply has to be in the  format given below without any additional text.
        Reply Format :
        reply: [reply]   

        Tweet : {}
    '''.format(tone,tweet))
    print(result)

    return Response({"reply":str(result)})

@api_view(['POST', 'GET'])
def thread_gen(request):
    now = datetime.now()  
    return Response({"time":str(now)})

@api_view(['POST', 'GET'])
def reply_gen(request):
    sign = Login(email, passwd)
    cookies = sign.login()
    
    tweet = request.data['tweet']
    tone = request.data['tone']
    print(tweet)
    print(tone)
    
    tweet = '''
    {}
    '''.format(tweet)

    # Create a ChatBot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"
    result = chatbot.chat('''generate a {} and more human like 20-word reply with emoji to express emotions if possible  for the following tweet present after "Tweet :". 
    For easy processing and consistency, format your response as a JSON object with "reply" and the content of each as the keys has to be the reply.
   
           

        Tweet : {}
    '''.format(tone,tweet))

    try:
        reply = json.loads(result)
        reply =reply['reply']
    except Exception as e:
        try:
            firstValue = result.index("{")
            lastValue = len(result) - \
                result[::-1].index("}")
            jsonString = result[firstValue:lastValue]

            reply = json.loads(jsonString)
            reply =reply['reply']
        except Exception as e:
            
            reply = result
    try:
        reply = json.loads(reply)
        result =reply['reply']
    except Exception as e:
        result = reply
    
    print(result)

    return Response({"reply":str(result)})

@api_view(['POST', 'GET'])
def quoted_retweet_gen(request):
    now = datetime.now()  
    return Response({"time":str(now)})

@api_view(['POST', 'GET'])
def tweet_rewrite(request):
    now = datetime.now()  
    return Response({"time":str(now)})

