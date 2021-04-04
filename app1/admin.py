from django.contrib import admin
from .models import Courses,Lessons,Question,Enrollment,Submission,online_course,online_course_submmision,Instructor,Choice,Learner,ins_or_stu
# Register your models here.
from .models import userchoices

admin.site.register(userchoices)



admin.site.register(Courses)
admin.site.register(Instructor)
admin.site.register(Enrollment)
admin.site.register(Lessons)
admin.site.register(Question)
admin.site.register(online_course_submmision)
admin.site.register(online_course)
admin.site.register(Submission)
admin.site.register(Choice)
admin.site.register(Learner)
admin.site.register(ins_or_stu)