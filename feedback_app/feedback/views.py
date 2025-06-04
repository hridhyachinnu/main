from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import InternFeedbackForm

def intern_feedback_view(request):
    if request.method == 'POST':
        form = InternFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html', {'name': form.cleaned_data['name']})
    else:
        form = InternFeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})