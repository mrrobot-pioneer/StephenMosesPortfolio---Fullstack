from django.shortcuts import render
from django.http import JsonResponse
import json
from collections import OrderedDict
from .models import Project, Skill, Experience, Message

def index(request):
    # Fetch and order projects by rank first, then by created_at
    projects = Project.objects.all().order_by('rank', '-created_at')
    experiences = Experience.objects.all().order_by('-start_date')

    # Group skills by category in the correct order
    category_order = ['frontend', 'backend', 'testing', 'deployment']
    skills_by_category = OrderedDict()
    
    # Initialize with all categories in the correct order
    for category_key in category_order:
        skills_by_category[category_key] = []
    
    # Populate skills
    for skill in Skill.objects.all():
        if skill.category in skills_by_category:
            skills_by_category[skill.category].append(skill)

    # Pass data to the template
    context = {
        'projects': projects,
        'skills_by_category': skills_by_category,
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