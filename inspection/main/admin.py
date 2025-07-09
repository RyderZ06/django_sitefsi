from django.contrib import admin
from .models import JobTitle, Department, Gender, Employee

@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'job_title', 'department', 'gender', 'birthday', 'image', 'resume', 'created', 'updated']
    list_filter = ['job_title', 'department', 'gender']  # Добавляет фильтры в админке для удобства
    search_fields = ['name', 'resume']  # Поля для поиска
    prepopulated_fields = {'slug': ('name',)}  # Автозаполнение slug из name
    readonly_fields = ['created', 'updated']  # Поля только для чтения
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'job_title', 'department', 'gender', 'birthday', 'image', 'resume')
        }),
        ('Дополнительная информация', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',),  # Скрываемое поле
        }),
    )
