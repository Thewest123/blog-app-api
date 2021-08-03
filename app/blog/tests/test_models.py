from django.test import TestCase
from django.contrib.auth import get_user_model
from blog import models
from unittest.mock import patch


def sample_user(email='test@email.com', password='testpass123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTest(TestCase):

    @patch('uuid.uuid4')
    def test_blog_file_name_uuid(self, mock_uuid):
        """Test that image is saved in the correct location"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.blog_image_file_path(None, 'myimage.jpg')

        expected_path = f'uploads/blog/{uuid}.jpg'

        self.assertEqual(expected_path, file_path)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            name='Some Tag name',
            slug='some-tag-name'
        )

        self.assertEqual(str(tag), tag.name)

    def test_category_str(self):
        """Test the category string representation"""
        category = models.Category.objects.create(
            name='Some caTEgory name',
            slug='some-category-name'
        )

        self.assertEqual(str(category), category.name)

    def test_blogpost_str(self):
        """Test the blogpost string representation"""
        models.Category.objects.create(
            name='Uncategorized',
            slug='uncategorized'
        )

        blogpost = models.BlogPost.objects.create(
            title='Sample blog post',
            slug='sample-blog-post',
            author=sample_user(),
            content='Lorem ipsum dolor sit amet'

        )

        self.assertEqual(str(blogpost), blogpost.title)
