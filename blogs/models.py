from django.db import models

class Title(models.Model):
    title_text = models.CharField(max_length=75)
    pub_date = models.DateTimeField(auto_now_add = True) 

    def __str__(self):
        return self.title_text


class Body(models.Model):
   title = models.ForeignKey(Title, on_delete=models.CASCADE)
   body_text = models.CharField(max_length=200)

   def __str__(self):
       return self.body_text

