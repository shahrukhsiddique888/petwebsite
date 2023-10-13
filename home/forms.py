from django import forms

from .models import petList

# image =forms.ImageField()      

class NoteForm(forms.ModelForm):
    class Meta:
       model =petList
       fields= ('title', 'text', 'age' ,'image' )
       
    #    'age','gender','description','image_path','status','suburb','state','fee','date_added')



