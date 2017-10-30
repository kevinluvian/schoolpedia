from django.http import HttpResponseRedirect
from django.shortcuts import (
    get_object_or_404,
    render
)
from django.urls import reverse
from app.models import (
    School, Bookmark, SchoolComment, ReportComment
)
from app import utils
from django.contrib.auth.decorators import login_required


@login_required
def bookmark(request, school_id):
    latitude, longitude, has_coordinate = utils.get_coordinate_from_request(request)
    user = request.user
    school = get_object_or_404(School, id=school_id)
    new_bookmark = Bookmark(
        user=user,
        school=school
    )
    new_bookmark.save()
    if has_coordinate:
        redirect_url = '{}?latitude={}&longitude={}'.format(reverse('app:school_list'), latitude, longitude)
    else:
        redirect_url = reverse('app:school_list')
    return HttpResponseRedirect(redirect_url)


@login_required
def unbookmark(request, school_id):
    latitude, longitude, has_coordinate = utils.get_coordinate_from_request(request)
    user = request.user
    school = get_object_or_404(School, id=school_id)
    try:
        bookmark = Bookmark.objects.get(user=user, school=school)
        bookmark.delete()
    except Bookmark.DoesNotExist:
        pass
    if has_coordinate:
        redirect_url = '{}?latitude={}&longitude={}'.format(reverse('app:school_list'), latitude, longitude)
    else:
        redirect_url = reverse('app:school_list')
    return HttpResponseRedirect(redirect_url)


@login_required
def bookmark_list(request):
    user = request.user
    bookmark_list = Bookmark.objects.filter(user=user)
    return render(request, 'app/bookmark/index.html', {'bookmark_list': bookmark_list})


def report_comment(request, comment_id):
    comment = get_object_or_404(SchoolComment, id=comment_id)
    try:
        new_report = ReportComment.objects.get(reported_by=request.user, comment=comment)
    except ReportComment.DoesNotExist:
        new_report = ReportComment(
            reported_by=request.user,
            comment=comment
        )
        new_report.save()
    return HttpResponseRedirect(reverse('app:school_detail', kwargs={'school_id': comment.school.id}))


def change_password(request):
    pass


def change_user_info(request):
    pass


def logout(request):
    pass
