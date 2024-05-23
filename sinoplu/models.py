from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'sinoplu/{0}/{1}'.format(instance.user.id, filename)
    

class Sinopluyuz(models.Model): 
    KategoriChoices = [
        ('egitim' , 'Eğitim'),  
        ('saglik' , 'Sağlık'),
        ('insaat' , 'İnşaat'),
        ('gida' , 'Gıda'),
        ('ulasim' , 'Ulaşım'),
        ('diger' , 'Diğer')
    ]
    SehirChoices = [
        ('istanbul' , 'İstanbul'),
        ('sinop' , 'Sinop'),
        ('ankara' , 'Ankara')
    ]
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    kategori = models.CharField('Kategori', max_length=20, choices=KategoriChoices)
    sehir = models.CharField('Şehirim', max_length=20, choices=SehirChoices)
    content = models.TextField(verbose_name = 'içerik')
    number = models.IntegerField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    publishing_date = models.DateTimeField(verbose_name = 'kayıt tarihi', auto_now_add = True)
    image1 = models.ImageField(upload_to=user_directory_path, default='sinoplu.jpg')
    slug = models.SlugField(blank=True)
    DisplayFields = ['publishing_date', 'sehir', 'number', 'content', 'kategori', 'image1']
    FilterFields = ['first_name', 'last_name', 'sehir', 'kategori' ]

    def __str__(self):
        return f"{self.first_name} - {self.last_name} "

    class Meta:
        ordering = ["publishing_date"]
        verbose_name_plural = "Sinoplular_Listesi"
        