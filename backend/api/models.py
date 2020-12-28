from django.db import models

"""
Create a database model for the project.
"""

# Create your models here.
class Hero(models.Model):
    """
    Hero model for database.
    """
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name