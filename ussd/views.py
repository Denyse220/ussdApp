from django.http.response import HttpResponse
from django.shortcuts import render
import africastalking
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .iteganya import *
# Create your views here.
def  welcome(request):
    return render(request, 'index.html')

#  python3 -m pip install africastalking
AfricasUsername='denysedufitimana@gmail.com'
api_key ='e206468a9df4c9be697e337f35a1a0caab9f549e2135af9f417d990beb246dbc'
africastalking.initialize(AfricasUsername,api_key)

@csrf_exempt
def ussdApp(request):

    if request.method == 'POST':

        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number =request.POST.get("phoneNumber")
        text = request.POST['text']
        level = text.split('*')
        category = text[:3]
        response =""
        #  main menu for our application
        if text == '':
            response =  "CON Welcome to E-Butchery \n"
            response += "1. Kugura \n"
            response += "2. Kumenya menu\n"
        elif text == '1':

            response = "CON Hitamo ubwoko bw'inyama\n"
            response += "1. inka  \n"
            response += "2. ihene"
        elif text == '1*1':
            product="inka"
            response = "CON shyiramo ibiro ukeneye' "+str(product)+"\n"
        elif category =='1*1' and int(len(level)) == 3 and str(level[2]) in  str(level):
            response = "CON Aderesi \n"
        elif category =='1*1' and int(len(level)) == 4 and str(level[3]) in  str(level):
            response = "CON injiza amafaranga wishyure\n"
        elif category =='1*1' and int(len(level)) == 5 and str(level[4]) in  str(level):
            

            # save the data into the database
            category='Inka'
            sizeOfland=level[2]
            names= level[3]
            idnumber = level[4]
            insert = Idafarmuser(sessiondId=session_id,
            serviceCode = service_code,
            phoneNumber=phone_number,
            level=level,
            category=category,
            sizeOfland=sizeOfland,
            names=names,
            idnumber=idnumber,
            )
            insert.save()
            response = "END Murakoze guhahana natwe\n"


        elif text == '1*2':
            product ="Inkoko"
            response ="CON ibiro ukeneye' "+str(product)+"\n"
        elif category =='1*2' and int(len(level)) == 3 and str(level[2]) in  str(level):
            response = "CON  \n"
        elif category =='1*2' and int(len(level)) == 4 and str(level[3]) in  str(level):
            response = "CON aderesi\n"
        elif category =='1*2' and int(len(level)) == 5 and str(level[4]) in  str(level):
            category='Inkoko'
            sizeOfland=level[2]
            names= level[3]
            idnumber = level[4]
            insert = Idafarmuser(sessiondId=session_id,
            serviceCode = service_code,
            phoneNumber=phone_number,
            level=level,
            category=category,
            sizeOfland=sizeOfland,
            names=names,
            idnumber=idnumber,
            )
            insert.save()
            response = "END Murakoze guhahana natwe \n"
         
        #  ======================== INGENGABIHE==================
        elif text == '2':
            response = "CON Hitamo isaha ikunogeye \n "
            response += "1. 80:00-11:00 \n"
            response += "2. 1:00-5:00 \n"
            response += "3. Anytime"
        elif text == '2*1':
            response ="END murakoze"
            # save the data
        #     insertData(
        #         category='Rimwe',
        #         sessionID=session_id,
        #         phoneNumber=phone_number
        #     )
        #     response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe rimwe mukwezi"
        # elif text == '2*2':
        #     insertData(
        #         category='Kabiri',
        #         sessionID=session_id,
        #         phoneNumber=phone_number
        #     )
        #     response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe kabiri mukwezi"
        # elif text == '2*3':
        #     insertData(
        #         category='Burigihe',
        #         sessionID=session_id,
        #         phoneNumber=phone_number
        #     )
        #     response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe Buri munsi"

        else:
            response = "END Ukanze ibitaribyo, ongera mukanya"
        return HttpResponse(response)
    else:
         return HttpResponse('we are on ussd app')
