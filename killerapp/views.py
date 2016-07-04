from django.shortcuts import render

# from calcapp.models import Calculations
# from channels import Group
import json
# from channels.sessions import channel_session
from django.views.decorators.csrf import csrf_exempt
from killerapp.models import *
import stripe
from django.http import HttpResponseRedirect, HttpResponse


@csrf_exempt
def homepage(request):
	context = {}
	if request.method =='POST':
		name= request.POST.get('name')
		phone = request.POST.get('phone')
		email = request.POST.get('email')
		suggestion = request.POST.get('suggestions')

		if name and phone and email and suggestion:
			suggestions = Suggestions()
			suggestions.name = name
			suggestions.phone = phone
			suggestions.email = email
			suggestions.suggestion = suggestion
			suggestions.save()
			return HttpResponse("success")
		else:
			context['error_form'] = True
			return HttpResponse("error")

	return render(request, 'index.html', context)

def subscribe(request):
	context = {}
	if request.method == 'POST':
		token = request.POST.get('stripeToken')
		name = request.POST.get('InputName')
		phoneno = request.POST.get('Inputphno')
		tvshow = request.POST.get('InputTvshow')
		if token and name and phoneno and tvshow:
# Get the credit card details submitted by the form
			try:
			  	charge = stripe.Charge.create(
			    	amount=100, # amount in cents, again
			    	currency="usd",
			    	source=token,
			    	description="spoiler charge"
			  	)
			  	spoilerVictim = SpoilerVictim()
				spoilerVictim.name = name
				spoilerVictim.phoneno = phoneno
				spoilerVictim.tvshow = tvshow
				spoilerVictim.save()

				context['successful'] = True
			except stripe.error.CardError as e:
			  	print e
			  	context['failure'] = True
			  	pass
		else:
			context['nodata'] = True


	return render(request, 'subscribe.html', context)