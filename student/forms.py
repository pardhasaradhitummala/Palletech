from django import forms

from student.models import StudentModel


class TraineeForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "name",
                    'class':'name'
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "enter email",
                    'class': 'email'
                }
            ),
            "phone": forms.NumberInput(
                attrs={
                    "placeholder": "phone number",
                    'class': 'phonenumber'
                }
            ),
            "course": forms.TextInput(
                attrs={
                    "placeholder": "course",
                    'class': 'course'
                }
            ),
            "fee": forms.NumberInput(
                attrs={
                    "placeholder": "fee",
                    'class': 'fee'
                }
            ),
            "image": forms.FileInput(
                attrs={
                    'class': 'image'
                }
            )
        }
