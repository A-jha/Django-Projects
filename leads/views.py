from re import template
from django.core.mail import send_mail
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm
# Create your views here.


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    # return HttpResponse("Hello Home page")
    return render(request, "leads/lead_list.html", context)

# ---------X----List----X--------


class LeadDetailView(generic.DetailView):
    template_name = "leads_details.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


def lead_detail(request, pk):
    # print(pk)
    lead = Lead.objects.get(id=pk)
    print(lead)
    context = {
        "lead": lead
    }
    return render(request, 'leads_details.html', context)

# def lead_create(request):
#     #print(request.POST)
#     if request.method == "POST":
#         #print("Receiving POST Request")
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             first_name = data['first_name']
#             last_name = data['last_name']
#             age = data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent =agent
#             )
#             #print("lead is created")
#             return redirect("/leads")
#     context = {
#         "Form":LeadForm()
#     }
#     return render(request,"leads/lead_create.html",context)

# def lead_create(request):
#     #print(request.POST)
#     form = LeadModelForm()
#     if request.method == "POST":
#         #print("Receiving POST Request")
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             first_name = data['first_name']
#             last_name = data['last_name']
#             age = data['age']
#             agent = data['agent']
#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent =agent
#             )
#             #print("lead is created")
#             return redirect("/leads")
#     context = {
#         "Form":LeadModelForm()
#     }
#     return render(request,"leads/lead_create.html",context)


def lead_create(request):
    # print(request.POST)
    form = LeadModelForm()
    if request.method == "POST":
        #print("Receiving POST Request")
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "Form": LeadModelForm()
    }
    return render(request, "leads/lead_create.html", context)


class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        # TODO send mail
        send_mail(
            subject="A lead has been created",
            message="I hope you are okay",
            from_email="test@test.com",
            recipient_list=['test2@test.com']
        )
        return super(LeadCreateView, self).form_valid(form)
# --------update-------
# def lead_update(request,pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         #print("Receiving POST Request")
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             first_name = data['first_name']
#             last_name = data['last_name']
#             age = data['age']
#             #agent = Agent.objects.first()
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             #print("lead is created")
#             return redirect("/leads")
#     context = {
#         "form":form,
#         "lead":lead
#     }
#     return render(request,"leads/lead_update.html",context)


class UpdateView(generic.UpdateView):
    template_name = "leads.lead_update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        #print("Receiving POST Request")
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "lead": lead,
        "form": form
    }
    return render(request, "leads/lead_update.html", context)


class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")
