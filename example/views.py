# example/views.py
from datetime import datetime

from django.http import HttpResponse

from rest_framework.response import Response

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

def index(request):
    now = datetime.now()  
    return Response({"time":str(now)})