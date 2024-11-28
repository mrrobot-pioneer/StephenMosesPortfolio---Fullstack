from django.contrib import admin
from .models import Project, Skill, Service,Experience, Message

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_skills_used', 'created_at')
    list_filter = ('created_at', 'skills_used')
    search_fields = ('name', 'description', 'skills_used__name')

    def get_skills_used(self, obj):
        return ", ".join([skill.name for skill in obj.skills_used.all()])
    get_skills_used.short_description = 'Skills Used'

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'category')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'pricing')
    search_fields = ('name', 'description')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'role', 'start_date', 'end_date')
    search_fields = ('company', 'role')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender_contact', 'is_read', 'send_at')
    list_filter = ('is_read', 'send_at')
    search_fields = ('sender_name', 'sender_contact', 'message')
