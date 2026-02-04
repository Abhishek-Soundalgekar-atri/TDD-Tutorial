from django.test import TestCase
from lists.models import Item
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        self.assertEqual(saved_items[0].text, 'The first (ever) list item')
        self.assertEqual(saved_items[1].text, 'Item the second')
        
    def test_cannot_save_empty_item(self):
        item = Item(text='')
        with self.assertRaises(ValidationError):
            item.full_clean()