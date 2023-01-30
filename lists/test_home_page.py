from django.test import TestCase

from lists.models import Item


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_post_request(self):
        self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirect_after_post(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

    def test_only_save_items_when_post(self):
        self.client.get('/')

        self.assertEqual(Item.objects.count(), 0)
