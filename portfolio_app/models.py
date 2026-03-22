from django.db import models
from django.core.validators import FileExtensionValidator

class Project(models.Model):
    RANK_CHOICES = [
        (1, 'Rank 1 - Highest Priority'),
        (2, 'Rank 2'),
        (3, 'Rank 3'),
        (4, 'Rank 4'),
        (5, 'Rank 5 - Lowest Priority'),
    ]

    name = models.CharField(max_length=500)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='projects/')
    skills_used = models.ManyToManyField('Skill', related_name="projects")
    link = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    rank = models.PositiveIntegerField(choices=RANK_CHOICES, default=1) 

    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('testing', 'Testing'),
        ('deployment', 'Deployment'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    icon = models.FileField(
        upload_to='skills/',
        validators=[FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg', 'gif', 'webp'])]
    )

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.role} at {self.company}'


class Message(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_contact = models.CharField(max_length=100)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    send_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message