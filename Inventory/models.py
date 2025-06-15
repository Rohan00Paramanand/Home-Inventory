from django.db import models

class Item(models.Model):

    ROOMS = [
        ("r_room", "Rohan's Room"),
        ("R_room", "Radhika's Room"),
        ("P_room", "Parents' Room"),
        ("G_room", "Guest Room"),
        ("Rr_bathroom", "R & r Bathroom"),
        ("P_bathroom", "Parents' Bathroom"),
        ("C_bathroom", "Corridor Bathroom"),
        ("G_bathroom", "Guest Bathroom"),
        ("living_room", "Living Room"),
        ("kitchen", "Kitchen"),
    ]

    name = models.CharField(max_length=200)
    spot = models.CharField(max_length=100)
    location = models.CharField(max_length=100, choices=ROOMS)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
