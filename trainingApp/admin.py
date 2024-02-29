from django.contrib import admin

from trainingApp.models import Teacher, Student, Course, Lesson, Group


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'teacher', 'start_products', 'cost',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'course', 'link_to_video',)


@admin.register(Group)
class CroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'students', 'course',)