from django.contrib import admin
from .models import Classes, Sections, Students
# Register your models here.


class ClassesAdmin(admin.ModelAdmin):
    list_display = ['added_by', 'name', 'category']


class SectionsAdmin(admin.ModelAdmin):
    list_display = ['section_added_by', 'section_of_class', 'section_name']


class StudentsAdmin(admin.ModelAdmin):
    list_display = ['student_added_by', 'student_class', 'student_section']


admin.site.register(Classes, ClassesAdmin)
admin.site.register(Sections, SectionsAdmin)
admin.site.register(Students, StudentsAdmin)