import requests
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": "HoNXQkn9s1YhejAclzf0kOxI3KQRfO8VJPu0wT1D",
        "count": 10
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        apod_list = data if isinstance(data, list) else [data]
    except requests.exceptions.HTTPError as http_err:
        return HttpResponse(f'HTTP error occurred: {http_err}', status=500)
    except requests.exceptions.RequestException as req_err:
        return HttpResponse(f'Error occurred: {req_err}', status=500)
    except ValueError as json_err:
        return HttpResponse(f'JSON decode error: {json_err}', status=500)

    return render(request, 'index.html', {'apod_list': apod_list})
