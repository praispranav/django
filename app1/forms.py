from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import ins_or_stu, online_course, Instructor , Learner
from .models import userchoices


class userchoiceform(ModelForm):
    class Meta:
        model = userchoices
        fields = '__all__'

class instructorform(ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'

class signup_form(ModelForm):
    class Meta:
        model = User
        fields= '__all__'

class online_course_form(ModelForm):
    class Meta:
        model = online_course
        fields= '__all__'

class profilesetupform(ModelForm):
    class Meta:
        model = ins_or_stu
        fields = '__all__'

class learnerform(ModelForm):
    class Meta:
        model = Learner
        fields = '__all__'