from django import forms

class JobDescForm(forms.Form):
    job_desc = forms.CharField(label="Job Description", widget=forms.Textarea(attrs={'class':'form-control'}))

