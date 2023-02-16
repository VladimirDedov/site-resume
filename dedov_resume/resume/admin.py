from django.contrib import admin
from .models import *

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('name' ,'email','phone' , 'address', 'photo', 'published')
    list_editable = ('published',)


@admin.register(Education)
class AdminEducation(admin.ModelAdmin):
    list_display = ('school_name','user',  'description', 'specialization', 'years' )

@admin.register(JobSkills)
class AdminJobSkills(admin.ModelAdmin):
    list_display = ('id', 'description_job')

@admin.register(Experience)
class AdminExperience(admin.ModelAdmin):
    list_display = ('name_organization', 'position', 'years', 'description')

@admin.register(Language)
class AdminLanguage(admin.ModelAdmin):
    list_display = ('name_language', 'level')

@admin.register(Skills)
class AdminSkills(admin.ModelAdmin):
    list_display = ('skill_name', 'skill_value','tooltip', 'skill_level')