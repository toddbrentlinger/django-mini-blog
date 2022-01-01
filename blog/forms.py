from django import forms
from django.db.models.fields import CharField, DateTimeField
from django.forms.fields import DateField

class CreateCommentForm(forms.Form):
    # Description
    description = forms.CharField(help_text="Enter new comment.")
    # Post Date - Not Editable
    post_date_time = forms.DateTimeField(disabled=True)
    # Blog - Not Editable
    blog_post = None
    # Include Blog Name and Link
    pass