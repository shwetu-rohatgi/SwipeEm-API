from django.shortcuts import render
from django.http import JsonResponse,HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
import json as simplejson
from .models import product

# Create your views here.
@login_required
def home(request, id):
	instance = get_object_or_404(product, pk=id)
	test = {
	"name":instance.name,
	"url":instance.image.url,
	"price":instance.price,
	"shipping_charges":instance.shipping_charges,
	"description":instance.description,
	"brand":instance.brand,
	"material":instance.material,
	"gender":instance.gender,
	"estimated_arrival":instance.estimated_arrival,
	}
	return JsonResponse(test)