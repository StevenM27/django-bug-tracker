from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Bug
from .forms import BugForm, SortForm

# Create your views here.
def index(request):

    if request.method == "POST":
        form = SortForm(request.POST)

        if form.is_valid():
            sort_by = form.cleaned_data.get("CHOICES")

    else:
        sort_by = "date"

    print("Sorting by " + sort_by)

    bug_list = Bug.objects.order_by("-" + str(sort_by))
    sort_form = SortForm()

    page = {
        "list" : bug_list,
        "title" : "Bug Tracker",
        "form" : sort_form,
    }

    return render(request, 'bugtracker/index.html', page)


def new_bug(request):

    if request.method == "POST":
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bugtracker')
    form = BugForm()

    page = {
        "forms" : form,
        "title" : "Bug Tracker",
    }

    return render(request, 'bugtracker/new_bug.html', page)


def edit(request, bug_id):

    bug = Bug.objects.get(id=bug_id)
    form = BugForm(initial={'author': bug.author, 'type': bug.type, 'priority': bug.priority, 'description': bug.description, 'status': bug.status, 'date': bug.date})
    page = {
        "form": form,
        "bug": bug,
        "title": "Bug Tracker",
    }

    return render(request, 'bugtracker/edit.html', page)



def update(request, bug_id):
    bug = Bug.objects.get(id=bug_id)
    form = BugForm(request.POST)
    if form.is_valid():
        bug.author = form.cleaned_data['author']
        bug.type = form.cleaned_data['type']
        bug.priority = form.cleaned_data['priority']
        bug.description = form.cleaned_data['description']
        bug.date = form.cleaned_data['date']
        bug.status = form.cleaned_data['status']

        bug.save()

    return redirect('bugtracker')



def delete(request, bug_id):
    bug = Bug.objects.get(id=bug_id)
    bug.delete()
    messages.info(request, "Bug entry has been removed.")
    return redirect('bugtracker')