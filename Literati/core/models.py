from django.db import models

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('Graphics Designing', 'Graphics Designing'),
        ('Editing', 'Editing'),
        ('Voice Acting', 'Voice Acting'),
        ('Public Speaking', 'Public Speaking'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category} - {self.title}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

    
