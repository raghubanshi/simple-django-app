from django.http import JsonResponse

def get_message(request):
    return JsonResponse({"message": "Hello from Django!"})

def get_data(request):
    data = {
        "name": "Praveen Raghubanshi",
        "age": 25,
        "city": "St. Louis"
    }
    return JsonResponse(data)
