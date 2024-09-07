import csv
from django.core.management.base import BaseCommand
from banks.models import Bank, Branch

class Command(BaseCommand):
    help = 'Load bank and branch data from CSV file'

    def handle(self, *args, **kwargs):
        # Use 'utf-8' encoding to avoid UnicodeDecodeError
        with open('bank_branches.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                bank, created = Bank.objects.get_or_create(
                    bank_id=row['bank_id'],
                    defaults={'name': row['bank_name']}
                )
                branch, created = Branch.objects.update_or_create(
                    ifsc=row['ifsc'],
                    defaults={
                        'bank': bank,
                        'branch_name': row['branch'],
                        'address': row['address'],
                        'city': row['city'],
                        'district': row['district'],
                        'state': row['state'],
                    }
                )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
