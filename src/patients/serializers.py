from .models import (
    Patient,
    Disease,
    Symptom,
    MedicalRecord,
)
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = [
            'id',
            'name',
        ]


class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = [
            'id',
            'name',
        ]


class MedicalRecordSerializer(serializers.ModelSerializer):

    body_fat = serializers.CharField(
        required=False,
    )
    body_muscle = serializers.CharField(
        required=False,
    )
    waist = serializers.CharField(
        required=False,
    )
    belly = serializers.CharField(
        required=False,
    )
    hip = serializers.CharField(
        required=False,
    )
    biceps = serializers.CharField(
        required=False,
    )
    another_measures = serializers.CharField(
        required=False,
    )
    surgeries = serializers.CharField(
        required=False,
    )
    under_medication = serializers.BooleanField(
        default=False,
        required=False,
    )
    medicines = serializers.CharField(
        required=False,
    )
    under_supplement = serializers.BooleanField(
        default=False,
        required=False,
    )
    supplements = serializers.CharField(
        required=False,
    )
    allergic = serializers.BooleanField(
        default=False,
        required=False,
    )
    allergies = serializers.CharField(
        required=False,
    )
    food_intolerant = serializers.BooleanField(
        default=False,
        required=False,
    )
    intolerant_foods = serializers.CharField(
        required=False,
    )
    smoker = serializers.BooleanField(
        default=False,
        required=False,
    )
    smoke_frequency = serializers.CharField(
        required=False,
    )
    coffee_drinker = serializers.BooleanField(
        default=False,
        required=False,
    )
    ways_of_coffe_consume = serializers.CharField(
        required=False,
    )
    alcohol_drinker = serializers.BooleanField(
        default=False,
        required=False,
    )
    ways_of_alcohol_consume = serializers.CharField(
        required=False,
    )
    sugar_drinker = serializers.BooleanField(
        default=False,
        required=False,
    )
    ways_of_sugar_drinks_consume = serializers.CharField(
        required=False,
    )
    firstbreak_hour = serializers.TimeField(
        required=False,
    )
    firstbreak_detail = serializers.CharField(
        required=False,
    )
    secondbreak_hour = serializers.TimeField(
        required=False,
    )
    secondbreak_detail = serializers.CharField(
        required=False,
    )
    between_meals = serializers.CharField(
        required=False,
    )
    dislike_foods = serializers.CharField(
        required=False,
    )
    like_foods = serializers.CharField(
        required=False,
    )
    exercise_details = serializers.CharField(
        required=False,
    )
    injuries = serializers.CharField(
        required=False,
    )

    class Meta:
        model = MedicalRecord
        fields = [
            'id',
            'patient',
            'nutritionist',
            'body_fat',
            'body_muscle',
            'waist',
            'belly',
            'hip',
            'biceps',
            'another_measures',
            'reason_objectives',
            'surgeries',
            'diseases',
            'symptoms',
            'under_medication',
            'medicines',
            'under_supplement',
            'supplements',
            'allergic',
            'allergies',
            'food_intolerant',
            'intolerant_foods',
            'smoker',
            'smoke_frequency',
            'coffee_drinker',
            'ways_of_coffe_consume',
            'alcohol_drinker',
            'ways_of_alcohol_consume',
            'water_mililiters',
            'sugar_drinker',
            'ways_of_sugar_drinks_consume',
            'wake_up_time',
            'sleep_time',
            'breakfast_hour',
            'breakfast_detail',
            'firstbreak_hour',
            'firstbreak_detail',
            'lunch_hour',
            'lunch_detail',
            'secondbreak_hour',
            'secondbreak_detail',
            'dinner_hour',
            'dinner_detail',
            'between_meals',
            'dislike_foods',
            'like_foods',
            'exercise_details',
            'injuries',
        ]

    def create(self, validated_data):
        record = MedicalRecord.objects.create(
            patient=validated_data['patient']
        )
        if 'nutritionist' in validated_data:
            record.nutritionist = validated_data['nutritionist']
        if 'body_fat' in validated_data:
            record.body_fat = validated_data['body_fat']
        if 'body_muscle' in validated_data:
            record.body_muscle = validated_data['body_muscle']
        if 'waist' in validated_data:
            record.waist = validated_data['waist']
        if 'belly' in validated_data:
            record.belly = validated_data['belly']
        if 'hip' in validated_data:
            record.hip = validated_data['hip']
        if 'biceps' in validated_data:
            record.biceps = validated_data['biceps']
        if 'another_measures' in validated_data:
            record.another_measures = validated_data['another_measures']
        if 'reason_objectives' in validated_data:
            record.reason_objectives = validated_data['reason_objectives']
        if 'surgeries' in validated_data:
            record.surgeries = validated_data['surgeries']
        if 'diseases' in validated_data:
            record.diseases = validated_data['diseases']
        if 'symptoms' in validated_data:
            record.symptoms = validated_data['symptoms']
        if 'under_medication' in validated_data:
            record.under_medication = validated_data['under_medication']
        if 'medicines' in validated_data:
            record.medicines = validated_data['medicines']
        if 'under_supplement' in validated_data:
            record.under_supplement = validated_data['under_supplement']
        if 'supplements' in validated_data:
            record.supplements = validated_data['supplements']
        if 'allergic' in validated_data:
            record.allergic = validated_data['allergic']
        if 'allergies' in validated_data:
            record.allergies = validated_data['allergies']
        if 'food_intolerant' in validated_data:
            record.food_intolerant = validated_data['food_intolerant']
        if 'intolerant_foods' in validated_data:
            record.intolerant_foods = validated_data['intolerant_foods']
        if 'smoker' in validated_data:
            record.smoker = validated_data['smoker']
        if 'smoke_frequency' in validated_data:
            record.smoke_frequency = validated_data['smoke_frequency']
        if 'coffee_drinker' in validated_data:
            record.coffee_drinker = validated_data['coffee_drinker']
        if 'ways_of_coffe_consume' in validated_data:
            record.ways_of_coffe_consume = validated_data['ways_of_coffe_consume']
        if 'alcohol_drinker' in validated_data:
            record.alcohol_drinker = validated_data['alcohol_drinker']
        if 'ways_of_alcohol_consume' in validated_data:
            record.ways_of_alcohol_consume = validated_data['ways_of_alcohol_consume']
        if 'water_mililiters' in validated_data:
            record.water_mililiters = validated_data['water_mililiters']
        if 'sugar_drinker' in validated_data:
            record.sugar_drinker = validated_data['sugar_drinker']
        if 'ways_of_sugar_drinks_consume' in validated_data:
            record.ways_of_sugar_drinks_consume = validated_data['ways_of_sugar_drinks_consume']
        if 'wake_up_time' in validated_data:
            record.wake_up_time = validated_data['wake_up_time']
        if 'sleep_time' in validated_data:
            record.sleep_time = validated_data['sleep_time']
        if 'breakfast_hour' in validated_data:
            record.breakfast_hour = validated_data['breakfast_hour']
        if 'breakfast_detail' in validated_data:
            record.breakfast_detail = validated_data['breakfast_detail']
        if 'firstbreak_hour' in validated_data:
            record.firstbreak_hour = validated_data['firstbreak_hour']
        if 'firstbreak_detail' in validated_data:
            record.firstbreak_detail = validated_data['firstbreak_detail']
        if 'lunch_hour' in validated_data:
            record.lunch_hour = validated_data['lunch_hour']
        if 'lunch_detail' in validated_data:
            record.lunch_detail = validated_data['lunch_detail']
        if 'secondbreak_hour' in validated_data:
            record.secondbreak_hour = validated_data['secondbreak_hour']
        if 'secondbreak_detail' in validated_data:
            record.secondbreak_detail = validated_data['secondbreak_detail']
        if 'dinner_hour' in validated_data:
            record.dinner_hour = validated_data['dinner_hour']
        if 'dinner_detail' in validated_data:
            record.dinner_detail = validated_data['dinner_detail']
        if 'between_meals' in validated_data:
            record.between_meals = validated_data['between_meals']
        if 'dislike_foods' in validated_data:
            record.dislike_foods = validated_data['dislike_foods']
        if 'like_foods' in validated_data:
            record.like_foods = validated_data['like_foods']
        if 'exercise_details' in validated_data:
            record.exercise_details = validated_data['exercise_details']
        if 'injuries' in validated_data:
            record.injuries = validated_data['injuries']
        record.save()

        return record


class PatientSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(
        source='user.id',
        read_only=True,
    )
    email = serializers.EmailField(
        source='user.email',
        required=False,
    )
    first_name = serializers.CharField(
        source='user.first_name',
        required=False,
    )
    last_name = serializers.CharField(
        source='user.last_name',
        required=False,
    )
    second_lastname = serializers.CharField(
        source='user.second_lastname',
        required=False,
    )
    gender = serializers.CharField(
        source='user.gender',
        required=False,
    )
    phone = serializers.CharField(
        source='user.phone',
        required=False,
    )
    residence_state = serializers.CharField(
        source='user.residence_state',
        required=False,
    )
    records = MedicalRecordSerializer(
        read_only=True,
        required=False,
        many=True,
    )
    password = serializers.CharField(
        source='user.password',
        style={'input_type': 'password'},
        required=False,
    )

    class Meta:
        model = Patient
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'second_lastname',
            'gender',
            'residence_state',
            'phone',
            'age',
            'birthday',
            'weight',
            'height',
            'body_mass',
            'body_fat',
            'body_muscle',
            'records',
            'password',
        ]

    def create(self, validated_data):

        print('#####'*50)
        print(validated_data)
        print('#####'*50)

        user = User(
            username = validated_data['user']['phone'],
            first_name = validated_data['user']['first_name'],
            last_name = validated_data['user']['last_name'],
            email = validated_data['user']['email'],
            residence_state = validated_data['user']['residence_state'],
            is_patient=True,
            is_nutritionist=False,
        )
        
        if 'second_lastname' in validated_data['user']:
            user.second_lastname = validated_data['user']['second_lastname']
        if 'phone' in validated_data['user']:
            user.phone = validated_data['user']['phone']
        if 'gender' in validated_data['user']:
            user.gender = validated_data['user']['gender']

        user.set_password(validated_data['user']['password'])
        user.save()
        
        patient = Patient.objects.create(
            user=user,
        )
        
        if 'age' in validated_data:
            patient.age = validated_data['age']
        if 'birthday' in validated_data:
            patient.birthday = validated_data['birthday']
        if 'weight' in validated_data:
            patient.weight = validated_data['weight']
        if 'height' in validated_data:
            patient.height = validated_data['height']
        if 'weight' and 'height' in validated_data:
            imc = patient.weight / (patient.height**2)
            imc = round(imc, 2)
            patient.body_mass = imc
        if 'body_fat' in validated_data:
            patient.body_fat = validated_data['body_fat']
        if 'body_muscle' in validated_data:
            patient.body_muscle = validated_data['body_muscle']
        patient.save()
        
        return patient

    def update(self, instance, validated_data):
        if 'user' in validated_data:
            if 'first_name' in validated_data['user']:
                instance.user.first_name = validated_data['user']['first_name']
            if 'last_name' in validated_data['user']:
                instance.user.last_name = validated_data['user']['last_name']
            if 'second_lastname' in validated_data['user']:
                instance.user.second_lastname = validated_data['user']['second_lastname']
            if 'email' in validated_data['user']:
                instance.user.email = validated_data['user']['email']
            if 'phone' in validated_data['user']:
                instance.user.phone = validated_data['user']['phone']
            if 'gender' in validated_data['user']:
                instance.user.gender = validated_data['user']['gender']
            if 'residence_state' in validated_data['user']:
                instance.user.residence_state = validated_data['user']['residence_state']
            instance.user.save()

        if 'age' in validated_data:
            instance.age = validated_data['age']
        if 'birthday' in validated_data:
            instance.birthday = validated_data['birthday']
        if 'weight' in validated_data:
            instance.weight = validated_data['weight']
        if 'height' in validated_data:
            instance.height = validated_data['height']
        if 'weight' and 'height' in validated_data:
            imc = instance.weight / (instance.height**2)
            imc = round(imc, 2)
            instance.body_mass = imc
        if 'body_fat' in validated_data:
            instance.body_fat = validated_data['body_fat']
        if 'body_muscle' in validated_data:
            instance.body_muscle = validated_data['body_muscle']
        instance.save()

        return instance
