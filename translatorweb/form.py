from django import forms


class TranslatorForm(forms.Form):
    arabicText = forms.CharField(label='Arabic Text',widget=forms.Textarea(attrs={'dir': 'rtl'}),required=True)
    transliterateText = forms.CharField(label='Transliterate Text',widget=forms.Textarea,required=False)
    englishText = forms.CharField(label='English Text',widget=forms.Textarea,required=False)
