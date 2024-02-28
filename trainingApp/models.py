from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Teacher(models.Model):
    ...


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование курса')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель')
    start_products = models.DateTimeField(**NULLABLE, verbose_name='Начало курса')
    cost = models.CharField(**NULLABLE, verbose_name='Стоимость курса')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


