from django import forms
from app.models import Enquiry, SchoolComment, School, EnquiryAnswer


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ('name', 'email', 'message')


class CommentForm(forms.ModelForm):
    class Meta:
        model = SchoolComment
        fields = ('rating', 'message',)


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = (
            'school_name',
            'lat',
            'lng',
            'express_nonaff_lower',
            'express_nonaff_upper',
            'normal_technical_nonaff_upper',
            'normal_technical_nonaff_lower',
            'normal_academic_nonaff_upper',
            'normal_academic_nonaff_lower',
        )


class EnquiryAnswerForm(forms.ModelForm):
    class Meta:
        model = EnquiryAnswer
        fields = ('answer',)
