from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Project, Skill, Service, Experience, Message

def index(request):
    # Fetch and order projects by rank first, then by created_at
    projects = Project.objects.all().order_by('-rank', '-created_at')
    services = Service.objects.all()
    experiences = Experience.objects.all().order_by('start_date')


    # Group skills by category
    skills_by_category = {}
    for skill in Skill.objects.all():
        skills_by_category.setdefault(skill.category, []).append(skill)

    # Pass data to the template
    context = {
        'projects': projects,
        'skills_by_category': skills_by_category,
        'services': services,
        'experiences' : experiences
    }

    return render(request, 'portfolio_app/index.html', context)


def contact(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Message.objects.create(
            sender_name=data['name'],
            sender_contact=data['email'],
            message=data['message']
        )
        return JsonResponse({'message': 'Message sent successfully'})