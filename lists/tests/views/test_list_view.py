from django.test import TestCase

from lists.models import Item, List


class ListViewTest(TestCase):
    def test_display_all_items(self):
        list_ = List.objects.create()
        Item.objects.create(text='itemey 1', list=list_)
        Item.objects.create(text='itemey 2', list=list_)

        response = self.client.get(f'/lists/{list_.id}/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')

    def test_uses_list_template(self):
        list_ = List.objects.create()

        response = self.client.get(f'/lists/{list_.id}/')

        self.assertTemplateUsed(response, 'list.html')

    def test_display_items_only_for_that_list(self):
        new_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=new_list)
        Item.objects.create(text='itemey 2', list=new_list)

        other_list = List.objects.create()
        Item.objects.create(text='Other list item 1', list=other_list)
        Item.objects.create(text='Other list item 2', list=other_list)

        response = self.client.get(f'/lists/{new_list.id}/')
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'Other list item 1')
        self.assertNotContains(response, 'Other list item 2')

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get(f'/lists/{correct_list.id}/')
        self.assertEqual(response.context['list'], correct_list)
