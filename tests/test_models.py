from django.test import TestCase
from .models import Organizer

class OrganizerModelTest(TestCase):
    # Create a test instance of Organizer model
    @classmethod
    def setUpTestData(cls):
        Organizer.objects.create(name='Test Organizer', email='test@example.com', phone='1234567890')

    # Test for the correct label of the name field
    def test_name_label(self):
        organizer = Organizer.objects.get(id=1)
        # get the label of the name field of Organizer model
        field_label = organizer._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    # Test for the correct label of the email field
    def test_email_label(self):
        organizer = Organizer.objects.get(id=1)
        # get the label of the email field of Organizer model
        field_label = organizer._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    # Test for the correct label of the phone field
    def test_phone_label(self):
        organizer = Organizer.objects.get(id=1)
        field_label = organizer._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'phone')

    # Test for the correct max length of the name field
    def test_name_max_length(self):
        organizer = Organizer.objects.get(id=1)
        # get the max length of the name field of Organizer model
        max_length = organizer._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    # Test for the correct max length of the email field
    def test_email_max_length(self):
        organizer = Organizer.objects.get(id=1)
        max_length = organizer._meta.get_field('email').max_length
        # assert that the max length matches the expected value
        self.assertEquals(max_length, 254)

    # Test for the correct string representation of the object
    def test_object_name_is_name(self):
        organizer = Organizer.objects.get(id=1)
        expected_object_name = f'{organizer.name}'
        self.assertEquals(expected_object_name, str(organizer))

    # Positive test for valid phone number
    def test_valid_phone_number(self):
        organizer = Organizer.objects.get(id=1)
        organizer.phone = '+1-123-456-7890'
        organizer.save()
        updated_organizer = Organizer.objects.get(id=1)
        self.assertEquals(updated_organizer.phone, '+1-123-456-7890')

    # Negative test for invalid phone number
    def test_invalid_phone_number(self):
        organizer = Organizer.objects.get(id=1)
        with self.assertRaisesMessage(ValueError, 'Phone number must be in a valid format.'):
            organizer.phone = '123'
            organizer.save()