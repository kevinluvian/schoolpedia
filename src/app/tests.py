from django.urls import resolve
from django.test import TestCase
from app.controllers.base import index
from app.models import Enquiry, School
from django.urls import reverse
from django.conf import settings
from sso.models import User


class HomePageTest(TestCase):
    def setUp(self):
        settings.DEBUG = True
        School.objects.create(id=1, school_name='school1', mainlevel_code='SECONDARY')

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'app/home/index.html')

    def test_should_be_able_to_search_psle(self):
        response = self.client.get('/schools/', data={'score': '200'})
        self.assertTemplateUsed(response, 'app/school/school_list.html')

    def test_should_not_be_able_to_search_psle(self):
        response = self.client.get('/schools/', data={'score': '-1'})
        self.assertRedirects(response, '/')

    def test_should_be_able_to_open_school_detail(self):
        response = self.client.get(reverse('app:school_detail', kwargs={'school_id': 1}))
        self.assertContains(response, 'school1')

    def test_should_not_be_able_to_open_school_detail(self):
        response = self.client.get(reverse('app:school_detail', kwargs={'school_id': 999}))
        self.assertEqual(response.status_code, 404)


class ContactUsTest(TestCase):
    def test_should_be_able_to_create_enquiry(self):
        page = self.client.get(reverse('app:contact_us'))
        token = page.context.get("csrf_token")
        self.client.post(
            reverse('app:contact_us'),
            data={'name': 'kevin', 'email': 'kevin@kevin.com', 'message': 'hello', 'csrf_token': token}
        )
        self.assertEqual(Enquiry.objects.all().count(), 1)

    def test_should_not_be_able_to_create_enquiry(self):
        self.assertEqual(Enquiry.objects.all().count(), 0)
        page = self.client.get(reverse('app:contact_us'))
        token = page.context.get("csrf_token")
        self.client.post(
            reverse('app:contact_us'),
            data={'name': 'kevin', 'email': 'INVALID EMAIL', 'message': 'hello2', 'csrf_token': token}
        )
        self.assertEqual(Enquiry.objects.all().count(), 0)


class BookmarkTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='kevin', password='secret')

    def test_should_not_able_to_access_and_add_callback(self):
        response = self.client.get(reverse('app:bookmark_list'))
        self.assertRedirects(response, reverse('sso:login') + '?next=' + reverse('app:bookmark_list'))

    def test_should_be_able_to_access(self):
        self.client.login(username='kevin', password='secret')
        response = self.client.get(reverse('app:bookmark_list'))
        self.assertTemplateUsed(response, 'app/bookmark/index.html')


class AdminTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='kevin', password='secret')
        User.objects.create_user(username='kevinadmin', password='secret', is_superuser=True)

    def test_admin_should_be_able_to_access(self):
        self.client.login(username='kevinadmin', password='secret')
        response = self.client.get(reverse('app:admin'))
        self.assertTemplateUsed(response, 'app/admin_base.html')

    def test_user_should_not_be_able_to_access(self):
        self.client.login(username='kevin', password='secret')
        response = self.client.get(reverse('sso:login'))
        self.assertRedirects(response, reverse('sso:login') + '?next=' + reverse('app:admin'))

    def test_public_user_should_not_be_able_to_access(self):
        response = self.client.get(reverse('app:admin'))
        self.assertRedirects(response, reverse('sso:login') + '?next=' + reverse('app:admin'))
