from django.shortcuts import render

def control_view(request):
    return render(request, 'control.html')
def panel_view(request):
    return render(request, 'panel.html')