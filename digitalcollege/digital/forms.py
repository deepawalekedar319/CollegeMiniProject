from django import forms

class EmailSendForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	to = forms.EmailField()
	Description = forms.CharField(required = False,widget = forms.Textarea)

class SendQueryForm(forms.Form):
	query = forms.CharField(widget = forms.Textarea);

class UpdateForm(forms.Form):
	updates = forms.CharField(widget = forms.Textarea);

class CreateFile(forms.Form):
	notes = forms.CharField(widget = forms.Textarea);