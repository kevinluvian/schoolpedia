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
            'url_address',
            'address',
            'postal_code',
            'telephone_no',
            'telephone_no_2',
            'fax_no',
            'fax_no_2',
            'email_address',
            'mrt_desc',
            'bus_desc',
            'principal_name',
            'first_vp_name',
            'second_vp_name',
            'third_vp_name',
            'fourth_vp_name',
            'fifth_vp_name',
            'visionstatement_desc',
            'missionstatement_desc',
            'philosophy_culture_ethos',
            'dgp_code',
            'zone_code',
            'cluster_code',
            'type_code',
            'nature_code',
            'session_code',
            'mainlevel_code',
            'sap_ind',
            'autonomous_ind',
            'gifted_ind',
            'ip_ind',
            'mothertongue1_code',
            'mothertongue2_code',
            'mothertongue3_code',
            'special_sdp_offered',
        )


class EnquiryAnswerForm(forms.ModelForm):
    class Meta:
        model = EnquiryAnswer
        fields = ('answer',)
