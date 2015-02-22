import json
from django.http import HttpResponse
from oauth2_provider.models import AccessToken
# Create your views here.


def get(request):
    if "access_token" in request.GET:
        token = request.GET["access_token"]
        u = AccessToken.objects.get(token=token).user
        response_data = {}
        response_data['id'] = u.id
        response_data['username'] = u.username
        response_data['first_name'] = u.first_name
        response_data['last_name'] = u.last_name
        response_data['email'] = u.email

        return HttpResponse(json.dumps(response_data), content_type="application/json")