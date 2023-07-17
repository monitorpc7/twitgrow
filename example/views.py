# example/views.py
from datetime import datetime
import json

from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from hugchat import hugchat
from hugchat.login import Login
from bardapi import Bard


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
    token = 'Yggwf6og3zgFs6pESPR-y413Vt_fqk8kPwZmSqf72VQOf2ZfHk5gLXdPBxinDfQ5qAQ6RQ.'
    bard = Bard(token=token)
    
    topic = request.data['topic']
    tone = request.data['tone']
    print(topic+"-"+tone)
    topic = '''
    {}
    '''.format(topic)

    prompt ="I want you to act as an expert social media marketer and a expert copywriter.you have a goal on growing your audience. with that, generate a engaging and more human like maximum 200-word tweet with emoji and indentations on each line for the following topic present after 'Topic :' for the tone " +tone+'''. 
            For easy processing and consistency, format your response as a JSON object with key "tweet" which has to have the generated 
        tweet on the given topic and in that json also include a key called "tone" that has the tone of that generated tweet. the format of the json 
        response should the one present after "Format :".

            Format: 
            {
            'tweet': [tweet],
            'tone':[tone of the tweet]
            }    
        

            Topic : '''+topic
    result = bard.get_answer(prompt)['content']

    try:
        reply = json.loads(result)
        reply =reply['tweet']
    except Exception as e:
        try:
            firstValue = result.index("{")
            lastValue = len(result) - \
                result[::-1].index("}")
            jsonString = result[firstValue:lastValue]

            reply = json.loads(jsonString)
            reply =reply['tweet']
        except Exception as e:
            
            reply = result
    try:
        reply = json.loads(reply)
        result =reply['tweet']
    except Exception as e:
        result = reply

    print(result)

    return Response({"tweet":str(result)})

@api_view(['POST', 'GET'])
def thread_gen(request):
    token = 'Yggwf6og3zgFs6pESPR-y413Vt_fqk8kPwZmSqf72VQOf2ZfHk5gLXdPBxinDfQ5qAQ6RQ.'
    bard = Bard(token=token)
    
    topic = request.data['topic']
    tone = request.data['tone']
    print(topic+"-"+tone)
    topic = '''
    {}
    '''.format(topic)

    initial = '''
    I want you to act like an experienced social media expert with the ability to
        write highly captivating Twitter threads that people would love reading furthur. I want you to help me write a Twitter
        long thread with more content about this topic: {} . 
    '''.format(topic)


    prompt = initial+'''. 
        
        For easy processing and consistency, format your response as a JSON object with key "thread" which has to have the generated 
        tweet on the given topic.   

        the format of the json response should the one present after "Format :".

                Format: 
                {
                'thread': [thread],
                'tone':[tone of the tweet]
                }           


            '''
    result = bard.get_answer(prompt)['content']

    try:
        reply = json.loads(result)
        reply =reply['thread']
    except Exception as e:
        try:
            firstValue = result.index("{")
            lastValue = len(result) - \
                result[::-1].index("}")
            jsonString = result[firstValue:lastValue]

            reply = json.loads(jsonString)
            reply =reply['thread']
        except Exception as e:
            
            reply = result
    try:
        reply = json.loads(reply)
        result =reply['thread']
    except Exception as e:
        result = reply

    print(result)

    return Response({"thread":str(result)})

