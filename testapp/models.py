import uuid

from django.db import models


class Filler(models.Model):
    thing_one = models.UUIDField(default=uuid.uuid4)
    thing_two = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return "{}/{}".format(self.thing_one, self.thing_two)
