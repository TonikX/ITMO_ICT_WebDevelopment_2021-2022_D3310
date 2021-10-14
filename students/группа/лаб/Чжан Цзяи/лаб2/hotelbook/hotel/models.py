from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Hotel(models.Model):
    name_hotel = models.CharField(max_length=50)
    owner_hotel = models.CharField(max_length=50)
    add_hotel = models.CharField(max_length=100)
    des_hotel = models.CharField(max_length=600)

    def __str__(self):
        return "{}, {}, {}, {}".format(self.name_hotel, self.owner_hotel, self.add_hotel, self.des_hotel)


class Room(models.Model):
    TYPES = [
        ('1', '1 человек'),
        ('2', '2 человека'),
        ('3', '3 человека'),
        ('4', '4 человека')
    ]
    type_room = models.CharField(max_length=1, choices=TYPES)
    price_room = models.FloatField()
    cap_room = models.FloatField()
    fac_room = models.CharField(max_length=200)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    order_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}, {}, {}, {}".format(self.price_room, self.cap_room, self.fac_room, self.get_type_room_display())


class Comment(models.Model):
    POINT = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )
    text_comment = models.CharField(max_length=1600)
    point = models.CharField(max_length=2, choices=POINT)
    b_date = models.DateField()
    e_date = models.DateField()
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
