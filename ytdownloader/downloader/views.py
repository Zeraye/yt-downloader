from django.shortcuts import redirect, render
from .forms import DownloadFileForm
from .models import DownloadFile
import re

def home(request):
    if request.method == 'POST':
        form = DownloadFileForm(request.POST)
        if form.is_valid():
            re_exp = '((?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)'
            ytlink = re.findall(re_exp, request.POST['ytlink'])[0][-1]
            newfile = DownloadFile.objects.create_file(ytlink)
            if newfile != None:
                newfile.save()
            return redirect('files/' + ytlink)
    else:
        form = DownloadFileForm()

    return render(request, 'downloader/home.html', {'form': form})

def file(request, specific_ytlink):
    context = {'file': DownloadFile.objects.filter(ytlink=specific_ytlink)}
    return render(request, 'downloader/file.html', context)
