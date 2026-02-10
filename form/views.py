from django.shortcuts import render

from form.forms import ContactForm

# Create your views here.


def contact(request):
    """
    Handle contact form submissions.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request, 'form/success.html')
            except Exception as e:
                print("💥 Contact form error:", e)
                return render(request, 'form/contact.html', {'form': form})
        else:
            print("❌ Form errors:", form.errors)
    else:
        form = ContactForm()
    return render(request, 'form/contact.html', {'form': form})


def success(request):
    """
    Render success page after contact form submission.
    """
    return render(request, 'form/success.html')