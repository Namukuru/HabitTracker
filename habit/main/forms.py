from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Habit

class SignUpForm(UserCreationForm):
  email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
  first_name = forms.CharField(label="", max_length="100", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
  last_name = forms.CharField(label="",max_length="100", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
  class Meta:
    model = User
    fields = ('username','first_name', 'last_name','email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
      super(SignUpForm, self).__init__(*args, **kwargs)

      self.fields['username'].widget.attrs['class'] = 'form-control'
      self.fields['username'].widget.attrs['placeholder'] = 'Username'
      self.fields['username'].label = ''
      self.fields['username'].help_text = ''

      self.fields['password1'].widget.attrs['class'] = 'form-control'
      self.fields['password1'].widget.attrs['placeholder'] = 'Password'
      self.fields['password1'].label = ''
      self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li></ul>'

      self.fields['password2'].widget.attrs['class'] = 'form-control'
      self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
      self.fields['password2'].label = ''
      self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


#add habits form
class AddRecordForm(forms.ModelForm):
  name= forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Habit Name', "class":"form-control"}), label="")
  description= forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Description', "class":"form-control"}), label="")
  start_date= forms.DateField(required=True, widget=forms.widgets.DateTimeInput(attrs={'placeholder':'Start Date', "class":"form-control"}), label="")
  frequency= forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Frequency', "class":"form-control"}), label="")
  habit_type = forms.ChoiceField(choices=Habit.HABIT_TYPE_CHOICES, required=True, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}), label="Habit Type")

  
  class Meta:
      model = Habit
      fields = ('name','description', 'start_date','frequency','habit_type')
      
      '''def clean(self):
        cleaned_data = super().clean()
        habit_type = cleaned_data.get('habit_type')

        if habit_type == 'integer':
            # Additional validation for integer habits if needed
            pass
        elif habit_type == 'yes_no':
            # Additional validation for yes/no habits if needed
            pass
        elif habit_type == 'timer':
            # Additional validation for timer habits if needed
            pass

        return cleaned_data'''