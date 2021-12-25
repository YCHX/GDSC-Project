from django.shortcuts import render
from django import forms


# Create task form
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    status = forms.fields.ChoiceField(
        choices = (
            ('todo', 'TODO'),
            ('done', 'DONE')
        ), 
        required=True,
        widget=forms.widgets.Select
    )


# Create your views here.
def index(request):
    return render(request, "tasks/index.html")

# Add a new task:
def add(request):
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })