from . import models
import typing


def get_all_rooms():
    return models.Room.objects.all()


def get_room(pk: typing.Optional[int] = 1):
    try:
        return models.Room.objects.get(pk=pk)
    except models.Room.DoesNotExist:
        return None
