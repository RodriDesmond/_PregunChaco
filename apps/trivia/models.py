from django.db import models

class BaseModel(models.Model):
    creado = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Categoria(BaseModel):
    nombre_categoria = models.CharField(max_length=100)
    logo_categoria = models.ImageField(upload_to ='uploads/')

    def __str__(self):
        return self.nombre_categoria

    def logo_url(self):
        if self.logo_categoria and hasattr(self.logo_categoria, 'url'):
            return self.logo_categoria.url
