from django.contrib import admin
from resume.models import *
# Register your models here.
class Profile_Admin(admin.ModelAdmin):
        list_display=['content',]

class ExperienceAdmin(admin.ModelAdmin):
        list_display=['jobtitle','summary']

class keySkillsAdmin(admin.ModelAdmin):
        list_display=['languages',]

class EducationAdmin(admin.ModelAdmin):
        list_display=['Qualification','percentage','college']

class TrainingAdmin(admin.ModelAdmin):
        list_display=['institute','duration','instructor']
admin.site.register(Profile,Profile_Admin)
admin.site.register(Experience,ExperienceAdmin)
admin.site.register(keySkills,keySkillsAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(Training,TrainingAdmin)
