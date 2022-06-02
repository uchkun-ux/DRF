from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    

    # class Meta:
    #     verbo")
    #     verbose_names")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     ret_detail", kwargs={"pk": self.pk})
