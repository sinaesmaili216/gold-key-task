from django.test import TestCase

from content.models import Content


class DeleteManagementTest(TestCase):
    def setUp(self):
        self.content_id = Content.objects.create(title='title', description='description', image='img.jpg',
                                                 payment_status='رایگان').id

    def test_delete_content(self):
        response = self.client.post(f'http://127.0.0.1:8000/delete/{self.content_id}')
        self.assertEqual(response.status_code, 302)
