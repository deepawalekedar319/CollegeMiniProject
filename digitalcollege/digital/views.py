from django.shortcuts import render,get_object_or_404 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from digital.forms import EmailSendForm,SendQueryForm,UpdateForm,CreateFile
from digital import models 

#if possible make DRBUG as False in settings.py and even add HOSTS

@login_required
def home_view(request):
	details = models.StudentModel.objects.get(id = request.user.id)
	return render(request,'digital/home.html',{'details':details})

@login_required
def attendence_view(request):
	get_id = models.StudentModel.objects.get(id = request.user.id)
	attendence = get_id.attendence
	return render(request,'digital/attendence.html',{'attendence':attendence})

@login_required
def cse_view(request):
	hod = models.YearModel.objects.filter(hod_dept__icontains="CSE")
	cse = models.FacuiltyModel.objects.filter(dept__contains='CSE')
	return render(request,'digital/cse.html',{'cse':cse,'hod':hod})

@login_required
def eee_view(request):
	hod = models.YearModel.objects.filter(hod_dept__icontains="EEE")
	eee = models.FacuiltyModel.objects.filter(dept__contains='EEE')
	return render(request,'digital/eee.html',{'eee':eee,'hod':hod})

@login_required
def ece_view(request):
	hod = models.YearModel.objects.filter(hod_dept__icontains="ECE")
	ece = models.FacuiltyModel.objects.filter(dept__contains='ECE')
	return render(request,'digital/ece.html',{'ece':ece,'hod':hod})

@login_required
def ounotes_view(request):
	pdfs = models.OuNotesModel.objects.all()
	return render(request,'digital/ounotes.html',{'pdf':pdfs})

@login_required
def search_view(request):
	query=request.GET['query']
	pdf=models.OuNotesModel.objects.filter(pdfname__icontains=query)
	return render(request,'digital/search.html',{'pdf':pdf})

@login_required
def previouspapers_view(request):
	paper_info = models.PreviousPapersModel.objects.all()
	return render(request,'digital/previous.html',{'papers':paper_info})

@login_required
def get_selected_paper_view(request,previous):
	image = get_object_or_404(models.PreviousPapersModel,slug=previous)
	return render(request,'digital/get_particular_paper.html',{'image':image})

@login_required
def previous_paper_search_view(request):
	query=request.GET['query']	
	subject=models.PreviousPapersModel.objects.filter(subject__icontains=query)
	desc=models.PreviousPapersModel.objects.filter(desc__icontains=query)
	return render(request,'digital/papersearch.html',{'subject':subject,'desc':desc})

@login_required
def gallary_view(request):
	images = models.GallaryModel.objects.all()
	return render(request,'digital/gallary.html',{'images':images})

@login_required
def get_selected_gallary_view(request,gallary,year,month,day):
	image = get_object_or_404(models.GallaryModel,slug=gallary,publish__year=year,publish__month=month,publish__day=day)
	return render(request,'digital/get_gallary_image.html',{'image':image})

@login_required
def gallary_search_view(request):
	query=request.GET['query']	
	title=models.GallaryModel.objects.filter(title__icontains=query)
	desc=models.GallaryModel.objects.filter(desc__icontains=query)
	publish=models.GallaryModel.objects.filter(publish__icontains=query)
	return render(request,'digital/searchgallaryimage.html',{'title':title,'desc':desc,'publish':publish})

def logout_view(request):
	return render(request,'digital/logout.html')

def mail_send_view(request):
	send=False
	if request.method == 'POST':
		form = EmailSendForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			subject='{}({}) has sent you an mail' .format(cd['name'],cd['email'])
			message=' {}\'s description is :\n{} '.format(cd['name'],cd['Description'])
			send_mail(subject,message,'MethodistCollege@Digitals.com',[cd['to']])
			send=True
	else :
		form = EmailSendForm()
	return render(request,'digital/sendmail.html',{'form':form,'send':send})

@login_required
def library_view(request):
	details = models.StudentModel.objects.get(id = request.user.id)
	student = models.LibraryModel.objects.filter(rollno = details.rollno)
	books = []
	for s in student:
		books.append(s.borrowed_books)
	total = sum(books)
	return render(request,'digital/library.html',{'student':student,'total':total})

@login_required
def timetable_view(request):
	timetable = models.TimeTableAndSyllabusModel.objects.all()
	for time in timetable:
		timetable = time.timetable
	return render(request,'digital/time.html',{'timetable':timetable})

@login_required
def syllabus_view(request):
	syllabus = models.TimeTableAndSyllabusModel.objects.all()
	for sylla in syllabus:
		syllabus = sylla.syllabus
	return render(request,'digital/syllabus.html',{'syllabus':syllabus})

@login_required
def profile_view(request):
	details = models.StudentModel.objects.get(id = request.user.id)
	return render(request,'digital/profile.html',{'details':details})

@login_required
def query_view(request):
	details = models.StudentModel.objects.get(id = request.user.id)
	mail = details.stu_email
	hod = models.YearModel.objects.filter(hod_dept = details.branch)
	for h in hod:
		email = h.hod_email
	send=False
	if request.method == 'POST':
		form = SendQueryForm(request.POST)
		if form.is_valid():							
			cd = form.cleaned_data
			subject='{}({}) has raise an query ' .format(details.firstname,mail)
			message=' {}\'s query is :\n{} '.format(details.firstname,cd['query'])
			send_mail(subject,message,'MethodistCollege@Digitals.com',[email])
			send=True
	else :
			form = SendQueryForm()			
	return render(request,'digital/query.html',{'form':form,'send':send})

@login_required
def update_view(request):
	details = models.StudentModel.objects.get(id = request.user.id)
	mail = details.stu_email
	hod = models.YearModel.objects.filter(hod_dept = details.branch)
	for h in hod:
		email = h.hod_email
	send=False
	if request.method == 'POST':
		form = UpdateForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			subject='{}({}) wants to update profile ' .format(details.firstname,mail)
			message=' {}\'s wants to update :\n{} '.format(details.firstname,cd['updates'])
			send_mail(subject,message,'MethodistCollege@Digitals.com',[email])
			send=True
	else :
			form = UpdateForm()		
	return render(request,'digital/update.html',{'form':form,'send':send})		

@login_required
def results_view(request):
	my_result = models.ResultModel.objects.get(rollno=request.user.id)
	result_pdf = my_result.result
	return render(request,'digital/results.html',{'result':result_pdf})

@login_required
def document_view(request):
	return render(request,'digital/document.html')

@login_required
def create_view(request):
	form = CreateFile()
	if request.method == 'POST':
		form = CreateFile(request.POST)
		print(form)
	return render(request,'digital/create.html',{'form':form})