from django.test import TestCase

from lists.models import Item


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')

    def test_only_save_items_when_post(self):
        self.client.get('/')

        self.assertEqual(Item.objects.count(), 0)
