from django.shortcuts import render
from .models import Event
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


def home(request):
    reviews = Review.objects.all().order_by('-created_at')
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.save()
            return redirect('home')
    else:
        form = ReviewForm()

    return render(request, 'main/home.html', {'form': form, 'reviews': reviews})

def calendar_view(request):
    events = Event.objects.all()
    event_list = [{'title': event.title, 'start': event.start_date.isoformat(), 'end': event.end_date.isoformat()} for event in events]
    return render(request, 'main/calendar.html', {'events': event_list})


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
    else:
        form = EventForm()
    return render(request, 'main/add_event.html', {'form': form})
