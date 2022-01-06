<template lang="html">
  
  <div class="container">
    
    <div class="row">
      <div class="col text-left">
        <h2>Historial Clínico</h2>
      </div>
    </div>

    <div class="row">
      <div class="col">
        <div class="card">
          <div class="card-body">
            
            <form @submit="onSubmit">

              <div class="form-group row">
                <label for="nutritionists" class="col-sm-2 col-form-label">
                  Nutriologo:
                </label>
                <div class="col-sm-6">
                  <select 
                    name="nutritionists"
                    class="form-control"
                    v-model="form.nutritionist"
                  >
                    <option v-for="nutritionist in nutritionists" v-bind:value="nutritionist.id">
                      {{ nutritionist.first_name }} {{ nutritionist.last_name }} {{ nutritionist.second_lastname }}
                    </option>
                  </select>
                </div>
              </div>

              <div class="form-group row">
                <label for="body_fat" class="col-sm-2 col-form-label">
                  % de Grasa
                </label>
                <div class="col-sm-6">
                  <input 
                    type="number"
                    placeholder="%"
                    name="body_fat"
                    class="form-control"
                    step="0.01"
                    v-model="form.body_fat"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="body_muscle" class="col-sm-2 col-form-label">
                  % de Músculo
                </label>
                <div class="col-sm-6">
                  <input 
                    type="number"
                    placeholder="%"
                    name="body_muscle"
                    class="form-control"
                    step="0.01" 
                    v-model="form.body_muscle"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="waist" class="col-sm-2 col-form-label">
                  Circunferencia de Cintura (cm)
                </label>
                <div class="col-sm-6">
                  <input 
                    type="number"
                    placeholder="cm"
                    name="waist"
                    class="form-control"
                    step="0.01" 
                    v-model="form.waist"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="belly" class="col-sm-2 col-form-label">
                  Circunferencia de abdomen (cm)
                </label>
                <div class="col-sm-6">
                  <input 
                    type="number"
                    placeholder="cm"
                    name="belly"
                    step="0.01" 
                    class="form-control"
                    v-model="form.belly"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="hip" class="col-sm-2 col-form-label">
                  Circunferencia de cadera (cm)
                </label>
                <div class="col-sm-6">
                  <input 
                    type="number"
                    placeholder="cm"
                    name="hip"
                    step="0.01" 
                    class="form-control"
                    v-model="form.hip"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="biceps" class="col-sm-2 col-form-label">
                  Circunferencia de biceps (cm)
                </label>
                <div class="col-sm-6">
                  <input 
                    type="number"
                    placeholder="cm"
                    name="biceps"
                    step="0.01" 
                    class="form-control"
                    v-model="form.biceps"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="another_measures" class="col-sm-2 col-form-label">
                  Otras medidas antropométricas
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    name="another_measures"
                    class="form-control"
                    v-model="form.another_measures"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="reason_objectives" class="col-sm-2 col-form-label">
                  Objetivos y Razones
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Explique brevemente el motivo de su consulta, y ¿que objetivos tiene?"
                    name="reason_objectives"
                    class="form-control"
                    v-model="form.reason_objectives"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="surgeries" class="col-sm-2 col-form-label">
                  Cirugías
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="¿Le han practicado alguna cirugía recientemente? ¿Cuál y cuando?"
                    name="surgeries"
                    class="form-control"
                    v-model="form.surgeries"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="diseases" class="col-sm-2 col-form-label">
                  Enfermedades:
                </label>
                <div class="col-sm-6">
                  <select 
                    name="diseases"
                    class="form-control"
                    v-model="form.diseases"
                    multiple
                  >
                    <option v-for="disease in diseases" v-bind:value="disease.id">
                      {{ disease.name }}
                    </option>
                  </select>
                </div>
              </div>

              <div class="form-group row">
                <label for="symptoms" class="col-sm-2 col-form-label">
                  Síntomas:
                </label>
                <div class="col-sm-6">
                  <select 
                    name="symptoms"
                    class="form-control"
                    v-model="form.symptoms"
                    multiple
                  >
                    <option v-for="symptom in symptoms" v-bind:value="symptom.id">
                      {{ symptom.name }}
                    </option>
                  </select>
                </div>
              </div>

              <div class="form-group row">
                <label for="under_medication" class="col-sm-2 col-form-label">
                  Bajo Medicación
                </label>
                <div class="col-sm-6">
                  <input 
                    type="checkbox"
                    name="under_medication"
                    class="form-control"
                    v-model="form.under_medication"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="medicines" class="col-sm-2 col-form-label">
                  Medicinas tomadas
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Menciona las medicinas y cantidades"
                    name="medicines"
                    class="form-control"
                    v-model="form.medicines"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="under_supplement" class="col-sm-2 col-form-label">
                  ¿Toma suplementos?
                </label>
                <div class="col-sm-6">
                  <input 
                    type="checkbox"
                    name="under_supplement"
                    class="form-control"
                    v-model="form.under_supplement"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Suplementos tomados
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Menciona los suplementos y cantidades"
                    name="supplements"
                    class="form-control"
                    v-model="form.supplements"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  ¿Alergico a Comidas?
                </label>
                <div class="col-sm-6">
                  <input 
                    type="checkbox"
                    name="allergic"
                    class="form-control"
                    v-model="form.allergic"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Comidas que den alergia
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Menciona los alimentos que te den alergia"
                    name="allergies"
                    class="form-control"
                    v-model="form.allergies"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  ¿Intolerante a Comidas?
                </label>
                <div class="col-sm-6">
                  <input 
                    type="checkbox"
                    name="food_intolerant"
                    class="form-control"
                    v-model="form.food_intolerant"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Comidas que no toleras
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Menciona las comidas que a las que eres intolerante"
                    name="intolerant_foods"
                    class="form-control"
                    v-model="form.intolerant_foods"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  ¿Fumador?
                </label>
                <div class="col-sm-6">
                  <input 
                    type="checkbox"
                    name="smoker"
                    class="form-control"
                    v-model="form.smoker"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Habitos de fumador
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Menciona cuantos cigarros al día fumas"
                    name="smoke_frequency"
                    class="form-control"
                    v-model="form.smoke_frequency"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  ¿Bebes café?
                </label>
                <div class="col-sm-6">
                  <input 
                    type="checkbox"
                    name="coffee_drinker"
                    class="form-control"
                    v-model="form.coffee_drinker"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Habitos de consumo de café
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Tazas al día/¿Grano o Soluble/Azúcar/Leche"
                    name="ways_of_coffe_consume"
                    class="form-control"
                    v-model="form.ways_of_coffe_consume"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  ¿Bebe Alcohol?
                </label>
                <div class="col-sm-6">
                  <input 
                    type="checkbox"
                    name="alcohol_drinker"
                    class="form-control"
                    v-model="form.alcohol_drinker"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Habitos de consumo de alcohol
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="¿Cuántas copas y cada cuándo?"
                    name="ways_of_alcohol_consume"
                    class="form-control"
                    v-model="form.ways_of_alcohol_consume"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Mililitros de agua al día
                </label>
                <div class="col-sm-6">
                  <input 
                    type="number"
                    placeholder="ml"
                    name="water_mililiters"
                    step="0.01" 
                    class="form-control"
                    v-model="form.water_mililiters"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  ¿Bebe bebidas azucaradas?
                </label>
                <div class="col-sm-6">
                  <input 
                    type="checkbox"
                    name="sugar_drinker"
                    class="form-control"
                    v-model="form.sugar_drinker"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Habitos de consumo de bebidas azucaradas
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Menciona las bebidas tomadas"
                    name="ways_of_sugar_drinks_consume"
                    class="form-control"
                    v-model="form.ways_of_sugar_drinks_consume"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Hora a la que se levanta
                </label>
                <div class="col-sm-6">
                  <input 
                    type="time"
                    name="wake_up_time"
                    class="form-control"
                    v-model="form.wake_up_time"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Hora a la que se duerme
                </label>
                <div class="col-sm-6">
                  <input 
                    type="time"
                    name="sleep_time"
                    class="form-control"
                    v-model="form.sleep_time"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Hora del Desayuno
                </label>
                <div class="col-sm-6">
                  <input 
                    type="time"
                    name="breakfast_hour"
                    class="form-control"
                    v-model="form.breakfast_hour"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Desayuno
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Detalla tu desayuno"
                    name="breakfast_detail"
                    class="form-control"
                    v-model="form.breakfast_detail"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Hora de Colación
                </label>
                <div class="col-sm-6">
                  <input 
                    type="time"
                    name="firstbreak_hour"
                    class="form-control"
                    v-model="form.firstbreak_hour"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Colación
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Detalla tu Colación"
                    name="firstbreak_detail"
                    class="form-control"
                    v-model="form.firstbreak_detail"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Hora de la Comida
                </label>
                <div class="col-sm-6">
                  <input 
                    type="time"
                    name="lunch_hour"
                    class="form-control"
                    v-model="form.lunch_hour"
                  >
                </div>
              </div>
              
              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Comida
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Detalla tu comida"
                    name="lunch_detail"
                    class="form-control"
                    v-model="form.lunch_detail"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Hora de Segunda Colación
                </label>
                <div class="col-sm-6">
                  <input 
                    type="time"
                    name="secondbreak_hour"
                    class="form-control"
                    v-model="form.secondbreak_hour"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Segunda Colación
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Detalla tu segunda colacion"
                    name="secondbreak_detail"
                    class="form-control"
                    v-model="form.secondbreak_detail"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Hora de la Cena
                </label>
                <div class="col-sm-6">
                  <input 
                    type="time"
                    name="dinner_hour"
                    class="form-control"
                    v-model="form.dinner_hour"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Cena
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Detalla tu cena"
                    name="dinner_detail"
                    class="form-control"
                    v-model="form.dinner_detail"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Entre comidas
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Detalla lo que comes entre comidas"
                    name="between_meals"
                    class="form-control"
                    v-model="form.between_meals"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Menciona comida que no te gusta
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Enlista la comida"
                    name="dislike_foods"
                    class="form-control"
                    v-model="form.dislike_foods"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Comidas preferidas
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Enlista la comida"
                    name="like_foods"
                    class="form-control"
                    v-model="form.like_foods"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Ejercicios que realizas
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Si haces algún ejercicio menciona a detalle"
                    name="exercise_details"
                    class="form-control"
                    v-model="form.exercise_details"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Lesiones
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Menciona lesiones recientes"
                    name="injuries"
                    class="form-control"
                    v-model="form.injuries"
                  >
                </div>
              </div>

              <div class="rows">
                <div class="col text-left">
                  <b-button type="submit" variant="primary">
                    Crear
                  </b-button>
                  <b-button 
                    type="submit"
                    variant="danger"
                    :to="{name: 'Patient', params: {patientId: patientId}}"
                  >
                    Cancelar
                  </b-button>
                </div>
              </div>
            
            </form>

          </div>
        </div>
      </div>
    </div>

  </div>

