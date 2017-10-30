from django import forms
from app.models import Enquiry, SchoolComment


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ('name', 'email', 'message')


class CommentForm(forms.ModelForm):
    class Meta:
        model = SchoolComment
        fields = ('rating', 'message',)