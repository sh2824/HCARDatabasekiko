from django import forms

class ArtistSearchForm(forms.Form):
        artist_fname = forms.CharField(label="First Name", max_length=100, required=False)
        artist_lname = forms.CharField(label="Last Name", max_length=100, required=False)

class StorageSearchForm(forms.Form):
        storage_loc = forms.CharField(label="Location", max_length=100, required=False)
        storage_city = forms.CharField(label="City", max_length=100, required=False)
        storage_room = forms.CharField(label="Room", max_length=100, required=False)
