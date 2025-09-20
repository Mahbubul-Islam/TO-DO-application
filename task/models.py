from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model): 
    STATE = [('pending', 'Pending'),
              ('completed', 'Completed')] # ('backend', 'frontend')
    
    CATEGORY = [('personal', 'Personal'),
                ('work', 'Work'),
                ('others', 'Others')]
    
    title = models.CharField(max_length=100) # for title
    description = models.TextField() # for description
    deu_date = models.DateField() # for due date
    deu_time = models.TimeField() # for due time
    state = models.CharField(max_length=10, choices=STATE, default= 'Pending') # select state by choise default will be pending
    category = models.CharField(max_length=10, choices=CATEGORY)
    is_completed = models.BooleanField(default=False) # for showing and filtering
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.title

