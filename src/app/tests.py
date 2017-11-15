from django.urls import resolve
from django.test import TestCase
from app.controllers.base import index
from django.http import HttpRequest


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'app/home/index.html')

    def test_should_be_able_to_search_psle(self):
        response = self.client.get('/schools/', data={'score': '200'})
        self.assertIn('ADMIRALTY SECONDARY SCHOOL', response.content.decode())

    # def test_should_not_be_able_to_search_psle(self):
    #     response = self.client.get('/schools/', data={'score': '400'})
    #     self.assertIn('Please enter valid PSLE score', response.content.decode())

    # def test_saving_and_retrieving_items(self):
    #     first_item = Item()
    #     first_item.text = 'The first (ever) list item'
    #     first_item.save()
    #     second_item = Item()
    #     second_item.text = 'Item the second'
    #     second_item.save()
    #     saved_items = Item.objects.all()
    #     self.assertEqual(saved_items.count(), 2)
    #     first_saved_item = saved_items[0]
    #     second_saved_item = saved_items[1]
    #     self.assertEqual(first_saved_item.text, 'The first (ever) list item')
    #     self.assertEqual(second_saved_item.text, 'Item the second')
