<template lang="html">

  <div class="container">
    
    <div class="row">
      <div class="col text-left">
        <h2>Nueva cita</h2>
      </div>
    </div>

    <div class="row">
      <div class="col">
        <div class="card">
          <div class="card-body">
            
            <form @submit="onSubmit">

              <div class="form-group row">
                <label for="nutritionist" class="col-sm-2 col-form-label">
                  Nutriologo
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Pedro"
                    name="nutritionist"
                    class="form-control"
                    v-model.trim="form.nutritionist"
                  >
                </div>
              </div>


              <div class="form-group row">
                <label for="app-date" class="col-sm-2 col-form-label">
                  Fecha
                </label>
                <div class="col-sm-6">
                  <input 
                    type="date"
                    name="app-date"
                    class="form-control"
                    v-model.trim="form.date"
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
                    class="btn-large-space"
                    :to="{name: 'PatientList'}"
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
        // api: 'http://localhost:8000/api/v1.0/',
        api: `https://binary07.pythonanywhere.com/api/v1.0/`,
        form: {
          nutritionist: '',
          date: '',
        }
      }
    },

    methods: {
      onSubmit(evt) {

        evt.preventDefault()

        const path =  this.api+`patients/`;

        axios.post(path, this.form).then((response) => {
          
          this.form.nutritionist = response.data.nutritionist
          this.form.date = response.data.date

          swal("Cuta registrada correctamente", "", "success")

        })
        .catch((error) => {
          console.log(error)
          swal("Ooops", "Hubo un error", "error")
        })
      },

    },
    
    created() {
      
    },

  }

</script>

<style lang="css" scoped>
  
</style>