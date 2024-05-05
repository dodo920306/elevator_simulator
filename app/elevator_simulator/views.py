from django.http import HttpResponse, JsonResponse
from .models import Elevator


# Create your views here.

def hello(request):
    return HttpResponse("Hello World!")

def status(request):
    try:
        elevator1, _ = Elevator.objects.get_or_create(id=1)
        elevator2, _ = Elevator.objects.get_or_create(id=2)
        response = JsonResponse({"applied": True, "error_msg": "", "floor": [elevator1.current_floor + 1, elevator2.current_floor + 1], "status": [elevator1.status, elevator2.status]})
    except Exception as e:
        response = JsonResponse({"applied": False, "error_msg": repr(e)})
    return response

def up(request):
    try:
        elevator1, _ = Elevator.objects.get_or_create(id=1)
        current = int(request.GET["current"])
        elevator1.move(current)
        response = JsonResponse({"applied": True, "error_msg": ""})
    except Exception as e:
        response = JsonResponse({"applied": False, "error_msg": repr(e)})
    return response

def down(request):
    try:
        elevator2, _ = Elevator.objects.get_or_create(id=2)
        current = int(request.GET["current"])
        elevator2.move(current)
        response = JsonResponse({"applied": True, "error_msg": ""})
    except Exception as e:
        response = JsonResponse({"applied": False, "error_msg": repr(e)})
    return response

def select(request):
    try:
        select = int(request.GET["select"])
        number = int(request.GET["number"])
        if number == 1:
            elevator1, _ = Elevator.objects.get_or_create(id=1)
            elevator1.move(select)
        else:
            elevator2, _ = Elevator.objects.get_or_create(id=2)
            elevator2.move(select)
        response = JsonResponse({"applied": True, "error_msg": ""})
    except Exception as e:
        response = JsonResponse({"applied": False, "error_msg": repr(e)})
    return response
