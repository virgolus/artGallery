# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from Contacts.models import Contact
from django.http import HttpResponse

def index(request):
    return render_to_response('ContactsManagement/index.html', {})

def getAllContacts(request):
    # Create json from Contacs
    Contacts = get_object_or_404(Contact.objects.all())
    #return render_to_response('ContactsManagement/index.html', {})
    return HttpResponse("{\"Result\":\"OK\", \"Records\":[{\"PersonId\":1,\"Name\":\"Benjamin\",\"SurName\":\"Button\"}, {\"PersonId\":2,\"Name\":\"Douglas\",\"SurName\":\"Adams\"}]}")