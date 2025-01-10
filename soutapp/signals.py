from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import Photo, Professeur, Etudiant # Importer les models nécessaire

# supprime Photo lors d'une mise à jour
@receiver(pre_save, sender=Photo)
def delete_Photo_image_file_on_update(sender, instance, **kwargs):
    """
    Supprime l'ancien fichier image lorsqu'une nouvelle image est mise à jour
    pour une instance du modèle Photo.
    """
    if not instance.pk:
        return  # Si l'instance est nouvelle (pas encore dans la base), on ne fait rien.

    try:
        old_instance = Photo.objects.get(pk=instance.pk)  # Récupère l'ancienne instance
        if old_instance.image and old_instance.image != instance.image:
            # Supprime l'ancien fichier si une nouvelle image est définie
            old_instance.image.delete(save=False)
    except Photo.DoesNotExist:
        pass  # L'ancienne instance n'existe pas, pas besoin de faire quoi que ce soit.

# Supprime la Photo lors de la suppression de l'instance
@receiver(post_delete, sender=Photo)
def delete_image_file(sender, instance, **kwargs):
    """
    Supprime le fichier image associé à une instance du modèle Photo
    lorsqu'elle est supprimée.
    
    """
    if instance.image:
        instance.image.delete(save=False)  # Supprime le fichier sans sauvegarder l'instance


# Supprime la photo du professeur à la mise à jour de celle-ci
@receiver(pre_save, sender=Professeur)
def delete_Professeur_image_file_on_update(sender, instance, **kwargs):
    """
    Supprime l'ancien fichier image lorsqu'une nouvelle image est mise à jour
    pour une instance du modèle Professeur.
    """
    if not instance.pk:
        return  # Si l'instance est nouvelle (pas encore dans la base), on ne fait rien.

    try:
        old_instance = Professeur.objects.get(pk=instance.pk)  # Récupère l'ancienne instance
        if old_instance.image_prof and old_instance.image_prof != instance.image_prof:
            # Supprime l'ancien fichier si une nouvelle image est définie
            old_instance.image_prof.delete(save=False)
    except Professeur.DoesNotExist:
        pass  # L'ancienne instance n'existe pas, pas besoin de faire quoi que ce soit.

# Supprime la photo du Professeur lors de la suppression de l'instance
@receiver(post_delete, sender=Professeur)
def delete_Professeur_image_file(sender, instance, **kwargs):
    """
    Supprime le fichier image associé à une instance du modèle testimony
    lorsqu'elle est supprimée.
    
    """
    if instance.image_prof:
        instance.image_prof.delete(save=False)  # Supprime le fichier sans sauvegarder l'instance


# supprime Etudiant lors d'une mise à jour
@receiver(pre_save, sender=Etudiant)
def delete_Etudiant_image_file_on_update(sender, instance, **kwargs):
    """
    Supprime l'ancien fichier image lorsqu'une nouvelle image est mise à jour
    pour une instance du modèle Etudiant.
    """
    if not instance.pk:
        return  # Si l'instance est nouvelle (pas encore dans la base), on ne fait rien.

    try:
        old_instance = Etudiant.objects.get(pk=instance.pk)  # Récupère l'ancienne instance
        if old_instance.image_etu and old_instance.image_etu != instance.image_etu:
            # Supprime l'ancien fichier si une nouvelle image est définie
            old_instance.image_etu.delete(save=False)
    except Etudiant.DoesNotExist:
        pass  # L'ancienne instance n'existe pas, pas besoin de faire quoi que ce soit.


# Supprime Etudiant lors de la suppression de l'instance
@receiver(post_delete, sender=Etudiant)
def delete_Etudiant_image_file(sender, instance, **kwargs):
    """
    Supprime le fichier image associé à une instance du modèle Etudiant
    lorsqu'elle est supprimée.
    
    """
    if instance.image_etu:
        instance.image_etu.delete(save=False)  # Supprime le fichier sans sauvegarder l'instance

