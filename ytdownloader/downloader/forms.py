from django import forms


class DownloadFileForm(forms.Form):
    ytlink = forms.URLField(label='url here', max_length=200)


