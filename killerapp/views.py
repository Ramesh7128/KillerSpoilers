from django.shortcuts import render

# from calcapp.models import Calculations
# from channels import Group
import json
# from channels.sessions import channel_session
from django.views.decorators.csrf import csrf_exempt

def homepage(request):
	return render(request, 'index.html', {})

def subscribe(request):
	if request.method == 'POST':
		token = request.POST.get('stripeToken')
		name = request.POST.get('InputName')
		phoneno = request.POST.get('Inputphno')
		tvshow = request.POST.get('InputTvshow')
		print token, "token", name, "name", phoneno, "tvshow", tvshow
		
		

	return render(request, 'subscribe.html', {})