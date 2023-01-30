from django.test import TestCase

from lists.models import List, Item


class NewItemTest(TestCase):
    def test_can_save_a_POST_request_to_an_existing_list(self):
        _, new_list = self.__create_item_in_list()

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, new_list)

    def test_redirects_to_list_view(self):
        response, new_list = self.__create_item_in_list()

        self.assertRedirects(response, f'/lists/{new_list.id}/')

    def __create_item_in_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
            f'/lists/{correct_list.id}/add_item',
            data={'item_text': 'A new item for an existing list'}
        )
        return response, correct_list
