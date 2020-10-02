from django import forms
from faceapp.models import UserProfile

class RegisterForm(forms.ModelForm):

    class Meta:
        model=UserProfile
        fields=(
        'face_id',
        'name',
        'address',
        'job',
        'phone',
        'email',
        'bio',
        'image',
    )
