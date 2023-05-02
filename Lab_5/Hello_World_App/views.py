import json
from django.http import HttpResponse


def Index(request):

    msg = {"message": "Hello World!"}

    return HttpResponse(json.dumps(msg), content_type='application/json')

# Create your views here.