@api_view(['POST', 'GET'])
def reply_gen(request):
    token = 'Yggwf6og3zgFs6pESPR-y413Vt_fqk8kPwZmSqf72VQOf2ZfHk5gLXdPBxinDfQ5qAQ6RQ.'
    bard = Bard(token=token)    
    
    tweet = request.data['tweet']
    tone = request.data['tone']

    print(tweet)
    print(tone)
    
    tweet = '''
    {}
    '''.format(tweet)

    prompt  = '''I want you to act as an expert social media marketer and a expert copywriter.you have a goal on growing your audience. with that, generate a {} and more human like 30-word reply  with emoji to express emotions if possible  for the following tweet present after "Tweet :". 
    For easy processing and consistency, format your response as a JSON object with "reply" and the content of each as the keys has to be the reply.

    Tweet : {}
    '''.format(tone,tweet)
    result = bard.get_answer(prompt)['content']
    #print(result)
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
    token = 'Yggwf6og3zgFs6pESPR-y413Vt_fqk8kPwZmSqf72VQOf2ZfHk5gLXdPBxinDfQ5qAQ6RQ.'
    bard = Bard(token=token)    
    
    tweet = request.data['tweet']
    tone = request.data['tone']

    print(tweet)
    print(tone)
    
    tweet = '''
    {}
    '''.format(tweet)

    prompt  = '''I want you to act as an expert social media marketer and a expert copywriter.you have a goal on growing your audience. with that, generate a {} and more human like 30-word quoted retweet reply with emoji to express emotions if possible  for the following tweet present after "Tweet :". 
    For easy processing and consistency, format your response as a JSON object with "reply" and the content of each as the keys has to be the reply.

    Tweet : {}
    '''.format(tone,tweet)
    result = bard.get_answer(prompt)['content']
    #print(result)
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
def tweet_rewrite(request):   
    token = 'Yggwf6og3zgFs6pESPR-y413Vt_fqk8kPwZmSqf72VQOf2ZfHk5gLXdPBxinDfQ5qAQ6RQ.'
    bard = Bard(token=token)
    
    tweet = request.data['tweet']    
    print(tweet)    
    
    tweet = '''
    {}
    '''.format(tweet)

    # Create a ChatBot
    prompt='''I want you to act as an expert social media marketer and a expert copywriter.you have a goal on growing your audience. with that, rewrite with the engaging indentations for the following tweet present after "Tweet :". 
    For easy processing and consistency, format your response as a JSON object with key "tweet" which has to have the rewritten version 
    of the given tweet and in that json also include a key called "tone" that has the tone of this tweet. the format of the json 
    response should the one present after "Format :".

        Format: 
        {
        'tweet': [rewritten tweet],
        'tone':[tone of the tweet]
        }    

        Tweet :'''+tweet

    result = bard.get_answer(prompt)['content']
    print(result)
    try:
        reply = json.loads(result)
        reply =reply['tweet']
    except Exception as e:
        try:
            firstValue = result.index("{")
            lastValue = len(result) - \
                result[::-1].index("}")
            jsonString = result[firstValue:lastValue]

            reply = json.loads(jsonString)
            reply =reply['tweet']
        except Exception as e:
            
            reply = result
    try:
        reply = json.loads(reply)
        result =reply['tweet']
    except Exception as e:
        result = reply

    print(result)

    return Response({"tweet":str(result)})

@api_view(['POST', 'GET'])
def topic_suggestion(request):   
    token = 'Yggwf6og3zgFs6pESPR-y413Vt_fqk8kPwZmSqf72VQOf2ZfHk5gLXdPBxinDfQ5qAQ6RQ.'
    bard = Bard(token=token)
    
    niche = request.data['niche']    
    print(niche)    
    
    niche = '''
    {}
    '''.format(niche)

    # Create a ChatBot
    prompt='''I want you to act as an expert social media marketer and a expert copywriter.you have a goal on growing your audience. 
    with that in mind, give me 10 trending and more engaging topics to post on twitter for the following niche present after "Niche :". 
    For easy processing and consistency, format your response as a JSON object with key "topics_list" which has to have the topics list
    of the given niche .for each time giveme different topics instead of previous ones. the format of the json response should the one present after "Format :".

        Format: 
        {
        'topics_list': [topics_list]        
        }    

        Niche :'''+niche

    result = bard.get_answer(prompt)['content']
    #print(result)
    try:
        reply = json.loads(result)
        reply =reply['topics_list']
    except Exception as e:
        try:
            firstValue = result.index("{")
            lastValue = len(result) - \
                result[::-1].index("}")
            jsonString = result[firstValue:lastValue]

            reply = json.loads(jsonString)
            reply =reply['topics_list']
        except Exception as e:
            
            reply = result
    try:
        reply = json.loads(reply)
        result =reply['topics_list']
    except Exception as e:
        result = reply

    try:
        topics_list = ""
        for element in list(result):
            topics_list += str(element) + "\n"
    except Exception as e:
        topics_list = result


    print(topics_list)

    return Response({"topics_list":str(topics_list)})
