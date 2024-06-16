from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=52)
	description = models.TextField()
	image = models.TextField()

	def __str__(self) -> str:
		return self.title
	
	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'