from django.shortcuts import render

# Create your views here.
def employmentFormPageView(request) :
	return render(request,"form.html")