from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'


class Skills(models.Model):
    name = models.CharField(max_length=256, blank=False, verbose_name='Навык')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
