from django.urls import path
from aplicatie1 import views

app_name = "locations"

urlpatterns = [
    path("", views.LocationView.as_view(), name="lista_locatii"),
    path("adaugare/", views.CreateLocationView.as_view(), name="adauga"),
    path("<int:pk>/update/", views.UpdateLocationView.as_view(), name="modifica"),
    path("<int:pk>/sterge/", views.delete_location, name="sterge"),
    path("<int:pk>/dezactiveaza", views.deactivate_location, name="dezactiveaza"),
    path("<int:pk>/activeaza/", views.activate_location, name="activeaza"),
    #
    path("companies/", views.CompanyView.as_view(), name="list_companies"),
    path("company/add", views.CreateCompanyView.as_view(), name="add_company"),
    path(
        "company/<int:pk>/update/",
        views.UpdateCompanyView.as_view(),
        name="update_company",
    ),
    path("company/<int:pk>/sterge/", views.delete_company, name="delete_company"),
    path(
        "company/<int:pk>/dezactiveaza",
        views.deactivate_company,
        name="deactivate_company",
    ),
    path(
        "company/<int:pk>/activeaza/", views.activate_company, name="activate_company"
    ),
]
