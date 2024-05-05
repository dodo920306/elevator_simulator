from django.db import models
from django.contrib.postgres.fields import ArrayField
from time import sleep

# Create your models here.
def get_default_levels():
    return [False] * 10

class Elevator(models.Model):
    current_floor = models.IntegerField(default=0)
    status = models.IntegerField(default=1)
    levels = ArrayField(
            models.BooleanField(default=False),
            size=10,
            default=get_default_levels
        )
    park = models.BooleanField(default=False)

    def move(self, floor: int):
        if floor > self.current_floor:
            self.status = 2
            self.save()
            sleep(1)
            while floor > self.current_floor:
                self.current_floor += 1
                self.save()
                sleep(1)
        elif floor < self.current_floor:
            self.status = 3
            self.save()
            sleep(1)
            while floor < self.current_floor:
                self.current_floor -= 1
                self.save()
                sleep(1)
        self.status = 1
        self.save()
