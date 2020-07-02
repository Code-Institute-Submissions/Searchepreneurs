from django import forms
from .models import Review


# Forms for the 'review' app


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = {'rating',
                  'review_title',
                  'review_description',
                  'review_image'}
