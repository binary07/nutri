<template lang="html">

  <div class="container">
    <div class="row">
      <div class="col text-left">
        <h2>{{ patient_first_name }} {{ patient_last_name }} {{ patient_second_lastname }}</h2>
        <div class="row">
          <div class="col">
            <div class="card">
              <div class="card-body">
                <p>Nutriologo: {{ nutritionist_first_name }} {{ nutritionist_last_name }} {{ nutritionist_second_lastname }}</p>
                <p>% de Grasa: {{ body_fat }}</p>
                <p>% de Músculo: {{ body_muscle }}</p>
                <p>Circunferencia de Cintura (cm): {{ waist }}</p>
                <p>Circunferencia de abdomen (cm): {{ belly }}</p>
                <p>Circunferencia de cadera (cm): {{ hip }}</p>
                <p>Circunferencia de biceps (cm): {{ biceps }}</p>
                <p>Otras medidas antropométricas: {{ another_measures }}</p>
                <p>Objetivos y Razones: {{ reason_objectives }}</p>
                <p>Cirugías: {{ surgeries }}</p>
                <p>Enfermedades:</p>
                <ul id="example-1">
                  <li v-for="(disease, index) in diseases_names">
                    {{ ++index }}.- {{ disease }}
                  </li>
                </ul>
                <p>Síntomas:</p>
                <ul id="example-1">
                  <li v-for="(symptom, index) in symptoms_names">
                    {{ ++index }}.- {{ symptom }}
                  </li>
                </ul>
                <p>Bajo Medicación: {{ under_medication }}</p>
                <p>Medicinas tomadas: {{ medicines }}</p>
                <p>¿Toma suplementos?: {{ under_supplement }}</p>
                <p>Suplementos tomados: {{ supplements }}</p>
                <p>¿Alergico a Comidas?: {{ allergic }}</p>
                <p>Comidas que den alergia: {{ allergies }}</p>
                <p>¿Intolerante a Comidas?: {{ food_intolerant }}</p>
                <p>Comidas que no toleras: {{ intolerant_foods }}</p>
                <p>¿Fumador?: {{ smoker }}</p>
                <p>Habitos de fumador: {{ smoke_frequency }}</p>
                <p>¿Bebes café?: {{ coffee_drinker }}</p>
                <p>Habitos de consumo de café: {{ ways_of_coffe_consume }}</p>
                <p>¿Bebe Alcohol?: {{ alcohol_drinker }}</p>
                <p>Habitos de consumo de alcohol: {{ ways_of_alcohol_consume }}</p>
                <p>Mililitros de agua al día: {{ water_mililiters }}</p>
                <p>¿Bebe bebidas azucaradas?: {{ sugar_drinker }}</p>
                <p>Habitos de consumo de bebidas azucaradas: {{ ways_of_sugar_drinks_consume }}</p>
                <p>Hora a la que se levanta: {{ wake_up_time }}</p>
                <p>Hora a la que se duerme: {{ sleep_time }}</p>
                <p>Hora del Desayuno: {{ breakfast_hour }}</p>
                <p>Desayuno: {{ breakfast_detail }}</p>
                <p>Hora de Colación: {{ firstbreak_hour }}</p>
                <p>Colación: {{ firstbreak_detail }}</p>
                <p>Hora de la Comida: {{ lunch_hour }}</p>
                <p>Comida: {{ lunch_detail }}</p>
                <p>Hora de Segunda Colación: {{ secondbreak_hour }}</p>
                <p>Segunda Colación: {{ secondbreak_detail }}</p>
                <p>Hora de la Cena: {{ dinner_hour }}</p>
                <p>Cena: {{ dinner_detail }}</p>
                <p>Entre comidas: {{ between_meals }}</p>
                <p>Menciona comida que no te gusta: {{ dislike_foods }}</p>
                <p>Comidas preferidas: {{ like_foods }}</p>
                <p>Ejercicios que realizas: {{ exercise_details }}</p>
                <p>Lesiones: {{ injuries }}</p>
              </div>
            </div>
          </div>
        </div>
        <b-button
          size="sm"
          variant="success"
          :to="{name: 'Patient', params: {patientId: patient}}"
        >
          Paciente
        </b-button>
      </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      recordId: this.$route.params.recordId,
      api: 'https://back.pruebasreset.website/api/v1.0/',
      patient: '',
      nutritionist: '',
      body_fat: '',
      body_muscle: '',
      waist: '',
      belly: '',
      hip: '',
      biceps: '',
      another_measures: '',
      reason_objectives: '',
      surgeries: '',
      diseases: [],
      symptoms: [],
      diseases_names: [],
      symptoms_names: [],
      under_medication: '',
      medicines: '',
      under_supplement: '',
      supplements: '',
      allergic: '',
      allergies: '',
      food_intolerant: '',
      intolerant_foods: '',
      smoker: '',
      smoke_frequency: '',
      coffee_drinker: '',
      ways_of_coffe_consume: '',
      alcohol_drinker: '',
      ways_of_alcohol_consume: '',
      water_mililiters: '',
      sugar_drinker: '',
      ways_of_sugar_drinks_consume: '',
      wake_up_time: '',
      sleep_time: '',
      breakfast_hour: '',
      breakfast_detail: '',
      firstbreak_hour: '',
      firstbreak_detail: '',
      lunch_hour: '',
      lunch_detail: '',
      secondbreak_hour: '',
      secondbreak_detail: '',
      dinner_hour: '',
      dinner_detail: '',
      between_meals: '',
      dislike_foods: '',
      like_foods: '',
      exercise_details: '',
      injuries: '',
      patient_first_name: '',
      patient_last_name: '',
      patient_second_lastname: '',
      nutritionist_first_name: '',
      nutritionist_last_name: '',
      nutritionist_second_lastname: '',
    }
  },
  methods: {
    getRecord() {
      const path = this.api+`medicalrecords/${this.recordId}/`

      axios.get(path).then((response) => {
        this.patient = response.data.patient
        this.nutritionist = response.data.nutritionist
        this.body_fat = response.data.body_fat
        this.body_muscle = response.data.body_muscle
        this.waist = response.data.waist
        this.belly = response.data.belly
        this.hip = response.data.hip
        this.biceps = response.data.biceps
        this.another_measures = response.data.another_measures
        this.reason_objectives = response.data.reason_objectives
        this.surgeries = response.data.surgeries
        this.diseases = response.data.diseases
        this.symptoms = response.data.symptoms
        this.under_medication = response.data.under_medication
        this.medicines = response.data.medicines
        this.under_supplement = response.data.under_supplement
        this.supplements = response.data.supplements
        this.allergic = response.data.allergic
        this.allergies = response.data.allergies
        this.food_intolerant = response.data.food_intolerant
        this.intolerant_foods = response.data.intolerant_foods
        this.smoker = response.data.smoker
        this.smoke_frequency = response.data.smoke_frequency
        this.coffee_drinker = response.data.coffee_drinker
        this.ways_of_coffe_consume = response.data.ways_of_coffe_consume
        this.alcohol_drinker = response.data.alcohol_drinker
        this.ways_of_alcohol_consume = response.data.ways_of_alcohol_consume
        this.water_mililiters = response.data.water_mililiters
        this.sugar_drinker = response.data.sugar_drinker
        this.ways_of_sugar_drinks_consume = response.data.ways_of_sugar_drinks_consume
        this.wake_up_time = response.data.wake_up_time
        this.sleep_time = response.data.sleep_time
        this.breakfast_hour = response.data.breakfast_hour
        this.breakfast_detail = response.data.breakfast_detail
        this.firstbreak_hour = response.data.firstbreak_hour
        this.firstbreak_detail = response.data.firstbreak_detail
        this.lunch_hour = response.data.lunch_hour
        this.lunch_detail = response.data.lunch_detail
        this.secondbreak_hour = response.data.secondbreak_hour
        this.secondbreak_detail = response.data.secondbreak_detail
        this.dinner_hour = response.data.dinner_hour
        this.dinner_detail = response.data.dinner_detail
        this.between_meals = response.data.between_meals
        this.dislike_foods = response.data.dislike_foods
        this.like_foods = response.data.like_foods
        this.exercise_details = response.data.exercise_details
        this.injuries = response.data.injuries
        this.getPatient()
        this.getNutritionist()
        this.getDiseases()
        this.getSymptoms()
      })
      .catch((error) => {
        console.log(error)
      })
    },

    getPatient() {

      const path = this.api+`patients/${this.patient}/`

      axios.get(path).then((response) => {
        this.patient_first_name = response.data.first_name
        this.patient_last_name = response.data.last_name
        this.patient_second_lastname = response.data.second_lastname
      })
      .catch((error) => {
        console.log(error)
      })
    },

    getNutritionist() {

      const path = this.api+`nutritionists/${this.nutritionist}/`

      axios.get(path).then((response) => {
        this.nutritionist_first_name = response.data.first_name
        this.nutritionist_last_name = response.data.last_name
        this.nutritionist_second_lastname = response.data.second_lastname
      })
      .catch((error) => {
        console.log(error)
      })
    },

    getDiseases() {

      var i;
      for (i = 0; i < this.diseases.length; i++) {
        
        const path = this.api+`diseases/${this.diseases[i]}/`

        axios.get(path).then((response) => {
          this.diseases_names.push(response.data.name)
        })
        .catch((error) => {
          console.log(error)
        })
      }
    },

    getSymptoms() {

      var i;
      for (i = 0; i < this.symptoms.length; i++) {
        
        const path = this.api+`symptoms/${this.symptoms[i]}/`

        axios.get(path).then((response) => {
          this.symptoms_names.push(response.data.name)
        })
        .catch((error) => {
          console.log(error)
        })
      }
    },

  },

  created(){
    this.getRecord()
  }
}
</script>

<style lang="css" scoped>
</style>