from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.db import models

class Professeur(models.Model):
    id_prof = models.AutoField(primary_key=True)
    nom_prof = models.CharField(max_length=50)
    prenom_prof = models.CharField(max_length=50)
    specialite_prof = models.CharField(max_length=150)
    image_prof = models.ImageField(upload_to='prof_photos/')
    adresse_prof = models.CharField(max_length=100)
    telephone_prof = models.CharField(max_length=50)
    email_prof = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if self.image_prof:
            try:
                img = Image.open(self.image_prof)
                img = img.convert('RGB')  # Assurer compatibilité
                img_io = BytesIO()
                
                # Toujours compresser l'image
                img.save(img_io, format='JPEG', quality=70)  # Ajuster la qualité
                
                # Remplacer l'image originale par la version compressée
                new_image_name = f"{self.image_prof.name.split('.')[0]}_compressed.jpg"
                self.image_prof = ContentFile(img_io.getvalue(), new_image_name)
            except Exception as e:
                raise ValueError(f"Erreur lors du traitement de l'image : {e}")
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom_prof} {self.prenom_prof}"


class LienSociale(models.Model):
    id_lien = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=50)
    lien = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    id_prof = models.ForeignKey(Professeur, on_delete=models.CASCADE)

    def __str__(self):
        return self.designation

class Photo(models.Model):
    id_photo = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/')
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if self.image:
            try:
                img = Image.open(self.image)
                img = img.convert('RGB')  # Assurer compatibilité
                img_io = BytesIO()
                
                # Toujours compresser l'image
                img.save(img_io, format='JPEG', quality=70)  # Ajuster la qualité
                
                # Remplacer l'image originale par la version compressée
                new_image_name = f"{self.image.name.split('.')[0]}_compressed.jpg"
                self.image = ContentFile(img_io.getvalue(), new_image_name)
            except Exception as e:
                raise ValueError(f"Erreur lors du traitement de l'image : {e}")
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre

class Message(models.Model):
    id_message = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)
    sujet = models.CharField(max_length=100)
    email_user = models.EmailField(max_length=255)
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sujet

class Filiere(models.Model):
    id_filiere = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.designation

class Etudiant(models.Model):
    id_etudiant = models.AutoField(primary_key=True)
    nom_etu = models.CharField(max_length=50)
    prenom_etu = models.CharField(max_length=50)
    email_etu = models.EmailField(max_length=100)
    image_etu = models.ImageField(upload_to='etudiant_photos/')
    telephone_etu = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    id_filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if self.image_etu:
            try:
                img = Image.open(self.image_etu)
                img = img.convert('RGB')  # Assurer compatibilité
                img_io = BytesIO()
                
                # Toujours compresser l'image
                img.save(img_io, format='JPEG', quality=70)  # Ajuster la qualité
                
                # Remplacer l'image originale par la version compressée
                new_image_name = f"{self.image_etu.name.split('.')[0]}_compressed.jpg"
                self.image_etu = ContentFile(img_io.getvalue(), new_image_name)
            except Exception as e:
                raise ValueError(f"Erreur lors du traitement de l'image : {e}")
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom_etu} {self.prenom_etu}"

class Soutenance(models.Model):
    id_sout = models.AutoField(primary_key=True)
    theme = models.CharField(max_length=255)
    Heure_deb = models.TimeField(null=True, blank=True)
    Heure_fin = models.TimeField()
    Date_sout = models.DateField()
    lieu = models.CharField(max_length=100)
    is_finish = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    id_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)

    def __str__(self):
        return self.theme

class Rapport(models.Model):
    id_rapport = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=255)
    sommaire = models.TextField()
    contenu = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    id_sout = models.ForeignKey(Soutenance, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

class Superviser(models.Model):
    id_sout = models.ForeignKey(Soutenance, on_delete=models.CASCADE)
    id_prof = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('id_sout', 'id_prof')

    def __str__(self):
        return f"{self.id_sout} - {self.id_prof}"

class Apprecier(models.Model):
    id_sout = models.ForeignKey(Soutenance, on_delete=models.CASCADE)
    id_prof = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    appreciation = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('id_sout', 'id_prof')

    def __str__(self):
        return f"{self.id_sout} - {self.id_prof}"

class SoutenanceImage(models.Model):
    id_sout = models.ForeignKey(Soutenance, on_delete=models.CASCADE)
    id_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    pour = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('id_sout', 'id_photo')

    def __str__(self):
        return f"{self.id_sout} - {self.id_photo}"
