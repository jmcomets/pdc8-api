# *-* coding: utf8 *-*
import csv
from django.core.management.base import NoArgsCommand
from catalog.models import Tree, TreeGenre

class Command(NoArgsCommand):
    def parse_data(self, filename):
        with open(filename, 'r') as fp:
            for tree_data in csv.DictReader(fp):
                tree_genre_fields = {
                        'name'   : tree_data['Genre'],
                        'species': tree_data['Espèce'],
                        'type'   : tree_data["Type d'arbre"]
                        }
                tree_fields = {
                        'id'            : tree_data['identifiant'],
                        'name'          : tree_data['Type en français'],
                        'area'          : tree_data["Nom de l'espace"],
                        'height'        : tree_data['Hauteur totale m'],
                        'trunk_diameter': tree_data['Diamètre du tronc cm'],
                        'crown_diameter': tree_data['Diamètre de la couronne m']
                        }
                yield tree_genre_fields, tree_fields

    def handle_noargs(self, **options):
        parsed_data = list(self.parse_data('arbres.csv'))
        for tree_genre_fields, tree_fields in parsed_data:
            tree_genre, created = TreeGenre.objects.get_or_create(**tree_genre_fields)
            tree_fields['genre'] = tree_genre
            if created:
                print('imported TreeGenre %s' % tree_genre.name)
        print('importing %s Trees' % len(parsed_data))
        Tree.objects.bulk_create(map(lambda ts: Tree(**ts[1]), parsed_data))
