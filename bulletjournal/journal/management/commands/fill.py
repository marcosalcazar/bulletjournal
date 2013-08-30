# -*- coding: utf-8 *-*
import datetime
from django.contrib.auth.models import User
from django.core.management.base import NoArgsCommand
import os
from django.core.management import call_command
from bulletjournal.settingsdev import DATABASE_NAME
from journal.models import Task, Event


try:
    os.remove(DATABASE_NAME)
except:
    pass
call_command('syncdb', interactive=False)
#call_command('migrate')


class Command(NoArgsCommand):

    def handle(self, *args, **options):
        print("User 'admin', pass='admin'")
        admin = User.objects.create(
            username="admin",
            email="admin@test.com.ar",
            password="pbkdf2_sha256$10000$nV6OEoaqhtYK$740HSWOW0Il7l5bqQjZGGKc/7QQmUvErb8WCiLoPtcE=",
            is_staff=True,
            is_active=True,
            is_superuser=True,
            last_login=datetime.datetime.now()
        )
        
        today = datetime.date.today()
        Task.objects.create(
            date = today,
            description = 'Programm a lot!',
            user = admin,
            indicator = 'N'
        )
        Event.objects.create(
            date = today - datetime.timedelta(days=1),
            description = 'Go shopping',
            user = admin,
            indicator = 'N'  
        )
        Event.objects.create(
            date = today,
            description = 'Meeting with Daniel',
            user = admin,
            indicator = 'N'  
        )

        print "Filling ended"
