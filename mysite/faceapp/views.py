from django.shortcuts import render,redirect
from faceapp.forms import RegisterForm
from django.contrib import messages
from faceapp.backEnd import FaceRecognition
from faceapp.models import UserProfile

facerecognition=FaceRecognition()

def faceapp(request):
    return render(request,'faceapp/face.html')
def register(request):
    if request.POST:
        form=RegisterForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            messages.success(request,'Successfully Registered')
            addFace(request.POST['face_id'])
            return redirect('/')
        else:
            messages.error(request,"Account register Failed")
    form=RegisterForm()
    context= {
     'title': 'Register Form',
     'form': 'form'
    }
    return render(request,'faceapp/register.html',context)
def addFace(face_id):
    face_id=face_id
    facerecognition.faceDetect(face_id)
    facerecognition.trainFace()
    return redirect('/')
def login(request):
    face_id=int(face_id)
    print(face_id)
    data= {
    'user': UserProfile.objects.get(face_id=face_id)
    }

    return render(request,'faceapp/profile.html',data)





# Create your views here.
