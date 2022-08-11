# from django import forms
# from datetime import date

# from events.models import Event, EventParticipants
# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = '__all__'
#         widgets = {
#             'start_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'end_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
#         }

#     def clean(self):
#         cleaned_data = self.cleaned_data

#         return cleaned_data

#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         if commit:
#             instance.save()
#         return instance
    
    

