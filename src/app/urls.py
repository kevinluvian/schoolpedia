from django.conf.urls import url
from app.views import scheduler, base
from app.views import public_view, user_view, admin_view

app_name = 'app'
urlpatterns = [
    url(r'^$', base.index, name='home'),
    url(r'^scheduler/run$', scheduler.update_school_data),

    # public views
    url(r'^schools/$', public_view.school_list, name='school_list'),
    url(r'^schools/(?P<school_id>\d+)/$', public_view.school_detail, name='school_detail'),
    url(r'^schools/(?P<school_id>\d+)/add_to_comparison/$', public_view.add_to_comparison, name='add_to_comparison'),
    url(r'^schools/(?P<school_id>\d+)/remove_from_comparison/$', public_view.remove_from_comparison, name='remove_from_comparison'),

    url(r'^compare_schools/$', public_view.compare_schools, name='compare_schools'),
    url(r'^contact_us/$', public_view.contact_us, name='contact_us'),

    # user views
    url(r'^comments/(?P<comment_id>\d+)/report/$', user_view.report_comment, name='report_comment'),

    url(r'^bookmarks/$', user_view.bookmark_list, name='bookmark_list'),
    url(r'^bookmarks/(?P<school_id>\d+)/bookmark/$', user_view.bookmark, name='bookmark'),
    url(r'^bookmarks/(?P<school_id>\d+)/unbookmark/$', user_view.unbookmark, name='unbookmark'),

    # admin views
    url(r'^admin/$', admin_view.index, name='admin'),
    url(r'^admin/users/$', admin_view.user_list, name='admin_users'),
    url(r'^admin/users/(?P<user_id>\d+)/$', admin_view.user_detail, name='admin_users_detail'),
    url(r'^admin/users/(?P<user_id>\d+)/block/$', admin_view.block_user, name='admin_block_user'),
    url(r'^admin/users/(?P<user_id>\d+)/unblock/$', admin_view.unblock_user, name='admin_unblock_user'),

    url(r'^admin/comments/(?P<comment_id>\d+)/delete/$', admin_view.delete_comment, name='admin_delete_comment'),

    url(r'^admin/schools/$', admin_view.school_list, name='admin_schools'),
    url(r'^admin/schools/(?P<school_id>\d+)/$', admin_view.school_detail, name='admin_schools_detail'),
    url(r'^admin/schools/(?P<school_id>\d+)/edit/$', admin_view.edit_school, name='admin_edit_school'),
    url(r'^admin/schools/(?P<school_id>\d+)/delete/$', admin_view.delete_school, name='admin_delete_school'),

    url(r'^admin/enquiries/$', admin_view.enquiry_list, name='admin_enquiries'),
    url(r'^admin/enquiries/(?P<enquiry_id>\d+)/$', admin_view.enquiry_detail, name='admin_enquiries_detail'),

    url(r'^admin/reports/$', admin_view.report_list, name='admin_reports'),
    url(r'^admin/reports/(?P<report_id>\d+)/ignore/$', admin_view.ignore_report, name='admin_ignore_report'),
]
