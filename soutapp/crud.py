from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Superviser, Apprecier
import json


# --- Superviser CRUD Operations ---
def list_supervisers(request):
    if request.method == 'GET':
        supervisers = list(Superviser.objects.values())
        return JsonResponse(supervisers, safe=False)


def create_superviser(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            superviser = Superviser.objects.create(
                id_sout_id=data['id_sout'],
                id_prof_id=data['id_prof'],
                role=data['role']
            )
            return JsonResponse({'message': 'Superviser créé avec succès', 'id': superviser.id})
        except Exception as e:
            return JsonResponse({'error': f"Erreur lors de la création : {str(e)}"})


def update_superviser(request, id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            superviser = get_object_or_404(Superviser, id=id)
            superviser.role = data.get('role', superviser.role)
            superviser.save()
            return JsonResponse({'message': 'Superviser mis à jour avec succès'})
        except Exception as e:
            return JsonResponse({'error': f"Erreur lors de la mise à jour : {str(e)}"})


def delete_superviser(request, id):
    if request.method == 'DELETE':
        try:
            superviser = get_object_or_404(Superviser, id=id)
            superviser.delete()
            return JsonResponse({'message': 'Superviser supprimé avec succès'})
        except Exception as e:
            return JsonResponse({'error': f"Erreur lors de la suppression : {str(e)}"})


# --- Apprecier CRUD Operations ---
def list_apprecies(request):
    if request.method == 'GET':
        apprecies = list(Apprecier.objects.values())
        return JsonResponse(apprecies, safe=False)


def create_apprecier(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            apprecier = Apprecier.objects.create(
                id_sout_id=data['id_sout'],
                id_prof_id=data['id_prof'],
                appreciation=data['appreciation']
            )
            return JsonResponse({'message': 'Apprecier créé avec succès', 'id': apprecier.id})
        except Exception as e:
            return JsonResponse({'error': f"Erreur lors de la création : {str(e)}"})


def update_apprecier(request, id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            apprecier = get_object_or_404(Apprecier, id=id)
            apprecier.appreciation = data.get('appreciation', apprecier.appreciation)
            apprecier.save()
            return JsonResponse({'message': 'Apprecier mis à jour avec succès'})
        except Exception as e:
            return JsonResponse({'error': f"Erreur lors de la mise à jour : {str(e)}"})


def delete_apprecier(request, id):
    if request.method == 'DELETE':
        try:
            apprecier = get_object_or_404(Apprecier, id=id)
            apprecier.delete()
            return JsonResponse({'message': 'Apprecier supprimé avec succès'})
        except Exception as e:
            return JsonResponse({'error': f"Erreur lors de la suppression : {str(e)}"})
