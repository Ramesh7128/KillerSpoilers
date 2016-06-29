from django.shortcuts import render

# from calcapp.models import Calculations
# from channels import Group
import json
# from channels.sessions import channel_session
from django.views.decorators.csrf import csrf_exempt

def homepage(request):
	return render(request, 'index.html', {})