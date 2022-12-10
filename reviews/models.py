from django.db import models
from common.models import CommonModel


class Review(CommonModel):

    """Review from a User to a Room or Experience"""

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey(
        "rooms.Room", blank=True, null=True, on_delete=models.CASCADE
    )
    experience = models.ForeignKey(
        "experiences.Experience", blank=True, null=True, on_delete=models.CASCADE
    )
    payload = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user} / {self.rating}"
