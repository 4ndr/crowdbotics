from django.db import models
from owner.models import Owner


class Pet(models.Model):
    name = models.CharField('name', max_length=100, blank=False)
    birthday = models.DateField('birthday', blank=False)
    owner = models.ForeignKey(Owner, blank=False, null=True)

    def __str__(self):
        return self.name


class Dog(Pet):

    class Meta:
        verbose_name = 'Dog'
        verbose_name_plural = 'Dogs'


class Cat(Pet):
    class Meta:
        verbose_name = 'Cat'
        verbose_name_plural = 'Cats'