from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Patient(models.Model):

    user = models.OneToOneField(
        'users.User',
        primary_key=True,
        verbose_name='usuario',
        related_name='patient',
        on_delete=models.CASCADE,
    )
    weight = models.FloatField(
        'peso',
        validators=[
            MaxValueValidator(500),
            MinValueValidator(1),
        ],
        blank=True,
        null=True,
    )
    birthday = models.DateField(
        'cumpleaños',
        blank=True,
        null=True,
    )
    age = models.PositiveIntegerField(
        'edad',
        blank=True,
        null=True,
    )
    height = models.FloatField(
        'estatura',
        validators=[
            MaxValueValidator(150),
            MinValueValidator(1),
        ],
        blank=True,
        null=True,
    )
    body_mass = models.FloatField(
        'masa corporal',
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1),
        ],
        blank=True,
        null=True,
    )
    body_fat = models.FloatField(
        'grasa corporal',
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1),
        ],
        blank=True,
        null=True,
    )
    body_muscle = models.FloatField(
        'músculo corporal',
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1),
        ],
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        user = self.user
        return f'{user.first_name} {user.last_name} {user.second_lastname}'


class Disease(models.Model):

    name = models.CharField(
        'nombre',
        max_length=50,
    )

    class Meta:
        verbose_name = "Enfermedad"
        verbose_name_plural = "Enfermedades"

    def __str__(self):
        return self.name


class Symptom(models.Model):

    name = models.CharField(
        'nombre',
        max_length=50,
    )

    class Meta:
        verbose_name = "Síntoma"
        verbose_name_plural = "Síntomas"

    def __str__(self):
        return self.name


