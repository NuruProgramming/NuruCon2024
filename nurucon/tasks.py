import threading
from django.core.mail import mail_admins


def send_admin_email(subject, message):
    def send_mail():
        mail_admins(subject, message, fail_silently=True)

    thread = threading.Thread(target=send_mail)
    thread.start()
