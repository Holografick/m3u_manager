from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Channel(models.Model):
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Link(models.Model):
    channel = models.ForeignKey('Channel', on_delete=models.CASCADE)
    is_primary = models.BooleanField()
    url = models.CharField(max_length=500)

    def __str__(self):
        return '{} | {} | {}'.format(self.channel.name, self.is_primary, self.url)

