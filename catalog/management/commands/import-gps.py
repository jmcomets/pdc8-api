import sys
import csv
from django.core.management.base import NoArgsCommand
from catalog.models import Tree

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        with open('gps.csv', 'r') as fp:
            reader = csv.reader(fp)
            for row in reader:
                short_id, latitude, longitude = row
                try:
                    tree = Tree.objects.get(id='AR%s' % short_id)
                    tree.latitude = latitude
                    tree.longitude = longitude
                    sys.stdout.write('+ %s\n' % short_id)
                    tree.save()
                except Tree.DoesNotExist:
                    sys.stdout.write('- %s\n' % short_id)
                sys.stdout.flush()
