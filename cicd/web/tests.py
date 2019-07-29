from django.test import TestCase, Client


class WebAbbTest(TestCase):
    def test_index(self):
        response = self.client.get('/web/')
        self.assertEqual(response.status_code, 200)