class MedicalRecord(models.Model):

    patient = models.ForeignKey(
        'Patient',
        verbose_name='paciente',
        related_name='records',
        on_delete=models.CASCADE,
    )
    nutritionist = models.ForeignKey(
        'nutritionists.Nutritionist',
        verbose_name='nutriolgo',
        related_name='records',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    body_fat = models.FloatField(
        'grasa corporal',
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1),
        ],
        blank=True,
        null=True,
    )
    body_muscle = models.FloatField(
        'músculo corporal',
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1),
        ],
        blank=True,
        null=True,
    )
    waist = models.FloatField(
        'cintura',
        blank=True,
        null=True
    )
    belly = models.FloatField(
        'abdomen',
        blank=True,
        null=True
    )
    hip = models.FloatField(
        'cadera',
        blank=True,
        null=True
    )
    biceps = models.FloatField(
        'biceps',
        blank=True,
        null=True
    )
    another_measures = models.TextField(
        'otras medidas antropométricas',
        blank=True,
        null=True,
    )
    reason_objectives = models.TextField(
        'razones y objetivos',
        blank=True,
        null=True,
    )
    surgeries = models.TextField(
        'cirugías',
        blank=True,
        null=True,
    )
    diseases = models.ManyToManyField(
        'Disease',
        verbose_name='enfermedades',
        related_name='records',
    )
    symptoms = models.ManyToManyField(
        'Symptom',
        verbose_name='síntomas',
        related_name='records',
    )
    under_medication = models.BooleanField(
        'bajo medicamento',
        default=False,
    )
    medicines = models.TextField(
        'medicinas',
        blank=True,
        null=True,
    )
    under_supplement = models.BooleanField(
        'bajo medicamento',
        default=False,
    )
    supplements = models.TextField(
        'suplementos',
        blank=True,
        null=True,
    )
    allergic = models.BooleanField(
        'alergico',
        default=False
    )
    allergies = models.TextField(
        'alergias',
        blank=True,
        null=True,
    )
    food_intolerant = models.BooleanField(
        'intolerante',
        default=True,
    )
    intolerant_foods = models.TextField(
        'comidas no toleradas',
        blank=True,
        null=True,
    )
    smoker = models.BooleanField(
        'fumador',
        default=False,
    )
    smoke_frequency = models.TextField(
        'frecuencia',
        blank=True,
        null=True,
    )
    coffee_drinker = models.BooleanField(
        'bebedor de café',
        default=True,
    )
    ways_of_coffe_consume = models.TextField(
        'formas de consumo de cafe',
        blank=True,
        null=True,
    )
    alcohol_drinker = models.BooleanField(
        'consumidor de alcohol',
        default=True,
    )
    ways_of_alcohol_consume = models.TextField(
        'formas de consumo de alcohol',
        blank=True,
        null=True,
    )
    water_mililiters = models.FloatField(
        'consumo de agua',
        blank=True,
        null=True,
    )
    sugar_drinker = models.BooleanField(
        default=True,
    )
    ways_of_sugar_drinks_consume = models.TextField(
        'formas de consumo de bebidas azucaradas',
        blank=True,
        null=True,
    )
    wake_up_time = models.TimeField(
        'hora al despertarse',
        blank=True,
        null=True,
    )
    sleep_time = models.TimeField(
        'hora al dormir',
        blank=True,
        null=True,
    )
    breakfast_hour = models.TimeField(
        'hora de desayuno',
        blank=True,
        null=True,
    )
    breakfast_detail = models.TextField(
        'detalle del desayuno',
        blank=True,
        null=True,
    )
    firstbreak_hour = models.TimeField(
        'hora de colación',
        blank=True,
        null=True,
    )
    firstbreak_detail = models.TextField(
        'detalle de la colación',
        blank=True,
        null=True,
    )
    lunch_hour = models.TimeField(
        'hora de comida',
        blank=True,
        null=True,
    )
    lunch_detail = models.TextField(
        'detalle de la comida',
        blank=True,
        null=True,
    )
    secondbreak_hour = models.TimeField(
        'hora de merienda',
        blank=True,
        null=True,
    )
    secondbreak_detail = models.TextField(
        'detalle del merienda',
        blank=True,
        null=True,
    )
    dinner_hour = models.TimeField(
        'hora de cena',
        blank=True,
        null=True,
    )
    dinner_detail = models.TextField(
        'detalle de la cena',
        blank=True,
        null=True,
    )
    between_meals = models.TextField(
        'entre comidas',
        blank=True,
        null=True,
    )
    dislike_foods = models.TextField(
        'comida que no le agrada',
        blank=True,
        null=True,
    )
    like_foods = models.TextField(
        'comida que le agrada',
        blank=True,
        null=True,
    )
    exercise_details = models.TextField(
        'detalles de ejercicios',
        blank=True,
        null=True,
    )
    injuries = models.TextField(
        'lesiones',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Historia Clínica"
        verbose_name_plural = "Historias Clínicas"


class MedicalTracing(models.Model):
    
    patient = models.ForeignKey(
        'Patient',
        verbose_name='paciente',
        related_name='tracings',
        on_delete=models.CASCADE,
    )
    nutritionist = models.ForeignKey(
        'nutritionists.Nutritionist',
        verbose_name='nutriolgo',
        related_name='tracings',
        on_delete=models.CASCADE,
    )
    meal_times = models.PositiveIntegerField(
        'tiempos de comida'
    )
    schedule = models.TextField(
        'horarios'
    )
    amounts = models.TextField(
        'cantidades'
    )
    water = models.TextField(
        'consumo de agua'
    )
    exercise = models.TextField(
        'ejercicio'
    )
    personal_goals = models.TextField(
        'metas personales'
    )
    weekend_meals = models.TextField(
        'alimentación de fines de semana'
    )
    alcohol = models.TextField(
        'alcohol'
    )
    gastric_symptoms = models.TextField(
        'síntomas gástricos'
    )
    comments = models.TextField(
        'comentarios'
    )
    weight = models.FloatField(
        'peso',
        validators=[
            MaxValueValidator(500),
            MinValueValidator(1),
        ],
    )
    body_fat = models.FloatField(
        'grasa corporal',
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1),
        ],
    )
    body_muscle = models.FloatField(
        'músculo corporal',
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1),
        ],
    )
    kg_muscle = models.FloatField(
        'kg músculo',
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1),
        ],
    )
    igv = models.FloatField(
        'igv',
    )
    waist = models.FloatField(
        'cintura',
    )
    belly = models.FloatField(
        'abdomen',
    )
    hip = models.FloatField(
        'cadera',
    )
    biceps = models.FloatField(
        'biceps',
    )
    quadriceps = models.FloatField(
        'cuádriceps',
    )

    class Meta:
        verbose_name = "Segumiento Médico"
        verbose_name_plural = "Segumientos Médicos"


class Meal(models.Model):
    meal_description = models.TextField(
        blank = True,
        null = True
    )

    patient = models.ForeignKey(
        'Patient',
        verbose_name='paciente',
        related_name='meal',
        on_delete=models.CASCADE,
    )
    nutritionist = models.ForeignKey(
        'nutritionists.Nutritionist',
        verbose_name='nutriolgo',
        related_name='meal',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    MEAL_TYPES = (
        ('Estandar', 'Estandar'),
        ('Perdida de Peso', 'Perdida de Peso'),
        ('Deportista', 'Deportista'),
        ('Vegano, Vegetariano', 'Vegano, Vegetariano'),
        ('Con Especificación', 'Con Especificación'),
    )

    meal_type = models.CharField(
        max_length=70,
        choices=MEAL_TYPES,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Plan Alimenticio"
        verbose_name_plural = "Planes Alimenticios"


class Recipes(models.Model):
    recipe = models.TextField(
        blank=True,
        null=True
    )

    patient = models.ForeignKey(
        'Patient',
        verbose_name='paciente',
        related_name='Recipes',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"