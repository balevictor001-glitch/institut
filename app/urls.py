from django.urls import path

from .views import (
    DashboardView,

    PromotionCreateView,
    PromotionDeleteView,
    PromotionDetailView,
    PromotionListView,
    PromotionUpdateView,

    EtudiantCreateView,
    EtudiantDeleteView,
    EtudiantDetailView,
    EtudiantListView,
    EtudiantUpdateView,
)

urlpatterns = [
    # =========================
    # DASHBOARD
    # =========================
    path(
        '',
        DashboardView.as_view(),
        name='dashboard'
    ),

    # =========================
    # ETUDIANTS
    # =========================
    path(
        'etudiants/',
        EtudiantListView.as_view(),
        name='etudiant_list'
    ),

    path(
        'etudiants/<int:pk>/',
        EtudiantDetailView.as_view(),
        name='etudiant_detail'
    ),

    path(
        'etudiants/ajouter/',
        EtudiantCreateView.as_view(),
        name='etudiant_create'
    ),

    path(
        'etudiants/<int:pk>/modifier/',
        EtudiantUpdateView.as_view(),
        name='etudiant_update'
    ),

    path(
        'etudiants/<int:pk>/supprimer/',
        EtudiantDeleteView.as_view(),
        name='etudiant_delete'
    ),

    # =========================
    # PROMOTIONS
    # =========================
    path(
        'promotions/',
        PromotionListView.as_view(),
        name='promotion_list'
    ),

    path(
        'promotions/ajouter/',
        PromotionCreateView.as_view(),
        name='promotion_create'
    ),

    path(
        'promotions/<int:pk>/',
        PromotionDetailView.as_view(),
        name='promotion_detail'
    ),

    path(
        'promotions/<int:pk>/modifier/',
        PromotionUpdateView.as_view(),
        name='promotion_update'
    ),

    path(
        'promotions/<int:pk>/supprimer/',
        PromotionDeleteView.as_view(),
        name='promotion_delete'
    ),
]