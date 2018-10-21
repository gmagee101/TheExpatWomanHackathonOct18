from django import forms

default_text="""Job Title: Mechanical Engineer
Essential Functions
- Challenge the status quo by creating superior product designs through the development and testing of specifications and methods.

Knowledge and Skills:
- Superior design skills
- Exceptional conceptual skills
- First-rate technical knowledge
- Strong communication skills
- Proven experience with production planning

Working Conditions:
- Tight deadlines and multiple priorities, requiring decisive decision making in a fast-paced environment. 
- Willing to work outside the standard 9-5 schedule, including early mornings, evenings, and weekends as required by tight project deadlines. 
- Ability to work independently in a competitive work environment.

Education & Experience Requirements:
- Bachelor’s degree
- 3-5 years of work experience
"""

class JobDescForm(forms.Form):
    job_desc = forms.CharField(initial=default_text, label="Job Description", widget=forms.Textarea(attrs={'class':'form-control'}))
    

