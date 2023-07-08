from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic, View
from django.http import Http404

# Custom class-based views here.
# compare to function-based views commented out below.
# class CourseListView(View):
#     def get(self, request):
#         context = {}
#         course_list = Course.objects.order_by('-total_enrollment')[:10]
#         context['course_list'] = course_list
#         return render(request, 'onlinecourse/course_list.html', context)

class EnrollView(View):
    def post(self, request, *args, **kwargs):
        course_id = kwargs.get('pk')
        course = get_object_or_404(Course, pk=course_id)
        course.total_enrollment += 1
        course.save()
        return HttpResponseRedirect(reverse(viewname='onlinecourse:course_details', args=(course.id,)))

# class CourseDetailsView(View):
#     def get(self, request, *args, **kwargs):
#         context = {}
#         course_id = kwargs.get('pk')
#         try:
#             course = Course.objects.get(pk=course_id)
#             context['course'] = course
#             return render(request, 'onlinecourse/course_detail.html', context)
#         except Course.DoesNotExist:
#             raise Http404("No course matches the given id.")

############# Generic Views ###########################
class CourseListView(generic.ListView):
    # which template should be used for rendering?
    template_name = 'onlinecourse/course_list.html'
    # which key should be listed from the context dict?
    context_object_name = 'course_list'

    # override get_queryset() so that only top 10 are listed.
    def get_queryset(self):
        courses = Course.objects.order_by('-total_enrollment')[:10]
        return courses

class CourseDetailsView(generic.DetailView):
    # for DetailView, need to specify model and template_name
    model = Course
    template_name = 'onlinecourse/course_detail.html'


############ Function based views #####################3

# Function-based course list view
# def popular_course_list(request):
#    context = {}
#    if request.method == 'GET':
#        course_list = Course.objects.order_by('-total_enrollment')[:10]
#        context['course_list'] = course_list
#        return render(request, 'onlinecourse/course_list_no_css.html', context)

# Function-based course_details view
# def course_details(request, course_id):
#    context = {}
#    if request.method == 'GET':
#        try:
#            course = Course.objects.get(pk=course_id)
#            context['course'] = course
#            return render(request, 'onlinecourse/course_detail.html', context)
#        except Course.DoesNotExist:
#            raise Http404("No course matches the given id.")

# Function-based enroll view
# def enroll(request, course_id):
#    if request.method == 'POST':
#       course = get_object_or_404(Course, pk=course_id)
#       # Create an enrollment
#       course.total_enrollment += 1
#       course.save()
#       return HttpResponseRedirect(reverse(viewname='onlinecourse:course_details', args=(course.id,)))
