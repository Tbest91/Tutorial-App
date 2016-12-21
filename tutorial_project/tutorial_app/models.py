from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here



class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to= 'profile_images', blank=True)
	bio = models.TextField(blank=True)

	def __unicode__(self):
		return self.user.username






class Category(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=100, unique=True)
	likes = models.IntegerField(default=0)
	slug = models.SlugField()

	def save(self,*args, **kwargs):
		self.slug = slugify(self.name)

		if self.likes <0:
			self.likes = 0

		super(Category, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name


class Page(models.Model):
	user = models.ForeignKey(User)
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title

