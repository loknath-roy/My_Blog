from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField



# Catagory Model
class Catagory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='catagory/')
    added_date = models.DateTimeField(auto_now_add=True,null=True)
    def image_tag(self):
        return format_html('<img src = "/media/{}" style = "width:40px; hight:40px;" />'.format(self.image))


    def __str__(self) -> str:
        return self.title
    

# Post Model
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    content = HTMLField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/',blank=True, null=True)
    added_date = models.DateTimeField(auto_now_add=True,null=True)
    cat = models.ForeignKey(Catagory,on_delete=models.CASCADE)

    def image_tag(self):
        return format_html('<img src = "/media/{}" style = "width:40px; hight:40px;" />'.format(self.image))


    def __str__(self) -> str:
        return self.title