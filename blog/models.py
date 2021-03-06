from django.db import models
from django.conf import settings


# Create your models here.
User= settings.AUTH_USER_MODEL

class BlogPost(models.Model): #blogpost_set -> queryset
	# id = models.IntergerField() #pk
	user=models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=120)
	slug= models.SlugField(unique=True)
	content = models.TextField(null=True, blank=True)

	def get_absolute_url(self):
		return f"/blog/{self.slug}"

	def get_edit_url(self):
		return f"{self.get_absolute_url}/edit"

	def get_delete_url(self):
		return f"{self.get_absolute_url}/delete"
	

