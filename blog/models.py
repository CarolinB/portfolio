from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        bodyPreview = self.body[:100]
        return bodyPreview

    def date_format(self):
        return self.pub_date.strftime('%b %e %Y, %I:%M %p')
