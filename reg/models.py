
from __future__ import unicode_literals
from django import forms
from django.db import models


gender = (
    ('Male', 'Male'), #(what to be entered, what to be shown)
    ('Female', 'Female'),
)


class College(models.Model):
    college_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    registration_no = models.IntegerField()

    class Meta:
        db_table = 'college'

    def __str__(self):
        return (self.name + " - " + str(self.college_id))



class Student(models.Model):
    voter_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=6,choices=gender,default='Male')
    dob = models.DateField()
    disability = models.CharField(max_length=50)
    college_id = models.CharField(max_length=9)
    college_name = models.ForeignKey(College, on_delete=models.CASCADE)
    citizenship_no = models.CharField(max_length=20)
    photo = models.FileField(upload_to='student-photo')
    is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'student'

    def __str__(self):
        return (str(self.voter_id)+'    |    '+self.name+'    |    '+self.citizenship_no)



class Election(models.Model):
    election_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    year = models.DateField()  # This field type is a guess.

    class Meta:
        db_table = 'election'

    def __str__(self):
        return  (self.name + str(self.year))


class Party(models.Model):
    party_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    registration_no = models.IntegerField()
    symbol = models.FileField(upload_to='party-symbol')

    class Meta:
        db_table= 'party'

    def __str__(self):
        return self.party_id


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    post_name = models.CharField(max_length=30, unique=True)
    post_election = models.ForeignKey(Election, on_delete=models.CASCADE)

    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.post_name


class Candidate(models.Model):
    voter_id = models.IntegerField()
    candidate_id = models.AutoField(primary_key=True)
    party_id = models.ForeignKey(Party, on_delete=models.CASCADE)
    election_id = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    college_id = models.CharField(max_length=9)
    votes = models.IntegerField(default=0)
    # symbol = models.FileField(upload_to='candidate-symbol')
    # is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'candidate'

    def __str__(self):
        return (str(self.candidate_id)+'    |    '+str(self.post)+'    |    '+str(self.party_id))



class WinnerReport(models.Model):
    post = models.CharField(primary_key=True,max_length=50)
    candidate_id = models.IntegerField()
    votes = models.IntegerField()
    election_id = models.IntegerField()

    class Meta:
        db_table = 'winner_report'

    def __str__(self):
        return (str(self.candidate_id)+'    |    '+str(self.post)+'    |    '+str(self.votes))