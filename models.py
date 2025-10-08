from django.db import models
from django.contrib.auth.models import User


class AnimalReport(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    ANIMAL_TYPE_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
    ]

    COLOR_CHOICES = [
        ('Brown', 'Brown'),
        ('White', 'White'),
        ('Black', 'Black'),
        ('Grey', 'Grey'),
        ('Orange', 'Orange'),
        ('BlackWhite', 'BlackWhite'),
        ('BrownWhite', 'BrownWhite'),
        ('WhiteOrange', 'WhiteOrange'),
        ('WhiteGrey', 'WhiteGrey'),
        ('BlackGrey', 'BlackGrey'),
    ]

    SIZE_CHOICES = [
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('Big', 'Big'),
    ]

    image = models.ImageField(upload_to='animal_images/')
    report_type = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    has_collartags = models.CharField(max_length=50, choices=[('Yes', 'Yes'), ('No', 'No')])
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    animal_type = models.CharField(max_length=50, choices=ANIMAL_TYPE_CHOICES)
    breed = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=20, blank=True, null=True, choices=SIZE_CHOICES)
    date = models.DateField(blank=True, null=True)
    behavior = models.CharField(max_length=50,blank=True, null=True)
    last_seen_location = models.CharField(max_length=255, blank=True, null=True)
    reporter_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    post_caption = models.CharField(max_length=100, blank=True, null=True)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    recent_events = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.reporter_name  
    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    fname = models.CharField(max_length=100, blank=True, null=True)
    mname = models.CharField(max_length=100, blank=True, null=True)
    lname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100,blank=True, null=True)
    contact_no = models.CharField(max_length=20, blank=True, null=True)

    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Non-Binary', 'Non-Binary'),
        ('Other', 'Other')
    ]
    gender = models.CharField(max_length=30,blank=True, null=True, choices=gender_choices)
    city = models.CharField(max_length=100, blank=True, null=True)
    age = models.CharField(max_length=2, blank=True, null=True)
    bday = models.DateField(max_length=100, blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    numpets = models.CharField(max_length=100, blank=True, null=True)
    tagone = models.CharField(max_length=50, blank=True, null=True)
    tagtwo = models.CharField(max_length=50, blank=True, null=True)
    tagthree = models.CharField(max_length=50, blank=True, null=True)
    caption = models.CharField(max_length=100, blank=True, null=True)
    

    def __str__(self):
        return self.user.username
    


class Event(models.Model):

    month_year = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateField()
    time = models.CharField(max_length=100, blank=False, null=False)
    location = models.CharField(max_length=100, blank=False, null=False)
    details = models.CharField(max_length=500, blank=False, null=False)


    def __str__(self):
        return f"{self.title} {self.date} {self.location}"