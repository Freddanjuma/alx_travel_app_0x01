import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
from listings.models import Listing

# Get the custom User model
User = get_user_model()

class Command(BaseCommand):
    help = 'Populates the database with sample listings data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting to seed the database..."))

        # Initialize Faker
        fake = Faker()

        # --- 1. Get or Create a Host User ---
        # We must create a 'host' user first to create listings.
        host_user, created = User.objects.get_or_create(
            email='host@example.com',
            defaults={
                'first_name': 'Demo',
                'last_name': 'Host',
                'role': User.Role.HOST, # Use the ENUM from your User model
                'is_staff': False,
                'is_superuser': False,
            }
        )
        
        if created:
            host_user.set_password('alxpassword123')
            host_user.save()
            self.stdout.write(self.style.SUCCESS(f'Created host user: {host_user.email}'))
        else:
            self.stdout.write(self.style.WARNING(f'Host user {host_user.email} already exists.'))

        # --- 2. Create Sample Listings ---
        num_listings = 20
        listings_created_count = 0

        for _ in range(num_listings):
            try:
                Listing.objects.create(
                    host=host_user, # Assign the existing host
                    title=fake.sentence(nb_words=5),
                    description=fake.paragraph(nb_sentences=3),
                    address=fake.street_address(),
                    city=fake.city(),
                    country=fake.country(),
                    price_per_night=round(random.uniform(50.00, 350.00), 2)
                )
                listings_created_count += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error creating listing: {e}'))

        self.stdout.write(self.style.SUCCESS(
            f'Successfully seeded the database with {listings_created_count} listings for {host_user.email}.'
        ))
