from django.test import TestCase
from .models import FacebookPost

class FacebookPostTestCase(TestCase):
    
    def setUp(self):
        FacebookPost.objects.create(post_text='This is tested text')
        
    def test_facebook_post_accurate(self):
        """Should check any inner or model error here is occured!"""
        post = FacebookPost.objects.get(post_text='This is tested text')
        self.assertEqual(post, 'This is tested text')

