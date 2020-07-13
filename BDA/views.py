from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from BDA.models import BDAdata


def bdaloginpage(request):
    # if the request is post
    if request.method == 'POST':
        context_id = ''
        context_password = ''
        # getting data from html page
        html_userid = request.POST['userid']
        html_password = request.POST['userpassword']
        #getting data from database based on user id
        data = BDAdata.objects.filter(userid=html_userid)
        #data is queryset if record is there it will contain one row
        # if record is not there it will be empty
        # if user is not there in database
        if len(data) == 0:
            context_id = 'user not found'
            context_password = ''
        else:
            if html_password == data[0].password:
                #we have to write logic for database record is matching and
                #password is matching
                print(str(data[0].dateofJoining))
                context = {
                    'user1': data[0].userid,
                    'date': str(data[0].dateofJoining)[:10]
                }
                return render(request,'BdaUsepannel.html',context)

            else:
                # if user is there and password not matches the database record
                context_id = ''
                context_password = 'your user name and password not matching'

        context = {
            'id':context_id,
            'password':context_password
        }

        return render(request, 'bdahomepage.html', context)
    # if the request is get
    else:
        context = {
            'id': '',
            'password': ''
        }
    return render(request,'bdahomepage.html',context)