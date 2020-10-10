from django.db import models
from users.models import Profile

# Create your models here.
class Category (models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = "categories"

class Condition (models.Model):
    condition = models.CharField(max_length=100)

    def __str__(self):
        return self.condition

class Team (models.Model):
    team = models.CharField(max_length=100)

    def __str__(self):
        return self.team

class Item (models.Model):
    STATUS = (
			('Reject', 'Reject'),
			('Monitor', 'Monitor'),
			('Passed', 'Passed'),
			)

    PRIORITY = (
			('Low', 'Low'),
			('Medium', 'Medium'),
			('High', 'High'),
			)
    title = models.CharField(max_length=200, blank=True,)
    category = models.ForeignKey(Category, null=True,  on_delete= models.SET_NULL)
    condition = models.ForeignKey(Condition, null=True, on_delete= models.SET_NULL)
    status = models.CharField(max_length=200, choices=STATUS)
    checker = models.ForeignKey(Profile, null=True, on_delete= models.SET_NULL)
    date_checked = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=200, choices=PRIORITY)
    team = models.ForeignKey(Team, null=True, on_delete= models.SET_NULL)
    comments = models.TextField(blank=True)
    photo_main = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='images')


    def __str__(self):
        return self.title

    