import json
from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import utils
from django.views.decorators.csrf import csrf_exempt
from tensorflow.keras.models import load_model

model = load_model("penyakitcabai/BestModelUas.keras")

@csrf_exempt
def index(request):
    if request.method == 'POST':  
        file_form = forms.UploadFileFrom(request.POST, request.FILES)  
        if file_form.is_valid():  
            filepath = utils.handle_uploaded_file(request.FILES['image'])
            result = utils.do_identification(model, filepath)
            response = HttpResponse(json.dumps({ 'message' : 'success', 'data' : result }), content_type='application/json')
            return response 
        else:
            response = HttpResponse(json.dumps({ 'message' : 'Form tidak valid', 'detail' : file_form.errors }), content_type='application/json', status=400)
            return response 
    else:  
        response = HttpResponse(json.dumps({ 'message' : 'gagal', 'detail' : 'Method selain POST tidak ada' }), content_type='application/json', status=400)
        return response 
