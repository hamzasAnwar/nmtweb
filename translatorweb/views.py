# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import subprocess
import time
from subprocess import PIPE

from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

from translatorweb.form import TranslatorForm


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        form = TranslatorForm()
        translateDict = {}
        translateDict['arabicText'] = ''

        form = TranslatorForm(initial=translateDict)
        return render(request, 'index.html', {'form': form})

    def post(self,request,**kwargs):
        form = TranslatorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form = form.cleaned_data
            translateDict={}
            arabicText = form['arabicText']

            print(+os.path.dirname(os.path.realpath(+__file__)))

            file = open(os.path.dirname('.')+'\\output\\test.ara', 'w+',encoding='utf8')
            file.write(arabicText)
            file.close()
            time.sleep(1)

            #os.system(os.path.dirname(os.path.realpath(__file__))+"\\arabic_preprocess.bat")
            #time.sleep(3)
            #process = subprocess.Popen([os.path.dirname(os.path.realpath(__file__))+"\\arabic_preprocess.bat"], stdout=PIPE, stderr=PIPE)
            #process.wait()  # Wait for process to complete.

            file = open(os.path.dirname(os.path.realpath(__file__))+'\\output\\test.tok.rom.ara', 'r',encoding='utf8')
            transliterated = file.read()
            file.close()

            translateDict['arabicText']=arabicText


            translateDict['transliterateText']=transliterated

            translateDict['englishText'] = arabicText.upper()

            translateForm = TranslatorForm(initial=translateDict)

            return render(request, 'index.html', {'form': translateForm})
