from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from aplicatie1.models import Location, AuditLocation, Company, AuditCompany


# Create your views here.
class LocationView(LoginRequiredMixin, ListView):
    model = Location
    template_name = "aplicatie1/locations_index.html"
    paginate_by = 5
    queryset = model.objects.all().order_by("id")

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data()
        data["page"] = (
            self.request.GET.get("page") if self.request.GET.get("page") else 1
        )
        return data


class CreateLocationView(LoginRequiredMixin, CreateView):
    model = Location
    fields = ["city", "country"]
    template_name = "aplicatie1/locations_form.html"

    def get_success_url(self):
        return reverse("locations:lista_locatii")


class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Location
    fields = ["city", "country"]
    template_name = "aplicatie1/locations_form.html"

    def get_success_url(self):
        return reverse("locations:lista_locatii")


@login_required
def delete_location(request, pk):
    location_value = Location.objects.get(id=pk)
    AuditLocation.objects.create(
        location=location_value.id,
        city=location_value.city,
        country=location_value.country,
        active=location_value.active,
        user_id=request.user.id,
    )
    Location.objects.filter(id=pk).delete()
    return redirect(f'/locations/?page={request.GET.get("page")}')


@login_required
def deactivate_location(request, pk):
    Location.objects.filter(id=pk).update(active=0)
    return redirect(f'/locations/?page={request.GET.get("page")}')


@login_required
def activate_location(request, pk):
    Location.objects.filter(id=pk).update(active=1)
    return redirect(f'/locations/?page={request.GET.get("page")}')


class CompanyView(LoginRequiredMixin, ListView):
    model = Company
    template_name = "aplicatie1/company_index.html"
    paginate_by = 5
    queryset = model.objects.all().order_by("id")

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data()
        data["page"] = (
            self.request.GET.get("page") if self.request.GET.get("page") else 1
        )
        return data


class CreateCompanyView(LoginRequiredMixin, CreateView):
    model = Company
    fields = ["name", "website", "location"]
    template_name = "aplicatie1/company_form.html"

    def get_success_url(self):
        return reverse("locations:list_companies")


class UpdateCompanyView(LoginRequiredMixin, UpdateView):
    model = Company
    fields = ["name", "website", "location"]
    template_name = "aplicatie1/company_form.html"

    def get_success_url(self):
        return reverse("locations:list_companies")


@login_required
def delete_company(request, pk):
    company_value = Location.objects.get(id=pk)
    AuditCompany.objects.create(
        company=company_value.id,
        name=company_value.name,
        website=company_value.website,
        location=company_value.location,
        active=company_value.active,
        user_id=request.user.id,
    )
    Company.objects.filter(id=pk).delete()
    return redirect(f"/locations/companies/")


@login_required
def deactivate_company(request, pk):
    Company.objects.filter(id=pk).update(active=0)
    return redirect(f"/locations/companies/")


@login_required
def activate_company(request, pk):
    Company.objects.filter(id=pk).update(active=1)
    return redirect(f"/locations/companies/")
