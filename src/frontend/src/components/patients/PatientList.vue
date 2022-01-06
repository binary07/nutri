<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
      
      <div>
        <h2>Pacientes</h2>

        <b-button 
          size="sm"
          variant="primary"
          :to="{name: 'CreatePatient'}"
        >
          Crear Paciente
        </b-button>
      </div>

      <br>

      <div class="col-md 12">
        <b-table stripped hover :items="patients" :fields="fields">
          <template v-slot:cell(action)="data">
            <b-button
              size="sm"
              variant="success"
              :to="{name: 'Patient', params: {patientId: data.item.id}}"
            >
              Ver más
            </b-button>
            <b-button
              size="sm"
              variant="primary"
              :to="{name: 'EditPatient', params: {patientId: data.item.id}}"
            >
              Editar
            </b-button>
            <!-- <b-button
              size="sm"
              variant="danger"
              :to="{name: 'DeletePatient', params: {patientId: data.item.id}}"
            >
              Eliminar
            </b-button> -->          
          </template>
        </b-table>
      </div>
      </div>
    </div>
  </div>
</template>


<script>
  import axios from 'axios';
  export default {
    data() {
      return {
        fields: [
          {key: 'first_name', label: 'Nombre(s)'},
          {key: 'last_name', label: 'Apellido Paterno'},
          {key: 'second_lastname', label: 'Apellido Materno'},
          {key: 'email', label: 'Correo'},
          {key: 'phone', label: 'Teléfono'},
          {key: 'age', label: 'Edad'},
          {key: 'action', label:'Acción'},
        ],
        patients: [],
        api: 'https://back.pruebasreset.website/api/v1.0/',
        // api: 'http://localhost:8000/api/v1.0/',
      }
    },

    methods: {
      getPatients () {
        const path = this.api+`patients/`
        axios.get(path).then((response) => {
          this.patients = response.data;
        })
        .catch((error) => {
          console.log(error)
        })
      },
      // setRating: function (id, rating) {
      //   if (rating >= 0) {
      //     rating = rating;
      //   }else{
      //     rating = 0;
      //   }

      //   $('.p'+id).raty({
      //         readOnly: true,
      //         score: rating
      //      }); 
      //   // alert(id);
      // },
    },

    created(){
      this.getPatients()
    },
  }

</script>

<style lang="css" scoped>
  
</style>