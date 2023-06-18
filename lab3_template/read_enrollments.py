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
print("1. Info about user David from Learner")
learner_david = Learner.objects.get(first_name="David")
print(learner_david.user_ptr.first_name, learner_david.user_ptr.last_name, learner_david.user_ptr.dob)
print()

print("2. Info about learner David from User")
user_david = User.objects.get(first_name="David")
print(user_david.learner.occupation, user_david.learner.social_link)
print()

print("3. Get all learners for intro to python course.")
course_python = Course.objects.get(name__contains="Python")
print(course_python.learners.all())
print()

print("4. Occupation list for courses taught by Yan")
courses_yan = Course.objects.filter(instructors__first_name="Yan")
yan_course_occupations = set()
for course in courses_yan:
    for learner in course.learners.all():
        yan_course_occupations.add(learner.occupation)
print(yan_course_occupations)
print()

print("5. which courses developer learners enrolled in, in Aug, 2020")
aug20_developer_courses = Course.objects.filter(
    learners__occupation="developer",
    enrollment__date_enrolled__month=8,
    enrollment__date_enrolled__year=2020
).distinct()
# print(Course.objects.get(name__contains="Cloud").enrollment_set.all()[0].date_enrolled.month)
print(aug20_developer_courses)

print("5. book solution")
enrollments = Enrollment.objects.filter(date_enrolled__month=8, date_enrolled__year=2020, learner__occupation="developer")
courses_for_developers = set()
for enrollment in enrollments:
    course = enrollment.course
    courses_for_developers.add(course.name)
print(courses_for_developers)