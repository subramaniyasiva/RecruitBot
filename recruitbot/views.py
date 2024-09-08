from django.shortcuts import render,redirect
from .forms import details_forms

def details_view(request):
    if request.method == 'POST':
        form = details_forms(request.POST)
        if form.is_valid():
            form.save()  # Save form data to the database
            return redirect('details_updated')  # Redirect after successful form submission
    else:
        form = details_forms()
    
    return render(request, 'home.html', {'form': form})
def details_updated_view(request):
    return render(request, 'details_updated.html')