from django.forms import ModelForm, Textarea, CheckboxSelectMultiple
from .models import Project, Review


class ProjectForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        # To each field at once loop through all fields and update.
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # To update a single attribute
        # self.fields['title'].widget.attrs.update({'class': 'input'})

    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description',
                  'demo_link', 'source_link', 'tags']
        widgets = {
            'description': Textarea(attrs={'cols': 30, 'rows': 5}),
            'tags': CheckboxSelectMultiple()
        }


class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        # To access each field at once loop through all fields and update.
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
        
    class Meta:
        model = Review
        fields = '__all__'
