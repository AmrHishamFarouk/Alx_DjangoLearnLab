from django import forms
from .models import Comment, Post, Tag

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'tags']  # Include tags field

    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        label='Your Comment'
    )
    
    # Add tags selection field (using a multiple choice field)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),  # Display all available tags
        widget=forms.CheckboxSelectMultiple,  # Display tags as checkboxes
        required=False,
        label='Tags'  # Label for tags
    )

    def __init__(self, *args, **kwargs):
        post_id = kwargs.get('initial', {}).get('post_id')  # Get post_id from kwargs
        super().__init__(*args, **kwargs)

        # If post_id is provided, pre-select tags related to the specific post
        if post_id:
            post = Post.objects.get(id=post_id)
            self.fields['tags'].queryset = post.tags.all()

# blog/forms.py doesn't contain: ["TagWidget()", "widgets"]