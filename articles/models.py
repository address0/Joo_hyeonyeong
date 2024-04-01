from django.db import models

# Create your models here.
class MenuList(models.Model):
    date = models.DateField()
    menu_course_type = models.CharField(max_length=2)
    set_menu_name = models.TextField()