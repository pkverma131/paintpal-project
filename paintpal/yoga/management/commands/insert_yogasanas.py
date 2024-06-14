import os
import json
from django.core.management.base import BaseCommand
from yoga.models import Yogasana

class Command(BaseCommand):
    help = 'Insert data from JSON files into Yogasana model'

    def add_arguments(self, parser):
        parser.add_argument('directory', type=str, help='Directory containing JSON files')

    def handle(self, *args, **kwargs):
        directory = kwargs['directory']
        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r') as file:
                    data = json.load(file)
                    yogasana = Yogasana.objects.create(
                        name=data['entry_title'],
                        description='',
                        steps='\n'.join(data['step_by_step']),
                        beginners_tips='\n'.join(data['beginners_tips']),
                        benefits='\n'.join(data['benefits']),
                        cautions='\n'.join(data['watch_out_for']),
                        variations='\n'.join(data['variations'])
                    )
                    self.stdout.write(self.style.SUCCESS(f'Successfully inserted {yogasana.name}'))

