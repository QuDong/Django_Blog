from django.db import models
from django.core.urlresolvers import reverse
from tinymce.models import HTMLField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100) #blog title
    category = models.CharField(max_length=50, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    content = HTMLField() #todo-qd: blank? null?

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path

    def __str__(self): #python2使用__unicode__, python3使用__str__
        return self.title

    class Meta:
        ordering = ['-date_time']