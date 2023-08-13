from django.http import HttpResponse


def see_all_rooms(request):
    return HttpResponse("All rooms!")


def see_one_rooms(request, room_id):
    return HttpResponse(f"Room #{room_id}")
