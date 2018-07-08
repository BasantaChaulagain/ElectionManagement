from django import forms
from . import models

class StudentForm(forms.ModelForm):
	class Meta:
		model=models.Student
		fields=['voter_id','name','sex','dob','disability','college_id','college_name','citizenship_no','photo']


class CandidateForm(forms.ModelForm):
	class Meta:
		model=models.Candidate
		fields=['voter_id','party_id','post','college_id','candidate_id','election_id']


class PartyForm (forms.ModelForm):
	class Meta:
		model=models.Party
		fields=['name','registration_no','symbol']


class CollegeForm (forms.ModelForm):
	class Meta:
		model=models.College
		fields=['name','location','registration_no']


class PostForm (forms.ModelForm):
	class Meta:
		model=models.Post
		fields=['post_name','post_election']

class ElectionForm (forms.ModelForm):
	class Meta:
		model=models.Election
		fields=['name','year']