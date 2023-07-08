from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic
from django.http import Http404

# Create your views here.
def popular_course_list(request):
    context = {}
    if request.method == 'GET':
        # get top 10 courses from Course model.
        course_list = Course.objects.order_by('-total_enrollment')[:10]
        # add to context dict to be passed into template
        context['course_list'] = course_list
        return render(request, 'onlinecourse/course_list.html', context)

def enroll(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, pk=course_id)
        course.total_enrollment += 1
        course.save()
        # always return HttpResponseRedirect after successfully
        # dealing with POST data.
        # here, reverse function generates endpoint URL for popular_course_list.
        return HttpResponseRedirect(reverse(viewname='onlinecourse:course_details', args=(course.id,)))

def course_details(request, course_id):
    context = {}
    if request.method == 'GET':
        try:
            course = Course.objects.get(pk=course_id)
            context['course'] = course
            return render(request, 'onlinecourse/course_detail.html', context)
        except Course.DoesNotExist:
            raise Http404("No course matches the given id.")