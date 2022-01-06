<template lang="html">
  
  <div class="container">
    
    <div class="row">
      <div class="col text-left">
        <h2>Editar Nutriologo</h2>
      </div>
    </div>

    <div class="row">
      <div class="col">
        <div class="card">
          <div class="card-body">
            
            <form @submit="onSubmit">

              <div class="form-group row">
                <label for="first_name" class="col-sm-2 col-form-label">
                  Nombre
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Nombre(s)"
                    name="first_name"
                    class="form-control"
                    v-model.trim="form.first_name"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="last_name" class="col-sm-2 col-form-label">
                  Apellido Paterno
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Apellido Paterno"
                    name="last_name"
                    class="form-control"
                    v-model.trim="form.last_name"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="second_lastname" class="col-sm-2 col-form-label">
                  Apellido Materno
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="Apellido Materno"
                    name="second_lastname"
                    class="form-control"
                    v-model.trim="form.second_lastname"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="email" class="col-sm-2 col-form-label">
                  Correo
                </label>
                <div class="col-sm-6">
                  <input 
                    type="email"
                    placeholder="ejemplo@gmail.com"
                    name="email"
                    class="form-control"
                    v-model.trim="form.email"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="phone" class="col-sm-2 col-form-label">
                  Teléfono
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    placeholder="5511223344"
                    name="phone"
                    class="form-control"
                    v-model.trim="form.phone"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="license" class="col-sm-2 col-form-label">
                  Cédula
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    name="license"
                    class="form-control"
                    v-model.trim="form.license"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="degree" class="col-sm-2 col-form-label">
                  Título Profesional
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    name="degree"
                    class="form-control"
                    v-model.trim="form.degree"
                  >
                </div>
              </div>

              <div class="form-group row">
                <label for="specialties" class="col-sm-2 col-form-label">
                  Especialidad(es)
                </label>
                <div class="col-sm-6">
                  <input 
                    type="text"
                    name="specialties"
                    class="form-control"
                    v-model.trim="form.specialties"
                  >
                </div>
              </div>

              <div class="rows">
                <div class="col text-left">
                  <b-button type="submit" variant="primary">
                    Editar
                  </b-button>
                  <b-button 
                    type="submit"
                    class="btn-large-space"
                    :to="{name: 'NutritionistList'}"
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
        nutritionistId: this.$route.params.nutritionistId,
        api: 'https://back.pruebasreset.website/api/v1.0/',
        form: {
          first_name: '',
          last_name: '',
          second_lastname: '',
          email: '',
          phone: '',
          license: '',
          degree: '',
          specialties: '',
        }
      }
    },

    methods: {
      onSubmit(evt) {

        evt.preventDefault()

        const path =  this.api+`nutritionists/${this.nutritionistId}/`

        axios.put(path, this.form).then((response) => {
          
          this.form.first_name = response.data.first_name
          this.form.last_name = response.data.last_name
          this.form.second_lastname = response.data.second_lastname
          this.form.email = response.data.email
          this.form.phone = response.data.phone
          this.form.license = response.data.license
          this.form.degree = response.data.degree
          this.form.specialties = response.data.specialties

          swal("Actualizado correctamente", "", "success")

        })
        .catch((error) => {
          swal("Ooops", "Hubo un error", "error")
        })
      },

      getNutritionist() {

        const path =  this.api+`nutritionists/${this.nutritionistId}/`
        
        axios.get(path).then((response) => {

          this.form.first_name = response.data.first_name
          this.form.last_name = response.data.last_name
          this.form.second_lastname = response.data.second_lastname
          this.form.email = response.data.email
          this.form.phone = response.data.phone
          this.form.license = response.data.license
          this.form.degree = response.data.degree
          this.form.specialties = response.data.specialties

          console.log(this.form.specialties)

        })
        .catch((error) => {
          console.log(error)
        })
      },
    },
    
    created() {
      this.getNutritionist()
    },

  }

</script>

<style lang="css" scoped>
  
</style>