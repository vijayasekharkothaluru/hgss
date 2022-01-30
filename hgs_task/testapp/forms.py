from django import forms
from django.core.exceptions import ValidationError
class Hgs_Form(forms.Form):
    text = forms.CharField(
        required=False,
        label="Enter Text",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Text'
            }
        )
    )
    start = forms.IntegerField(
        required=False,
        label="start Index",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'start Index'
            }
        )
    )
    end = forms.IntegerField(
        required=False,
        label="end Index",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'end Index'
            },
        )
    )

    def clean_end(self):
        text = self.cleaned_data.get('text')
        end = self.cleaned_data.get('end')
        start = self.cleaned_data.get('start')
        if end == None or end == '':
            raise ValidationError('Please Enter End Value')
        else:
            if end < 0:
                raise ValidationError("allows Positive values only")
            elif end == 0:
                raise ValidationError("zero not allowed")
            elif text != None:
                if len(text) < end:
                    raise ValidationError("end length should not Grether than Text Length")
            elif start != None:
                if end < start :
                    raise ValidationError("end length should be Grether than Start Length")
            return end

    def clean_start(self):
        text = self.cleaned_data.get('text')
        start = self.cleaned_data.get('start')
        if start == None or start == '':
            raise ValidationError('Please Enter Start Value')
        else:
            if text != None:
                if start < 0:
                    raise ValidationError("Start value allows Positive values only")
                elif start == 0:
                    raise ValidationError("zero not allowed")
                elif len(text) < start:
                    raise ValidationError("start length should not Grether than Text Length")
                return start

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if text == '' or text == None:
            raise ValidationError('Please Enter Text Value')
        return text