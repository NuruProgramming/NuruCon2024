from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .forms import SpeakerForm, RegistrationForm, SponsorForm
from .models import Speaker, Sponsor, Registration


def index(request):
    speaker_count = Speaker.objects.count()
    registration_count = Registration.objects.count()
    speakers = Speaker.objects.filter(approved=True).values('name', 'title', 'image')
    sponsors = Sponsor.objects.filter(approved=True).values('name', 'logo', 'website')
    return render(request, "index.html", {
        'speaker_count': speaker_count,
        'registration_count': registration_count,
        'speakers': speakers,
        'sponsors': sponsors
    })

def submit_speaker(request):
    if request.method == 'POST':
        form = SpeakerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'We will reach out to you soon!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)


def submit_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Tuonane Tar 5 October 👊🏾'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)


def submit_sponsor(request):
    if request.method == 'POST':
        form = SponsorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'We will reach out to you within a few hours.'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)


def registration_count(request):
    count = Registration.objects.count()
    return HttpResponse(f"{count} and counting")
