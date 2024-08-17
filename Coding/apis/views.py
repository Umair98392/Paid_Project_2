from django.shortcuts import render


from .models import localityDescription



def index(request):
   records = localityDescription.objects.all() # Collect all records from table 
   context = {
      
      'records' : records,
   }
    
   return render(request, 'index.html', context=context)

