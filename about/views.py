from django.shortcuts import render
from .models import About
from django.contrib import messages
from .forms import CollaborateForm
# Create your views here.


def AboutView(request):
    """
    Renders the About page
    """

    about = About.objects.all().order_by('-updated_on').first()
    
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
            request, messages.SUCCESS,
            "Request submitted I'll get back to you soon!"
            )

    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form":collaborate_form,
         },
    )