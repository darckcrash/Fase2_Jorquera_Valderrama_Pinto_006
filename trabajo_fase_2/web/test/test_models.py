from django.test import TestCase
from web.models import Preparacion

class preparaciontest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Preparacion.objects.create(name='preparacion', summary='Prueba')
    
    def test_name_label(self):
        preparacion=Preparacion.objects.get(id=1)
        field_label = preparacion._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_summary_label(self):
        preparacion=Preparacion.objects.get(id=1)
        field_label = preparacion._meta.get_field('summary').verbose_name
        self.assertEquals(field_label,'summary')
    
    def test_name_max_length(self):
        preparacion=Preparacion.objects.get(id=1)
        max_length = preparacion._meta.get_field('name').max_length
        self.assertEquals(max_length,100)
    
    def test_summary_max_length(self):
        preparacion=Preparacion.objects.get(id=1)
        max_length = preparacion._meta.get_field('summary').max_length
        self.assertEquals(max_length,1000)
        
    def test_get_absolute_url(self):
        preparacion=Preparacion.objects.get(id=1)
        self.assertEquals(preparacion.get_absolute_url(), '/web/preparacion/1')
