from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=32, null=False, unique=False)
    location = models.CharField(max_length=32, null=False)
    description = models.CharField(max_length=256, null=False, unique=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # verbose_name = 'Group'
        #fields = ['name', 'location', 'description']
        ordering = ['created']
        unique_together = (('name', 'location'))

    def __str__(self):
        return self.name
