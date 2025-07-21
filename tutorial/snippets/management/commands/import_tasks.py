# tasks/management/commands/import_tasks.py
import requests
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from snippets.models import Task

User = get_user_model()

class Command(BaseCommand):
    help = 'Import tasks from JSONPlaceholder into the Task model'

    def handle(self, *args, **kwargs):
        # Assign all imported tasks to a default owner
        owner, _ = User.objects.get_or_create(username='jsonplaceholder_user', defaults={
            'email': 'placeholder@example.com',
            'password': 'change_this_password'
        })

        url = 'https://jsonplaceholder.typicode.com/todos'

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            self.stderr.write(f"API request failed: {e}")
            return

        tasks_data = response.json()

        for item in tasks_data:
            title = item['title']
            is_complete = item['completed']

            task, created = Task.objects.update_or_create(
                title=title,  # You may want to use a more unique field
                owner=owner,
                defaults={
                    'description': 'Imported from JSONPlaceholder',
                    'is_complete': is_complete,
                    'due_date': None,
                    'completed_at': timezone.now() if is_complete else None,
                }
            )

            status = "Created" if created else "Updated"
            self.stdout.write(f"{status} task: {title}")
