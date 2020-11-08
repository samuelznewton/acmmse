from django.db import models
from django.conf import settings

# Create your models here.

class ImageContent(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.ImageField(upload_to='')
    def __str__(self):
        return self.content.url
    def __unicode__(self):
        return self.content.url
    class Meta:
        verbose_name_plural = "Image content"

class About_Pages(models.Model):
    PAGE_CHOICES = (
        ('ACM', 'About ACM'),
        ('MSE', 'About ACM Mid-Southeast'),
    )
    page = models.CharField(max_length=3, choices=PAGE_CHOICES, unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField(widget=forms.TextInput(attrs={'placeholder': 'Format with html, images are found at /file/filename'}))
    images = models.ManyToManyField(ImageContent, blank=True, label='filenames listed for convenience, no need to select these')
    def __str__(self):
        return self.page
    def __unicode__(self):
        return self.page
    class Meta:
        verbose_name_plural = "About pages"

class File(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to="")
    def filename(self):
        return os.path.basename(self.file.name)
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(widget=forms.TextInput(attrs={'placeholder': 'Format with html, images are found at /file/filename'}))
    images = models.ManyToManyField(ImageContent, blank=True, label='filenames listed for convenience, no need to select these')
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

class Officer(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    university = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='officers')
    def __str__(self):
        return self.position
    def __unicode__(self):
        return self.position

class Conference(models.Model):
    year = models.PositiveIntegerField()
    content = models.TextField(widget=forms.TextInput(attrs={'placeholder': 'Format with html, images are found at /file/filename'}))
    images = models.ManyToManyField(ImageContent, blank=True, label='filenames listed for convenience, no need to select these')
    def __str__(self):
        return str(self.year)
    def __unicode__(self):
        return str(self.year)
