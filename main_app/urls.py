from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('pets/', views.PetList.as_view(), name='pet_index'),
    path('pets/<int:pk>/', views.PetDetailView.as_view(), name='pet_detail'),
    path('pets/create/', views.PetCreateView.as_view(), name='pet_create'),
    path('pets/<int:pk>/update/', views.PetUpdateView.as_view(), name='pet_update'),
    path('pets/<int:pk>/delete/', views.PetDeleteView.as_view(), name='pet_delete'),
    path('pets/<int:pet_id>/pet_vaccinationdetail/', views.PetVaccinationDetail, name='pet_vaccinationdetail'),
    path('pets/<int:pet_id>/pet_vaccinationdetail/pet_addvaccination/', views.pet_addvaccination, name='pet_addvaccination'),
    path('pets/<int:pet_id>/assoc_vet/<int:vet_id>/', views.assoc_vet, name='assoc_vet'),
    path('pets/<int:pet_id>/unassoc_vet/<int:vet_id>/', views.unassoc_vet, name='unassoc_vet'),
    path('pets/<int:pet_id>/add_grooming/', views.add_grooming, name='add_grooming'),

    path('pets/<int:pet_id>/groomings/<int:grooming_id>/delete/', views.GroomingDeleteView, name='grooming_delete_view'),
    path('pets/<int:pet_id>/groomings/<int:grooming_id>/_delete/', views.GroomingDelete, name='grooming_delete'),

    path('vets/', views.VetList.as_view(), name='vet_index'),
    path('vets/<int:pk>/', views.VetDetailView.as_view(), name='vet_detail'),
    path('vets/create/', views.VetCreateView.as_view(), name='vet_create'),
    path('vets/<int:pk>/update/', views.VetUpdateView.as_view(), name='vet_update'),
    path('vets/<int:pk>/delete/', views.VetDeleteView.as_view(), name='vet_delete'),
    path('visits/', views.VisitList.as_view(), name='visit_index'),
    path('visits/<int:pk>/', views.VisitDetailView.as_view(), name='visit_detail'),
    path('visits/create/', views.VisitCreateView.as_view(), name='visit_create'),
    path('visits/<int:pk>/update/', views.VisitUpdateView.as_view(), name='visit_update'),
    path('visits/<int:pk>/delete/', views.VisitDeleteView.as_view(), name='visit_delete')
]

