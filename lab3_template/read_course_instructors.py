# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from related_objects.models import *
from datetime import date


# Your code starts from here:
print("i. courses taught by yan, through forward and backward access.")
yan_forward_courses = Course.objects.get(instructors__first_name="Yan")
print("yan_forward_courses:", yan_forward_courses)
instructor_yan = Instructor.objects.get(first_name="Yan")
yan_backward_courses = instructor_yan.course_set.all()
print("yan_backward_courses:", yan_backward_courses)

print()

print("ii. instructors of cloud app dev course.")
course_cloud = Course.objects.get(name__contains="Cloud")
print(course_cloud.instructors.all())

print()

print("iii. occupations of learners in courses taught by Yan")
for course in yan_backward_courses:
    for learner in course.learners.all():
        print("learner", learner.first_name, "has occupation", learner.occupation)