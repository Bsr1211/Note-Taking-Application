from django import forms
from Note_taking_app.models import Customer,Blog,Admin




class CustomerForms(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"



class AdminForms(forms.ModelForm):
    class Meta:
        model=Admin
        fields="__all__"

class BlogForms(forms.ModelForm):
    class Meta:
        model=Blog
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super(BlogForms, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True



class BlogForm(BlogForms):
    class Meta(BlogForms.Meta):
        pass

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False

