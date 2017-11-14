from django.conf.urls import url
from app.controllers import scheduler, base
from app.controllers.public_view import PublicView
from app.controllers.user_view import UserView
from app.controllers.admin_view import AdminView


app_name = 'app'
urlpatterns = [
    url(r'^$', base.index, name='home'),
    url(r'^scheduler/run$', scheduler.update_school_data, name='run_scheduler'),

    # public controllers
    url(r'^schools/$', PublicView.school_list, name='school_list'),
    url(r'^schools/(?P<school_id>\d+)/$', PublicView.school_detail, name='school_detail'),
    url(r'^schools/(?P<school_id>\d+)/add_to_comparison/$', PublicView.add_to_comparison, name='add_to_comparison'),
    url(r'^schools/(?P<school_id>\d+)/remove_from_comparison/$', PublicView.remove_from_comparison, name='remove_from_comparison'),

    url(r'^compare_schools/$', PublicView.compare_schools, name='compare_schools'),
    url(r'^contact_us/$', PublicView.contact_us, name='contact_us'),

    # user controllers
    url(r'^profile/$', UserView.profile, name='profile'),
    url(r'^change_password/$', UserView.change_password, name='change_password'),
    url(r'^change_profile/$', UserView.change_profile, name='change_profile'),
    url(r'^deactivate_account/$', UserView.deactivate_account, name='deactivate_account'),

    url(r'^comments/(?P<comment_id>\d+)/report/$', UserView.report_comment, name='report_comment'),

    url(r'^bookmarks/$', UserView.bookmark_list, name='bookmark_list'),
    url(r'^bookmarks/(?P<school_id>\d+)/bookmark/$', UserView.bookmark, name='bookmark'),
    url(r'^bookmarks/(?P<school_id>\d+)/unbookmark/$', UserView.unbookmark, name='unbookmark'),

    # admin controllers
    url(r'^admin/$', AdminView.index, name='admin'),
    url(r'^admin/users/$', AdminView.user_list, name='admin_users'),
    url(r'^admin/users/(?P<user_id>\d+)/$', AdminView.user_detail, name='admin_users_detail'),
    url(r'^admin/users/(?P<user_id>\d+)/block/$', AdminView.block_user, name='admin_block_user'),
    url(r'^admin/users/(?P<user_id>\d+)/unblock/$', AdminView.unblock_user, name='admin_unblock_user'),

    url(r'^admin/scheduler_logs/$', AdminView.scheduler_log_list, name='admin_schedulers'),
    url(r'^admin/scheduler_logs/(?P<log_id>\d+)/$', AdminView.scheduler_log_detail, name='admin_schedulers_detail'),

    url(r'^admin/comments/(?P<comment_id>\d+)/delete/$', AdminView.delete_comment, name='admin_delete_comment'),

    url(r'^admin/schools/$', AdminView.school_list, name='admin_schools'),
    url(r'^admin/schools/(?P<school_id>\d+)/$', AdminView.school_detail, name='admin_schools_detail'),
    url(r'^admin/schools/(?P<school_id>\d+)/edit/$', AdminView.edit_school, name='admin_edit_school'),
    url(r'^admin/schools/(?P<school_id>\d+)/delete/$', AdminView.delete_school, name='admin_delete_school'),

    url(r'^admin/enquiries/$', AdminView.enquiry_list, name='admin_enquiries'),
    url(r'^admin/enquiries/(?P<enquiry_id>\d+)/$', AdminView.enquiry_detail, name='admin_enquiries_detail'),

    url(r'^admin/reports/$', AdminView.report_list, name='admin_reports'),
    url(r'^admin/reports/(?P<report_id>\d+)/ignore/$', AdminView.ignore_report, name='admin_ignore_report'),
]
