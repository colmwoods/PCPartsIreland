from django.shortcuts import render, redirect
from django.contrib import messages
from form.forms import ContactForm, ReturnRequestForm

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
                messages.success(request, "Your message has been sent successfully!")
                return redirect('success')

            except Exception as e:
                messages.error(
                    request,
                    "Something went wrong while sending your message. Please try again."
                )
        else:
            messages.error(
                request,
                "Please correct the errors below and resubmit the form."
            )
    else:
        form = ContactForm()

    return render(request, 'form/contact.html', {'form': form})


def success(request):
    """
    Render success page after contact form submission.
    """
    return render(request, 'form/success.html')


def return_request(request):
    """
    Handle return request submissions.
    """
    if request.method == "POST":
        form = ReturnRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("return_success")
    else:
        form = ReturnRequestForm()

    return render(request, "form/return_form.html", {"form": form})


def return_success(request):
    """
    Render success page after return request.
    """
    return render(request, "form/return_success.html")