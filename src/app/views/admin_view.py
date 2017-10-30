from django.shortcuts import render


def index(request):
    return render(request, 'app/admin_base.html')


def user_list(request):
    user_list = User.objects.all()
    return render(request, 'app/admin/admin_users.html', {'user_list': user_list})


def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'app/admin/admin_users_detail.html', {'user': user})


def block_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unblock_user(request):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def school_list(request):
    school_list = School.objects.all()
    return render(request, 'app/admin/admin_schools.html', {'school_list': school_list})


def school_detail(request, school_id):
    school = School.objects.get(id=school_id)
    return render(request, 'app/admin/admin_users_detail.html', {'school': school})


def edit_school(request):
    pass


def delete_school(request, school_id):
    school = School.objects.get(id=school_id)
    school.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def enquiry_list(request):
    enquiries_list = Enquiry.objects.all()
    return render(request, 'app/admin/admin_enquiries.html', {'enquiries_list': enquiries_list})


def enquiry_detail(request):
    enquiry = Enquiry.objects.get(id=enquiry_id)
    return render(request, 'app/admin/admin_enquiries_detail.html', {'enquiry': enquiry})


def report_list(request):
    pass


def report_detail(request):
    pass


def ignore_report(request):
    pass
