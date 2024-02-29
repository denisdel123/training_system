from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Teacher(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    photo = models.ImageField(upload_to='teacher_photo/', verbose_name='Фотография', **NULLABLE)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Автор')
    start_products = models.DateTimeField(**NULLABLE, verbose_name='Начало')
    cost = models.CharField(max_length=50, **NULLABLE, verbose_name='Стоимость')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Student(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    photo = models.ImageField(upload_to='student_photo/', verbose_name='Фотография')
    access = models.ManyToManyField(Course, **NULLABLE, verbose_name='Доступные курсы')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    title = models.CharField(max_length=100, verbose_name='Название урока')
    link_to_video = models.URLField(verbose_name='Ссылка')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Group(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название группы')
    students = models.ManyToManyField(Student, **NULLABLE, verbose_name='Студенты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
