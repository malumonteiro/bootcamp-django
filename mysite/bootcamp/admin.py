from django.contrib import admin

from .models import Course

# Register your models here.

@admin.register(Course)
class CourseEntryLineAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "date", "age", "active"]
