from django.shortcuts import render, render_to_response
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from django.template.context_processors import csrf
from .fusioncharts import FusionCharts

from .models import *

# Create your views here.

def index(request):
	t=loader.get_template('index.html')
	context = {}
	return HttpResponse(t.render(context))



def party(request):
	message="Fill Up- Party Form"

	if request.method=="POST":
		t = loader.get_template('index.html')
		form = forms.PartyForm(request.POST, request.FILES)
		if form.is_valid():
			saved_form = form.save()
			context = {'form_number': saved_form.pk, 'message': "Form is received. Form ID is:"}
			return HttpResponse(t.render(context))
	else:
		form = forms.PartyForm()
		token = {}
		token.update(csrf(request))

	token = {'form': form, 'form_url': 'party', 'message': message}
	return render(request, 'forms.html', token)


def college(request):
	message="Fill Up- College Form"

	if request.method=="POST":
		t = loader.get_template('index.html')
		form = forms.CollegeForm(request.POST)
		if form.is_valid():
			saved_form = form.save()
			context = {'form_number': saved_form.pk, 'message': "Form is received. Form ID is"}
			return HttpResponse(t.render(context))
	else:
		form = forms.CollegeForm()
		token = {}
		token.update(csrf(request))

	token = {'form': form, 'form_url': 'college', 'message': message}
	return render(request, 'forms.html', token)


def post(request):
	message="Fill Up- Post Form"

	if request.method=="POST":
		t = loader.get_template('index.html')
		form = forms.PostForm(request.POST)
		if form.is_valid():
			saved_form = form.save()
			context = {'form_number': saved_form.pk, 'message': "Form is received. Form ID is"}
			return HttpResponse(t.render(context))
	else:
		form = forms.PostForm()
		token = {}
		token.update(csrf(request))

	token = {'form': form, 'form_url': 'post', 'message': message}
	return render(request, 'forms.html', token)



def election(request):
	message="Fill Up- Election Form"

	if request.method=="POST":
		t = loader.get_template('index.html')
		form = forms.ElectionForm(request.POST)
		if form.is_valid():
			saved_form = form.save()
			context = {'form_number': saved_form.pk, 'message': "Form is received. Form ID is"}
			return HttpResponse(t.render(context))
	else:
		form = forms.ElectionForm()
		token = {}
		token.update(csrf(request))

	token = {'form': form, 'form_url': 'election', 'message': message}
	return render(request, 'forms.html', token)




def student(request):
	message = "Fill Up - Student Form"
	if request.method == "POST":
		t=loader.get_template('index.html')
		form = forms.StudentForm(request.POST, request.FILES)
		if form.is_valid():
			saved_form=form.save()
			context = { 'form_number': saved_form.pk, 'message': "Form is received. Form ID is" }
			return HttpResponse(t.render(context))

	else:
		form = forms.StudentForm()
		token={}
		token.update(csrf(request))

	token = {'form':form, 'form_url':'student', 'message':message}
	return render(request, 'forms.html', token)


def candidate(request):
	message = "Fill Up - Candidate Form"
	if request.method == "POST":
		t=loader.get_template('index.html')
		form = forms.CandidateForm(request.POST, request.FILES)
		if form.is_valid():
			obj=form.save(commit=False)
			v_id=obj.voter_id
			if Student.objects.all().filter(voter_id = v_id).exists():
				saved_form=form.save()
				context = { 'form_number': saved_form.pk, 'message': "Form is received. Form ID is" }
				return HttpResponse(t.render(context))
			else:
				message = "You have not been registered as student. Get registered  before applying for the candidate."
		else:
			message="Registration Failed. Please try again."
	else:
		form= forms.CandidateForm()
		token={}
		token.update(csrf(request))

	token = {'form':form, 'message':message, 'form_url':'candidate'}
	return render(request, 'forms.html', token)



