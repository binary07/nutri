<template lang="html">
  
  <div class="container">
    
    <div class="row">
      <div class="col text-left">
        <h2>Seguimiento Clínico</h2>
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
                <label for="weight" class="col-sm-2 col-form-label">
                  Peso
                </label>
                <div class="col-sm-6">
                  <input 
                    type="number"
                    placeholder="%"
                    name="weight"
                    class="form-control"
                    step="0.01"
                    v-model="form.weight"
                  >
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
                <label for="kg_muscle" class="col-sm-2 col-form-label">
                  Kg de Músculo
                </label>
                <div class="col-sm-6">
                  <input 
                    type="number"
                    placeholder="%"
                    name="kg_muscle"
                    class="form-control"
                    step="0.01" 
                    v-model="form.kg_muscle"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="igv" class="col-sm-2 col-form-label">
                  IGV
                </label>
                <div class="col-sm-6">
                  <input 
                    type="number"
                    placeholder="%"
                    name="igv"
                    class="form-control"
                    step="0.01" 
                    v-model="form.igv"
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
                <label for="quadriceps" class="col-sm-2 col-form-label">
                  Cuádriceps (cm)
                </label>
                <div class="col-sm-6">
                  <input 
                    type="number"
                    placeholder="cm"
                    name="quadriceps"
                    step="0.01" 
                    class="form-control"
                    v-model="form.quadriceps"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="meal_times" class="col-sm-2 col-form-label">
                  Tiempos de Comida
                </label>
                <div class="col-sm-6">
                  <input 
                    type="number"
                    placeholder="cm"
                    name="meal_times"
                    class="form-control"
                    v-model="form.meal_times"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="schedule" class="col-sm-2 col-form-label">
                  Horarios
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Detalla tu segunda colacion"
                    name="schedule"
                    class="form-control"
                    v-model="form.schedule"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="amounts" class="col-sm-2 col-form-label">
                  Cantidades
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Detalla tu segunda colacion"
                    name="amounts"
                    class="form-control"
                    v-model="form.amounts"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="water" class="col-sm-2 col-form-label">
                  Agua
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Detalla tu segunda colacion"
                    name="water"
                    class="form-control"
                    v-model="form.water"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="exercise" class="col-sm-2 col-form-label">
                  Ejercicio
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Detalla tu segunda colacion"
                    name="exercise"
                    class="form-control"
                    v-model="form.exercise"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="personal_goals" class="col-sm-2 col-form-label">
                  Logros/Metas personales
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Detalla tu segunda colacion"
                    name="personal_goals"
                    class="form-control"
                    v-model="form.personal_goals"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="weekend_meals" class="col-sm-2 col-form-label">
                  Alimentación de fines de semana
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Detalla tu segunda colacion"
                    name="weekend_meals"
                    class="form-control"
                    v-model="form.weekend_meals"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="alcohol" class="col-sm-2 col-form-label">
                  Alcohol
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Detalla tu segunda colacion"
                    name="alcohol"
                    class="form-control"
                    v-model="form.alcohol"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="gastric_symptoms" class="col-sm-2 col-form-label">
                  Síntomas gástricos
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Detalla tu segunda colacion"
                    name="gastric_symptoms"
                    class="form-control"
                    v-model="form.gastric_symptoms"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="comments" class="col-sm-2 col-form-label">
                  Comentarios
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Detalla tu segunda colacion"
                    name="comments"
                    class="form-control"
                    v-model="form.comments"
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
          weight: '',
          body_fat: '',
          body_muscle: '',
          kg_muscle: '',
          waist: '',
          belly: '',
          hip: '',
          biceps: '',
          quadriceps: '',
          meal_times: '',
          schedule: '',
          amounts: '',
          water: '',
          exercise: '',
          personal_goals: '',
          weekend_meals: '',
          alcohol: '',
          gastric_symptoms: '',
          comments: '',
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

      onSubmit(evt) {

        evt.preventDefault()

        const path =  this.api+`medicalrecords/`;
        console.log("enviar Historia clínica a API", this.form);
        axios.post(path, this.form).then((response) => {

          this.form.patient = parseInt(this.patientId)
          this.form.nutritionist = response.data.nutritionist
          this.form.weight = response.data.weight
          this.form.body_fat = response.data.body_fat
          this.form.body_muscle = response.data.body_muscle
          this.form.kg_muscle = response.data.kg_muscle
          this.form.waist = response.data.waist
          this.form.belly = response.data.belly
          this.form.hip = response.data.hip
          this.form.biceps = response.data.biceps
          this.form.quadriceps = response.data.quadriceps
          this.form.meal_times = response.data.meal_times
          this.form.schedule = response.data.schedule
          this.form.amounts = response.data.amounts
          this.form.water = response.data.water
          this.form.exercise = response.data.exercise
          this.form.personal_goals = response.data.personal_goals
          this.form.weekend_meals = response.data.weekend_meals
          this.form.alcohol = response.data.alcohol
          this.form.gastric_symptoms = response.data.gastric_symptoms
          this.form.comments = response.data.comments
          
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
      this.getNutritionists()
    },

  }

</script>

<style lang="css" scoped>
  
</style>