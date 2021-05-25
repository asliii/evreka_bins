from django.http import JsonResponse
from base.models import *


def get_collection_frequencies(request):
    response = dict()
    try:
        response['data'] = list(BinOperation.objects.values('bin__name', 'operation__name', 'collection_frequency'))
    except Exception as e:
        response['status'] = False
        response['error'] = str(e)
    return JsonResponse(response, safe=False)