from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    """Fields -definice jednotlivých polí/sloupců modelu/tabulky
    Každé pole modelu(budoucí tabulky v databázi) je uloženo do vhodně
    pojmenované proměnné/atributu -zde "name"Vzniká jako instance
    určité třídy (zde models.CharField), která rozhoduje o datovém typu
    pole a o jeho vlastnostechV tomto případě bude pole "name"
    obsahovat maximálně 50 znaků (parametr max_length),bude obsahovat
    unikátní hodnoty (parametr unique),ve formuláři se bude zobrazovat
    pod označením "Genre name" (parametr verbose_name),a uživateli se
    jako nápověda nabídne text uvedený v parametru help_text """
    name = models.CharField(max_length=50, unique=True, verbose_name="Genre name",
                            help_text='Enter a film genre (e.g. sci-fi, comedy)')

    class Meta:
        # atribut ordering definuje upřednostňovaný způsob řazení -zde vzestupně podle pole/sloupce name
        ordering = ["name"]

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    # Textové pole pro vložení delšího textu popisujícího děj filmu
    # Formulářový prvek může zůstat prázdný -parametry blank=True, null=True
    plot = models.TextField(blank=True, null=True, verbose_name="Plot")
    # Pole obsahuje datum uvedení filmu, které musí být zadáno v náležitém tvaru (YYYY-MM-DD); nepovinný údaj
    release_date = models.DateField(blank=True, null=True,help_text="Please use the following format: <em>YYYY-MM-DD</em>.",verbose_name="Release date")
    # Celočíselné pole pro nepovinné zadání stopáže (délky) filmu v minutách
    runtime = models.IntegerField(blank=True, null=True,help_text="Please enter an integer value (minutes)",verbose_name="Runtime")
    # Pole pro zadání desetinného čísla vyjadřujícího hodnocení filmu v rozsahu 1.0 až 10.0
    # Výchozí hodnota je nastavena na 5.0
    # K validaci hodnot jsou použity metody z balíku/knihovny django.core.validators
    rate = models.FloatField(default=5.0,validators=[MinValueValidator(1.0), MaxValueValidator(10.0)],null=True,help_text="Please enter an float value (range 1.0 -10.0)",verbose_name="Rate")
    # Vytvoří vztah mezi modely Film a Genre typu M:N
    genres = models.ManyToManyField(Genre, help_text='Select a genre for this film')

    # Metadata
    class Meta:
        # Záznamy budou řazeny primárně sestupně (znaménko mínus) podle data uvedení
        # sekundárně vzestupně podle názvu
        ordering = ["-release_date", "title"]

    # Methods
    def __str__(self):
        """Součástí textové reprezentace filmu bude jeho název, rok uvedení a hodnocení"""
        return f"{self.title}, year: {str(self.release_date.year)}, rate: {str(self.rate)}"

    def get_absolute_url(self):
        """Metoda vrací URL stránky, na které se vypisují podrobné informace o filmu"""
        return reverse('film-detail', args=[str(self.id)])
