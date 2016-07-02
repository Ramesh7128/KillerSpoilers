from django.shortcuts import render

# from calcapp.models import Calculations
# from channels import Group
import json
# from channels.sessions import channel_session
from django.views.decorators.csrf import csrf_exempt
from killerapp.models import *
import stripe

def homepage(request):
	return render(request, 'index.html', {})

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
			context['failure'] = True


	return render(request, 'subscribe.html', context)