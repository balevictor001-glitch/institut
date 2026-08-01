from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from .forms import PromotionForm, EtudiantForm
from .models import Promotion, Etudiant


# =========================
# DASHBOARD
# =========================

class DashboardView(TemplateView):
    template_name = 'app/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Statistiques principales
        context['total_etudiants'] = Etudiant.objects.count()
        context['total_promotions'] = Promotion.objects.count()

        # Étudiants actifs / inactifs
        context['etudiants_actifs'] = Etudiant.objects.filter(
            actif=True
        ).count()

        context['etudiants_inactifs'] = Etudiant.objects.filter(
            actif=False
        ).count()

        # Étudiants récents
        context['etudiants_recents'] = Etudiant.objects.select_related(
            'promotion'
        ).order_by('-id')[:5]

        # Promotions avec nombre d’étudiants
        context['promotions_stats'] = Promotion.objects.annotate(
            nombre_etudiants=Count('etudiants')
        ).order_by('-nombre_etudiants')[:10]

        return context


# =========================
# ETUDIANT
# =========================

class EtudiantListView(ListView):
    model = Etudiant
    template_name = 'app/etudiant_list.html'
    context_object_name = 'etudiants'
    paginate_by = 10

    def get_queryset(self):
        queryset = Etudiant.objects.select_related(
            'promotion'
        ).order_by('-id')

        statut = self.request.GET.get('statut')

        if statut == 'actif':
            queryset = queryset.filter(actif=True)

        elif statut == 'inactif':
            queryset = queryset.filter(actif=False)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtre_statut'] = self.request.GET.get('statut')
        return context


class EtudiantDetailView(DetailView):
    model = Etudiant
    template_name = 'app/etudiant_detail.html'
    context_object_name = 'etudiant'


class EtudiantCreateView(SuccessMessageMixin, CreateView):
    model = Etudiant
    form_class = EtudiantForm
    template_name = 'app/etudiant_form.html'
    success_url = reverse_lazy('etudiant_list')
    success_message = "Étudiant ajouté avec succès."


class EtudiantUpdateView(SuccessMessageMixin, UpdateView):
    model = Etudiant
    form_class = EtudiantForm
    template_name = 'app/etudiant_form.html'
    success_url = reverse_lazy('etudiant_list')
    success_message = "Étudiant modifié avec succès."


class EtudiantDeleteView(SuccessMessageMixin, DeleteView):
    model = Etudiant
    template_name = 'app/etudiant_confirm_delete.html'
    success_url = reverse_lazy('etudiant_list')
    success_message = "Étudiant supprimé avec succès."

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request,
            self.success_message
        )
        return super().delete(request, *args, **kwargs)


# =========================
# PROMOTION
# =========================

class PromotionListView(ListView):
    model = Promotion
    template_name = 'app/promotion_list.html'
    context_object_name = 'promotions'

    def get_queryset(self):
        return Promotion.objects.prefetch_related('etudiants')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # ajouter un étudiant (avec photo) pour chaque promotion
        promotions = context['promotions']

        for promo in promotions:
            promo.etudiant_photo = promo.etudiants.filter(photo__isnull=False).first()

        return context


class PromotionDetailView(DetailView):
    model = Promotion
    template_name = 'app/promotion_detail.html'
    context_object_name = 'promotion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['etudiants'] = self.object.etudiants.all().order_by('-id')
        context['nombre_etudiants'] = self.object.etudiants.count()

        return context


class PromotionCreateView(SuccessMessageMixin, CreateView):
    model = Promotion
    form_class = PromotionForm
    template_name = 'app/promotion_form.html'
    success_url = reverse_lazy('promotion_list')
    success_message = "Promotion créée avec succès."


class PromotionUpdateView(SuccessMessageMixin, UpdateView):
    model = Promotion
    form_class = PromotionForm
    template_name = 'app/promotion_form.html'
    success_url = reverse_lazy('promotion_list')
    success_message = "Promotion modifiée avec succès."


class PromotionDeleteView(SuccessMessageMixin, DeleteView):
    model = Promotion
    template_name = 'app/promotion_confirm_delete.html'
    success_url = reverse_lazy('promotion_list')
    success_message = "Promotion supprimée avec succès."

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request,
            self.success_message
        )
        return super().delete(request, *args, **kwargs)