def viewdata(request):
	if request.method == "POST":
		t=loader.get_template('formdetails.html')
		querynum=request.POST.get("citz", "")
		if Student.objects.all().filter(citizenship_no = querynum).exists():
			result = Student.objects.all().filter(citizenship_no = querynum).values()
			img = result[0].get("photo")
			record=1
		else:
			result = "Your data is not in the database."
			img = ""
			record = 0
		context = { 'result':result, 'img': img, 'record':record}
		return HttpResponse(t.render(context))

	else:
		t=loader.get_template('viewMyData.html')
		context={}
		context.update(csrf(request))
		return HttpResponse(t.render(context))



def viewresult(request):	
	bar2 = bar3 = bar4 = bar5 = bar6 = FusionCharts("","","","","","","")
	ex = ["ex2", "ex3", "ex4", "ex5", "ex6"]
	bar = [bar2, bar3, bar4, bar5, bar6]
	chart = ["chart2", "chart3", "chart4", "chart5", "chart6"]
	color = ["#FFD904", "#D2100A", "#13BB0D", "#0D79BB", "#B51DDA"]
	#red, yellow, green, blue, purple

	colleges = College.objects.all()
	posts = Post.objects.all()
	parties = Party.objects.all()

	for college in colleges:
		query = 'SELECT s.name,s.voter_id, q.post, q.party_id_id, q.name as partyname FROM student s INNER JOIN (SELECT c.voter_id, c.party_id_id, w.votes, w.post, c.name FROM (SELECT p.name, d.* FROM party p INNER JOIN candidate d ON p.party_id = d.party_id_id)c INNER JOIN winner_report w ON c.candidate_id = w.candidate_id)q ON s.voter_id = q.voter_id'
		dataSource = {}
		dataSource['chart'] = { 
				"caption": "FSU Election - 2017", 
				"subCaption": college.name,
				"xAxisName": "Candidates",
				"yAxisName": "Votes",
				"theme": "fint",
				"bgColor": "#ffffff",
				"borderAlpha": "0",
				"showLegend" : "1",
				"placevaluesInside": "0",
				"rotatevalues": "0",
			}

		dataSource['data'] = []
		for key in WinnerReport.objects.raw(query):
		  	data = {}
		  	data['label'] = str(key.name)+' ('+str(key.post) +') '
			data['value'] = key.votes
			data['color'] = color[key.party_id_id-1]
			data['tooltext'] = "<div><b>$label</b><br/>Votes : <b>$value</b><br/>Party : <b>"+ key.partyname +"</b></div>"
		 	dataSource['data'].append(data)
		 	party = key.party_id_id
		 	
		column2D = FusionCharts("column2D", "ex1" , "500", "250", "chart1", "json", dataSource)
		
		for i in range(5):
			for post in Post.objects.raw('SELECT id,post_name FROM post WHERE id=%s',[i+1]):
				dataSource = {}
				
				dataSource['data'] = []
				for key in Candidate.objects.raw('SELECT s.name, q.votes, q.candidate_id, q.party_id_id, q.partyname FROM student s INNER JOIN (SELECT c.*, p.name as partyname FROM candidate c INNER JOIN party p ON c.party_id_id = p.party_id WHERE c.post_id=%s order by c.votes desc limit 3)q ON s.voter_id = q.voter_id',[i+1]):
					data = {}
					data['label'] = key.name
					data['value'] = key.votes
					data['color'] = color[key.party_id_id-1]
					data['tooltext'] = "<div><b>$label</b><br/>Votes : <b>$value</b><br/>Party : <b>"+ key.partyname +"</b></div>"
					dataSource['data'].append(data)

				dataSource['chart'] = { 
					"caption": "FSU Election - 2017" + ' (' + college.name + ' )', 
					"subCaption": post.post_name,
					"xAxisName": "Candidates",
					"yAxisName": "Votes",
					"theme": "fint",
					"bgColor": "#ffffff",
					"borderAlpha": "0",
					"showLegend" : "1",
					"placevaluesInside": "0",
					"rotatevalues": "0",
				}
			bar[i] = FusionCharts("bar2D", ex[i] , "500", "250", chart[i], "json", dataSource)
	

	return render(request, 'viewResult.html', {'output1': column2D.render(), 'output2':bar[0].render(), 'output3':bar[1].render()
		, 'output4':bar[2].render(), 'output5':bar[3].render(), 'output6':bar[4].render(), 'zipped':zip(parties,color)})


