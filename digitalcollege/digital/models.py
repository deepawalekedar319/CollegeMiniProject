from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import datetime

class StudentModel(models.Model):
	firstname = models.CharField(max_length = 260)
	lastname = models.CharField(max_length = 260)
	stu = models.ForeignKey(User,related_name='digital_library',on_delete=models.CASCADE)
	rollno = models.IntegerField()
	attendence = models.FloatField()
	stu_email = models.EmailField()
	micro_email = models.EmailField()
	branch = models.CharField(max_length = 10)
	block = models.CharField(max_length = 5)
	stu_year = models.IntegerField()
	stu_sem = models.IntegerField()

	def __str__(self):
		return self.firstname


class DepartmentModel(models.Model):
	depts = models.CharField(max_length = 12)

	def __str__(self):
		return self.depts

class YearModel(models.Model):
	hod = models.CharField(max_length = 120)
	hod_email = models.EmailField()
	hod_pno = models.CharField(max_length=12)
	hod_dept = models.CharField(max_length=120)
	def __str__(self):
		return str(self.hod)

class FacuiltyModel(models.Model):
	dept = 	models.CharField(max_length=120)
	f_year = models.IntegerField()
	name = models.CharField(max_length = 120)
	email = models.EmailField()
	pno = models.CharField(max_length = 12)

	def __str__(self):
		return self.name


class OuNotesModel(models.Model):
	dept = 	models.ForeignKey(DepartmentModel,related_name='ou_dept',on_delete=models.CASCADE)
	oufiles = models.FileField(null=True,default='no pdf')
	pdfname = models.CharField(max_length=120)

	def __str__(self):
		return self.pdfname

class PreviousPapersModel(models.Model):
	dept = 	models.ForeignKey(DepartmentModel,related_name='previous_images_dept',on_delete=models.CASCADE)
	year = models.IntegerField()
	slug = models.SlugField(max_length = 264)
	paper_year = models.IntegerField()
	subject = models.CharField(max_length = 60)
	desc = models.TextField()
	image = models.ImageField(null=True,default='no image')

	def __str__(self):
		return self.subject

	def get_absolute_url(self):
		return reverse('image',args=[self.slug,])
 
class GallaryModel(models.Model):
	title = models.CharField(max_length=256)
	slug = models.SlugField(max_length = 264,unique_for_date = "publish")
	image = models.ImageField(upload_to='images')
	desc = models.TextField()
	publish = models.DateTimeField(default = timezone.now)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	
	def __str__(self):
		return self.title

	def get_absolute_image(self):
		return reverse('gallary',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

class LibraryModel(models.Model):
	stu = models.ForeignKey(User,related_name='digital_college',on_delete=models.CASCADE)
	rollno = models.IntegerField()
	book_name = models.CharField(max_length = 120)
	borrowed_date = models.DateTimeField(default = timezone.now)
	valid_date = models.DateTimeField()
	total_books = models.IntegerField()
	borrowed_books = models.IntegerField()
	
	def __str__(self):
		return str(self.stu) 

class TimeTableAndSyllabusModel(models.Model):
	timetable = models.FileField(null=True,default='no timetable')
	syllabus = models.FileField(null=True,default='no syllabus')

	def __str__(self):
		return str(self.timetable)

class ResultModel(models.Model):
	dept = models.ForeignKey(DepartmentModel,related_name='results_model',on_delete=models.CASCADE)
	rollno = models.IntegerField(primary_key=True)
	result = models.FileField(null=True,default='no result')

	def __str__(self):
		return str(self.rollno)