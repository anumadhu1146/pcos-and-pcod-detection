from django.db import models
from django.contrib.auth.models import User
from PIL import Image



# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

    
class UserImageModel(models.Model):
    image = models.ImageField(upload_to = 'images/',blank=True)
    label = models.CharField(max_length=20,default='data')
    def __str__(self):
        return str(self.image)
    
from django.db import models

class HealthAssessment(models.Model):
    PCOS = models.CharField(max_length=3)  # 'Y' or 'N'
    Age = models.IntegerField()
    Weight = models.FloatField()  # Use FloatField for decimal values
    Height = models.FloatField()  # Use FloatField for decimal values
    BMI = models.FloatField()  # Use FloatField for decimal values
    Blood_Group = models.CharField(max_length=10)  # Adjust length as needed
    Pulse_rate = models.FloatField()  # bpm
    RR = models.FloatField()  # breaths/min
    Hb = models.FloatField()  # g/dl
    Marriage_Status = models.IntegerField()  # years
    Pregnant = models.CharField(max_length=3)  # 'Y' or 'N'
    No_of_abortions = models.IntegerField()
    TSH = models.FloatField()  # mIU/L
    PRG = models.FloatField()  # ng/mL
    RBS = models.FloatField()  # mg/dl
    Weight_gain = models.CharField(max_length=3)  # 'Y' or 'N'
    Hair_loss = models.CharField(max_length=3)  # 'Y' or 'N'
    Fast_food = models.CharField(max_length=3)  # 'Y' or 'N'
    Reg_Exercise = models.CharField(max_length=3)  # 'Y' or 'N'
    BP_Systolic = models.IntegerField()  # mmHg
    BP_Diastolic = models.IntegerField()  # mmHg
    Follicle_No_L = models.IntegerField()
    Follicle_No_R = models.IntegerField()


    def __str__(self):
        return f"Assessment {self.id} - {self.PCOS}"
