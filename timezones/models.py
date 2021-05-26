from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Timezone(models.Model):
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    gmt_diff = models.FloatField(
        validators=[MinValueValidator(-12), MaxValueValidator(12)]
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"<Timezone: {self.name} @ {self.city} is {self.get_gmt_repr()}>"

    def get_gmt_repr(self):
        sign = "-" if self.gmt_diff < 0 else "+"
        hours, minutes = str(abs(self.gmt_diff)).split(".")
        hours = hours.zfill(2)
        minutes = str(int(float("0." + minutes) * 60))

        if len(minutes) == 1:
            minutes += "0"

        return f"{sign}{hours}:{minutes}"
