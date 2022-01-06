<template lang="html">

  <div class="container">
    
    <div class="row">
      <div class="col text-left">
        <h2>Modificar Datos</h2>
      </div>
    </div>

    <div class="row">
      <div class="col">
        <div class="card">
          <div class="card-body">
            
            <form @submit="onSubmit">

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
                <label for="last_name" class="col-sm-2 col-form-label">
                  Nombre(s)
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
                    <option value="Otro">
                      Otro
                    </option>
                  </select>
                </div>
              </div>

              <div class="form-group row">
                <label for="residence_state" class="col-sm-2 col-form-label">
                  Estado de Residencia:
                </label>
                <div class="col-sm-6">
                  <select 
                    name="residence_state"
                    class="form-control"
                    v-model.trim="form.residence_state"
                  >
                    <option value="Aguascalientes">
                      Aguascalientes
                    </option>
                    <option value="Baja California">
                      Baja California
                    </option>
                    <option value="Baja California Sur">
                      Baja California Sur
                    </option>
                    <option value="Campeche">
                      Campeche
                    </option>
                    <option value="Coahuila">
                      Coahuila
                    </option>
                    <option value="Colima">
                      Colima
                    </option>
                    <option value="Chiapas">
                      Chiapas
                    </option>
                    <option value="Chihuahua">
                      Chihuahua
                    </option>
                    <option value="CDMX">
                      CDMX
                    </option>
                    <option value="Durango">
                      Durango
                    </option>
                    <option value="Edo. Méx">
                      Edo. Méx
                    </option>
                    <option value="Guanajuato">
                      Guanajuato
                    </option>
                    <option value="Guerrero">
                      Guerrero
                    </option>
                    <option value="Hidalgo">
                      Hidalgo
                    </option>
                    <option value="Jalisco">
                      Jalisco
                    </option>
                    <option value="Michoacán">
                      Michoacán
                    </option>
                    <option value="Morelos">
                      Morelos
                    </option>
                    <option value="Nayarit">
                      Nayarit
                    </option>
                    <option value="Nuevo León">
                      Nuevo León
                    </option>
                    <option value="Oaxaca">
                      Oaxaca
                    </option>
                    <option value="Puebla">
                      Puebla
                    </option>
                    <option value="Queretaro">
                      Queretaro
                    </option>
                    <option value="Quintana Roo">
                      Quintana Roo
                    </option>
                    <option value="San Luis Potosí">
                      San Luis Potosí
                    </option>
                    <option value="Sinaloa">
                      Sinaloa
                    </option>
                    <option value="Sonora">
                      Sonora
                    </option>
                    <option value="Tabasco">
                      Tabasco
                    </option>
                    <option value="Tamaulipas">
                      Tamaulipas
                    </option>
                    <option value="Tlaxcala">
                      Tlaxcala
                    </option>
                    <option value="Veracruz">
                      Veracruz
                    </option>
                    <option value="Yucatán">
                      Yucatán
                    </option>
                    <option value="Zacatecas">
                      Zacatecas
                    </option>
                  </select>
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
        api: 'https://back.pruebasreset.website/api/v1.0/',
        form: {
          first_name: '',
          last_name: '',
          second_lastname: '',
          email: '',
          phone: '',
          gender: '',
          residence_state: '',
        }
      }
    },

    methods: {
      onSubmit(evt) {

        evt.preventDefault()

        const path =  this.api+`patients/${this.patientId}/`;

        axios.put(path, this.form).then((response) => {

          this.form.first_name = response.data.first_name
          this.form.last_name = response.data.last_name
          this.form.second_lastname = response.data.second_lastname
          this.form.email = response.data.email
          this.form.phone = response.data.phone
          this.form.gender = response.data.gender
          this.form.residence_state = response.data.residence_state

          swal("Actualizado correctamente", "", "success")

        })
        .catch((error) => {
          swal("Ooops", "Hubo un error", "error")
        })
      },

      getPatient() {

        const path =  this.api+`patients/${this.patientId}/`;
        
        axios.get(path).then((response) => {

          this.form.first_name = response.data.first_name
          this.form.last_name = response.data.last_name
          this.form.second_lastname = response.data.second_lastname
          this.form.email = response.data.email
          this.form.phone = response.data.phone
          this.form.gender = response.data.gender
          this.form.residence_state = response.data.residence_state

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

<style lang="css" scoped>
  
</style>