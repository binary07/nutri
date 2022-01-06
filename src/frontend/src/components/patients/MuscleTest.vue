<template lang="html">

  <div class="container">
    
    <div class="row">
      <div class="col text-left">
        <h2>% de Grasa Corporal</h2>
      </div>
    </div>

    <div class="row">
      <div class="col">
        <div class="card">
          <div class="card-body">
            
            <form @submit="onSubmit">

              <div class="form-group row">
                <label for="gender" class="col-sm-2 col-form-label">
                  Género:
                </label>
                <div class="col-sm-6">
                  <select 
                    name="gender"
                    class="form-control"
                    v-model.trim="form.gender"
                  >
                    <option value="Femenino">
                      Femenino
                    </option>
                    <option value="Masculino">
                      Masculino
                    </option>
                  </select>
                </div>
              </div>

              <div class="form-group row">
                <label for="birthday" class="col-sm-2 col-form-label">
                  Fecha de Nacimiento
                </label>
                <div class="col-sm-6">
                  <input 
                    type="date"
                    name="birthday"
                    class="form-control"
                    v-model.trim="form.birthday"
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
                    placeholder="Ej: 25"
                    name="body_muscle"
                    step="0.01" 
                    class="form-control"
                    v-model.trim="form.body_muscle"
                  >
                </div>
              </div>

              <div class="rows">
                <div class="col text-left">
                  <b-button type="submit" variant="primary">
                    Enviar
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
        api: 'https://back.pruebasreset.website/api/v1.0/',
        form: {
          gender: '',
          body_muscle: '',
          birthday: '',
        }
      }
    },

    methods: {
      onSubmit(evt) {

        evt.preventDefault()

        const path =  this.api+`patients/${this.patientId}/`;

        axios.put(path, this.form).then((response) => {

          this.form.gender = response.data.gender
          this.form.body_muscle = response.data.body_muscle
          this.form.birthday = response.data.birthday

          swal("Actualizado correctamente", "", "success")

        })
        .catch((error) => {
          swal("Ooops", "Hubo un error", "error")
        })
      },

      getPatient() {

        const path =  this.api+`patients/${this.patientId}/`;
        
        axios.get(path).then((response) => {

          this.form.gender = response.data.gender
          this.form.body_muscle = response.data.body_muscle
          this.form.birthday = response.data.birthday

        })
        .catch((error) => {
          console.log(error)
        })
      },
    },
    
    created() {
      this.getPatient()
    },

  }

</script>

<style lang="css" scoped></style>
