from django.db import models
from django.utils import timezone

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
)

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="post_images/")
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
