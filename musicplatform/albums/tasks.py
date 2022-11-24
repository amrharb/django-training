from django.utils import timezone
from artists.models import Artist
from celery import shared_task
from django.core.mail import send_mail

@shared_task()
def send_artist_a_congratulation_email(id, name, release_at, cost):
    artist = Artist.objects.get(user_id = id)
    msssage = f'Album: {name}, released: {release_at} and cost is: {cost}'
    send_mail('Congratulate !', msssage, 'mahmoud.gmail.com', [artist.user.email], fail_silently=False,)

@shared_task()
def send_artist_a_reminder_email():
    for artist in Artist.objects.all():
        last_album = artist.albums.all().order_by('-created').first()
        if last_album.created.date() < timezone.now() - timezone.timedelta(days=30):
            message = 'Hi ' + artist.stage_name + ' we miss your albums, please release new albums such that people know you.'
            send_mail('Reminder !', message,'amr.gmail.com', [artist.user.email])