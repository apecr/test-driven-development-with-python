from django.test import TestCase

from lists.models import Item


class ListViewTest(TestCase):
    def test_display_all_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertTemplateUsed(response, 'list.html')
