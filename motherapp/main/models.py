from django.db import models
from django.shortcuts import reverse
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your models here.
STATUS_OPTION = (

    ('Old', 'Old'),
    ('New', 'New'),
    ('Interested', 'Not Interested'),
    ('Call Back', 'Call Back'),
    ('Wrong Number', 'Wrong Number'),
    ('Fait le mac', 'Fait le mac'),
    ('Fond dispo', 'Fond dispo'),
    ('NRP', 'NRP'),
    ('NRP 2', 'NRP 2'),
    ('Ancien Interesse', 'Ancien Interesse'),
    ('Client', 'Client'),
    ('Presque Client', 'Presque Client'),
    ('BON Call Back', 'BON Call Back')

)

class Participant(models.Model):
    Full_Name = models.CharField(max_length=200, help_text='Enter your name')
    Email = models.EmailField()
    Phone_No = models.CharField(max_length=20, help_text='Enter your phone number here')
    Status = models.CharField(choices=STATUS_OPTION, max_length=20)
    Created_on = models.DateTimeField(auto_now_add=True)
    identity  = models.SlugField(max_length=10, unique=True)
    Available = models.BooleanField(default=True)
    Profile_img = models.ImageField(upload_to='imagefolder', default="Upload Image", help_text="If image available, please upload")

    def __str__(self):
        return self.Full_Name
    def get_absolute_url(self):
        return reverse('main:detail_view', args=[self.identity])

