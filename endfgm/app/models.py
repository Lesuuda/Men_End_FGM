from django.db import models

"""information page class"""

class Information(models.Model):
    """
    class that provides various information on FGM
    """
    title = models.CharField(max_length=255)
    content = models.TextField(default='')
    category = models.CharField(max_length=100, choices=(
        ('effects', 'Harmful Effects of FGM'),
        ('legal', 'Legal Aspects of FGM'),
        ('myths', 'Myths and Misconceptions'),
        ('resources', 'Resources and Support'),
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """dunder method to print the content in string format"""
        return self.title

class Story(models.Model):
    """
    class to handle personal stories and accounts of thee
    effects of FGM
    """
    title = models.CharField(max_length=255)
    content = models.TextField(default='')
    pseudonym = models.CharField(max_length=50, blank=True)
    anonymized_location = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """dunder method to print the story in string format"""
        return self.title



