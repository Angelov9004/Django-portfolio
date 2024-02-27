from django.core.mail import send_mail
from django.shortcuts import render
from .services.forms import ContactForm
from .models import interests, expirience, resume,skills,counts,Home,about,university,education,contact,services,portfolio


def index(request):
    homes = Home.objects.all()  # Fetch all from table homes
    abouts = about.objects.all()
    counts_data = counts.objects.all()
    skills_data = skills.objects.all()
    interests_data = interests.objects.all()
    university_data = university.objects.all()
    expirience_data = expirience.objects.all()
    resume_data = resume.objects.all()
    education_data = education.objects.all()
    contact_data = contact.objects.all()
    services_data = services.objects.all()
    portfolio_data = portfolio.objects.all()



    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                form.cleaned_data['subject'],  # subject
                f"Message from {form.cleaned_data['name']} <{form.cleaned_data['email']}>\n\n"
                f"{form.cleaned_data['subject']} \n\n{form.cleaned_data['message']}",  # message
                None,  # from email
                ['angelov@angeloviliyan.com'],  # replace with your email
            )
            # Redirect to the same page to prevent form resubmission
            return render(request, 'index.html',
                          {'homes': homes, 'abouts': abouts, 'counts_data': counts_data,
                                          'skills_data': skills_data, 'interests_data': interests_data,
                                          'university_data': university_data,
                                          'expirience_data': expirience_data,
                                          'resume_data': resume_data, 'education_data': education_data, 'contact_data': contact_data,
                                           'services_data': services_data, 'portfolio_data': portfolio_data,
                                           'form': ContactForm(), 'success_message': True})
    else:
        form = ContactForm()

    return render(request, 'index.html', {'homes': homes, 'abouts': abouts, 'counts_data': counts_data,
                                          'skills_data': skills_data, 'interests_data': interests_data,
                                          'university_data': university_data,
                                          'expirience_data': expirience_data,
                                          'resume_data': resume_data, 'education_data': education_data, 'contact_data': contact_data,
                                           'services_data': services_data, 'portfolio_data': portfolio_data,
                                           'form': form})

