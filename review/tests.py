from django.test import TestCase
from .forms import ReviewForm


# Tests for the 'review' app


class TestReview(TestCase):

    def test_can_review_without_title(self):
        form = ReviewForm({'rating': 10,
                           'review_description': 'A review'})
        self.assertFalse(form.is_valid(), form.errors)

    def test_full_review_form_is_valid(self):
        form = ReviewForm({'rating': 10,
                           'review_title': 'Review Title',
                           'review_description': 'A review'})
        self.assertTrue(form.is_valid(), form.errors)
