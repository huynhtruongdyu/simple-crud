from django.db import models

# Create your models here.


class Device(models.Model):
    choices = (
        ('AVAILIBLE', 'Ready to be purchased'),
        ('SOLD', 'Sold'),
        ('RESTOCKING', 'Restocking in few days'),
    )

    type = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()
    status = models.CharField(max_length=10, choices=choices, default='SOLD')
    issues = models.CharField(max_length=100, default='No issues')

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type: {}, Price: {}'.format(self.type, self.price)


class Laptop(Device):
    pass


class Desktop(Device):
    pass


class Mobile(Device):
    pass
