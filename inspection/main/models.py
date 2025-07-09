from django.db import models

class JobTitle(models.Model):
    name = models.CharField(max_length=300, db_index=True)
    slug = models.SlugField(max_length=300, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self): # Метод отображения в Админке
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=300, db_index=True)
    slug = models.SlugField(max_length=300, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=20, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Гендер'
        verbose_name_plural = 'Гендер'

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    job_title = models.ForeignKey(JobTitle, related_name='employees', on_delete=models.PROTECT)
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.PROTECT)
    gender = models.ForeignKey(Gender, related_name='employees', on_delete=models.PROTECT)
    birthday = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='employees/%Y/%m/%d', blank=True)
    resume = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name

