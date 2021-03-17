from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Properites(models.Model):

    # reovoke the user name in properites model
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    vechile_name=models.CharField(max_length=200)
    vechile_series=models.CharField(max_length=200)
    vechile_price=models.IntegerField()
    vechile_description=models.TextField()
    vechile_image=models.CharField(max_length=500,default='https://www.google.com/search?q=coming+soon+images&tbm=isch&source=iu&ictx=1&fir=c9EY_13CZrZRWM%252CZL4qJNgKW_3MbM%252C_&vet=1&usg=AI4_-kSNigLBzBYkcLD6F8TsMbtt0ISAKA&sa=X&ved=2ahUKEwi5zb_fgNjtAhVaxDgGHXYyA24Q9QF6BAgNEAE#imgrc=c9EY_13CZrZRWM')
