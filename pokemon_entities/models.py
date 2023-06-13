from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название на русском')
    title_en = models.CharField(max_length=200, blank=True, null=True, verbose_name='Название на англиском')
    title_jp = models.CharField(max_length=200, blank=True, null=True, verbose_name='Название на японском')
    image = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    next_evolution = models.ForeignKey('self',
                                       blank=True,
                                       null=True,
                                       on_delete=models.SET_NULL,
                                       verbose_name='В кого эволюционирует',
                                       related_name='previous_evolutions')

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон', related_name='entities')
    appeared_at = models.DateTimeField(verbose_name='Когда появляется')
    disappeared_at = models.DateTimeField(verbose_name='Когда исчезает')
    level = models.IntegerField(verbose_name='Уровень', blank=True, null=True)
    health = models.IntegerField(verbose_name='Здоровье', blank=True, null=True)
    strength = models.IntegerField(verbose_name='Сила', blank=True, null=True)
    defence = models.IntegerField(verbose_name='Защита', blank=True, null=True)
    stamina = models.IntegerField(verbose_name='Выносливость', blank=True, null=True)

    class Meta:
        verbose_name = 'Появление покемона'
        verbose_name_plural = 'Появления покемонов'

    def __str__(self):
        return f'{self.pokemon}_{self.pk}'
