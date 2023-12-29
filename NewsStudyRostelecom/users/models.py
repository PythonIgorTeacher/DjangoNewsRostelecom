from django.db import models
from django.contrib.auth.models import User

from django.core.validators import RegexValidator
validate_phone = RegexValidator('\+7\s?[\(]{0,1}9[0-9]{2}[\)]{0,1}\s?\d{3}[-]{0,1}\d{2}[-]{0,1}\d{2}',
                                      message='Номер телефона указан некорректно')

class Account(models.Model):
    gender_choices= (('M','Male'),
                     ('F','Female'),
                     ('N/A','Not answered'))
    user = models.OneToOneField(User,on_delete=models.CASCADE,
                                primary_key=True)
    nickname = models.CharField(max_length=100)
    birthdate = models.DateField(null=True)
    gender = models.CharField(choices=gender_choices,max_length=20,null=True)
    account_image = models.ImageField(default='default.jpg',
                                      upload_to='account_images')
    address = models.CharField(max_length=100,null=True)
    vk = models.CharField(max_length=100,null=True)
    instagram = models.CharField(max_length=100,null=True)
    telegram = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=20,null=True,validators=[validate_phone])
    #pip install pillow в терминале если нет библиотеки

    def __str__(self):
        return f"{self.user.username}'s account"
    class Meta:
        ordering = ['user']
        verbose_name = 'Профиль'
        verbose_name_plural ='Профили'


from news.models import Article
class FavoriteArticle(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    article = models.ForeignKey(Article,on_delete=models.SET_NULL,null=True)
    create_at=models.DateTimeField(auto_now_add=True)