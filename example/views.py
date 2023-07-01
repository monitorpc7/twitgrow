# example/views.py
from datetime import datetime

from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

# def index(request):
#     now = datetime.now()
#     html = f'''
#     <html>
#         <body>
#             <h1>Hello from Vercel!</h1>
#             <p>The current modified time is { now }.</p>
#         </body>
#     </html>
#     '''
#     return HttpResponse(html)

@api_view(['POST', 'GET'])
def index(request):
    now = datetime.now()  
    return Response({"time":str(now)})