</template>

<script>

  import axios from 'axios'
  import swal from 'sweetalert'

  export default {
    data() {
      return {
        patientId: this.$route.params.patientId,
        diseases: [],
        symptoms: [],
        nutritionists: [],
        api: 'https://back.pruebasreset.website/api/v1.0/',
        form: {
          patient: this.$route.params.patientId,
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
          under_medication: false,
          medicines: '',
          under_supplement: false,
          supplements: '',
          allergic: false,
          allergies: '',
          food_intolerant: false,
          intolerant_foods: '',
          smoker: false,
          smoke_frequency: '',
          coffee_drinker: false,
          ways_of_coffe_consume: '',
          alcohol_drinker: false,
          ways_of_alcohol_consume: '',
          water_mililiters: '',
          sugar_drinker: false,
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
        }
      }
    },

    methods: {

      getNutritionists () {
        const path = this.api+`nutritionists/`;
        axios.get(path).then((response) => {
          this.nutritionists = response.data
        })
        .catch((error) => {
          console.log(error)
        })
      },

      getDiseases () {
        const path = this.api+`diseases/`;
        axios.get(path).then((response) => {
          this.diseases = response.data
          console.log(this.diseases)
        })
        .catch((error) => {
          console.log(error)
        })
      },

      getSymptoms () {
        const path = this.api+`symptoms/`;
        axios.get(path).then((response) => {
          this.symptoms = response.data
          console.log(this.symptoms)
        })
        .catch((error) => {
          console.log(error)
        })
      },

      onSubmit(evt) {

        evt.preventDefault()

        const path =  this.api+`medicalrecords/`;
        console.log("enviar Historia clínica a API", this.form);
        axios.post(path, this.form).then((response) => {

          this.form.patient = parseInt(this.patientId)
          this.form.nutritionist = response.data.nutritionist
          this.form.body_fat = response.data.body_fat
          this.form.body_muscle = response.data.body_muscle
          this.form.waist = response.data.waist
          this.form.belly = response.data.belly
          this.form.hip = response.data.hip
          this.form.biceps = response.data.biceps
          this.form.another_measures = response.data.another_measures
          this.form.reason_objectives = response.data.reason_objectives
          this.form.surgeries = response.data.surgeries
          this.form.diseases = response.data.diseases
          this.form.symptoms = response.data.symptoms
          this.form.under_medication = response.data.under_medication
          this.form.medicines = response.data.medicines
          this.form.under_supplement = response.data.under_supplement
          this.form.supplements = response.data.supplements
          this.form.allergic = response.data.allergic
          this.form.allergies = response.data.allergies
          this.form.food_intolerant = response.data.food_intolerant
          this.form.intolerant_foods = response.data.intolerant_foods
          this.form.smoker = response.data.smoker
          this.form.smoke_frequency = response.data.smoke_frequency
          this.form.coffee_drinker = response.data.coffee_drinker
          this.form.ways_of_coffe_consume = response.data.ways_of_coffe_consume
          this.form.alcohol_drinker = response.data.alcohol_drinker
          this.form.ways_of_alcohol_consume = response.data.ways_of_alcohol_consume
          this.form.water_mililiters = response.data.water_mililiters
          this.form.sugar_drinker = response.data.sugar_drinker
          this.form.ways_of_sugar_drinks_consume = response.data.ways_of_sugar_drinks_consume
          this.form.wake_up_time = response.data.wake_up_time
          this.form.sleep_time = response.data.sleep_time
          this.form.breakfast_hour = response.data.breakfast_hour
          this.form.breakfast_detail = response.data.breakfast_detail
          this.form.firstbreak_hour = response.data.firstbreak_hour
          this.form.firstbreak_detail = response.data.firstbreak_detail
          this.form.lunch_hour = response.data.lunch_hour
          this.form.lunch_detail = response.data.lunch_detail
          this.form.secondbreak_hour = response.data.secondbreak_hour
          this.form.secondbreak_detail = response.data.secondbreak_detail
          this.form.dinner_hour = response.data.dinner_hour
          this.form.dinner_detail = response.data.dinner_detail
          this.form.between_meals = response.data.between_meals
          this.form.dislike_foods = response.data.dislike_foods
          this.form.like_foods = response.data.like_foods
          this.form.exercise_details = response.data.exercise_details
          this.form.injuries = response.data.injuries
          console.log("respuesta API save Historia clínica", response.data)
          swal("Historia clínica guardada", "", "success")

        })
        .catch((error) => {
          console.log(error)
          swal("Ooops", "Hubo un error", "error")
        })
      },

    },
    
    created() {
      this.getDiseases()
      this.getSymptoms()
      this.getNutritionists()
    },

  }

</script>

<style lang="css" scoped>
  
</style>