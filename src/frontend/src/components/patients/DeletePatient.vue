<template lang="html">
  <div class="container">
    
    <div class="row">
      <div class="col">
        <h3>¿Deseas eliminar a este paciente?</h3>
        <p>Paciente: {{ this.element.first_name }} {{ this.element.last_name }} {{ this.element.second_lastname }}</p>
      </div>      
    </div>

    <div class="row">
      <div class="col">
        <b-button v-on:click="deletePatient" variant="danger">
          Eliminar
        </b-button>
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
        element: {
          first_name: '',
          last_name: '',
          second_lastname: '',
        }
      }
    },

    methods: {

      getPatient() {

        const path =  this.api+`patients/${this.patientId}/`;
        
        axios.get(path).then((response) => {

          this.element.first_name = response.data.first_name
          this.element.last_name = response.data.last_name
          this.element.second_lastname = response.data.second_lastname

        })
        .catch((error) => {
          console.log(error)
        })
      },

      deletePatient() {
        const path =  this.api+`patients/${this.patientId}/`;

        axios.delete(path).then((response) => {
          location.href = '/pacientes'
        })
        .catch((error) => {
          swal("No es posible eliminar el libro", "", "error")
        })
      }
    },
    
    created() {
      this.getPatient()
    },
  }

</script>

<style lang="css">
  
</style>