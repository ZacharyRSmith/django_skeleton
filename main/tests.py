from django.core.urlresolvers import reverse
from django.test import TestCase

class IndexViewTests(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is the index page.')
