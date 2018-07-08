from django.contrib import admin

from .models import Student, Candidate, College, Party, Post, Election, WinnerReport
# Register your models here.



admin.site.register(Student)
admin.site.register(Candidate)
admin.site.register(College)
admin.site.register(Party)
admin.site.register(Post)
admin.site.register(Election)
admin.site.register(WinnerReport)


