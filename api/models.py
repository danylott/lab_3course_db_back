from django.db import models


class Passenger(models.Model):
    full_name = models.CharField(max_length=45, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    passport = models.CharField(max_length=45, null=False, blank=False)
    min_comfort = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.full_name} {str(self.age)} {self.passport}"


class Train(models.Model):
    name = models.CharField(max_length=45, null=False, blank=False)
    power = models.IntegerField(null=False, blank=False)
    passengers = models.ManyToManyField(Passenger, through="Trip")

    def __str__(self):
        return f"{self.name} {self.power}"


class Trip(models.Model):
    train_id = models.ForeignKey(Train, on_delete=models.DO_NOTHING, null=False, blank=False)
    passenger_id = models.ForeignKey(Passenger, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateTimeField(null=False, blank=False)


class Carriage(models.Model):
    name = models.CharField(max_length=45, null=False, blank=False)
    power = models.IntegerField(null=False, blank=False)
    weight = models.IntegerField(null=False, blank=False)
    height = models.IntegerField(null=False, blank=False)
    maxPassengers = models.IntegerField(null=False, blank=False)
    maxLuggage = models.IntegerField(null=False, blank=False)
    comfort = models.IntegerField(null=False, blank=False)
    type = models.CharField(max_length=45, null=False, blank=False)
    train_id = models.ForeignKey(Train, on_delete=models.DO_NOTHING, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"


class Luggage(models.Model):
    width = models.IntegerField(null=False, blank=False)
    weight = models.IntegerField(null=False, blank=False)
    height = models.IntegerField(null=False, blank=False)
    length = models.IntegerField(null=False, blank=False)
    passenger_id = models.ForeignKey(Passenger, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f"{self.width}x{self.height}x{self.height}"
