from django.db import models
from django.contrib.auth.models import User

class ins_or_stu(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    ins = models.IntegerField()

class Courses(models.Model):
    title = models.CharField(max_length=100)
    des = models.CharField(max_length=400)
    image = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Lessons(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField()
    content = models.TextField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Enrollment(models.Model):
    date_enrolled = models.DateField(auto_now_add=True)
    course = models.ForeignKey(Courses, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    rating  = models.IntegerField()

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.name

class online_course(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    instructor_id = models.ForeignKey(Instructor, on_delete= models.CASCADE)

class Question(models.Model):
    text = models.TextField()
    grade = models.IntegerField()
    lesson_id = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class Submission(models.Model):
    enrollment_id = models.ForeignKey(Enrollment, on_delete=models.CASCADE)

class Choice(models.Model):
    choice = models.CharField(max_length=400, blank=True, null=True)
    is_correct = models.IntegerField()
    question_id = models.ForeignKey(Question, on_delete= models.CASCADE)
    def __str__(self):
        return self.choice

class userchoices(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.choice

class online_course_submmision(models.Model):
    submission_id = models.ForeignKey(Submission, on_delete= models.CASCADE)
    choice_id = models.ForeignKey(Choice, on_delete=models.CASCADE)

class Learner(models.Model):
    name = models.CharField(max_length= 100)
    occupation = models.CharField(max_length=100)
    social = models.URLField()
    user = models.ForeignKey(User, on_delete= models.CASCADE)