<template lang="html">

  <div class="container">
    <div class="row">
      <div class="col text-left">
        <h2>Paciente</h2>
        <div class="row">
          <div class="col">
            <div class="card">
              <div class="card-body">
                <p>Nombre: {{ first_name }} {{ last_name }} {{ second_lastname }}</p>
                <p>Correo: {{ email }}</p>
                <p>Teléfono: {{ phone }}</p>
                <p>Género: {{ gender }}</p>
                <p>Estado de Residencia: {{ residence }}</p>
                <p>Edad: </p>
                <p>Peso: {{ weight }}</p>
                <p>Altura: {{ height }}</p>
                <ul id="example-1">
                  Historiales Médicos:
                  <li v-for="(record, index) in records">
                    {{ ++index }}
                    <b-button
                      size="sm"
                      variant="success"
                      :to="{name: 'Record', params: {recordId: record.id}}"
                    >
                      Ver más
                    </b-button>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        <b-button size="sm" variant="primary" :to="{ name:'PatientList' }">Listado</b-button>
        <b-button
          size="sm"
          variant="success"
          :to="{name: 'IMCTest', params: {patientId: patientId}}"
        >
          IMC Test
        </b-button>
        <b-button
          size="sm"
          variant="success"
          :to="{name: 'FatTest', params: {patientId: patientId}}"
        >
          % de Grasa
        </b-button>
        <b-button
          size="sm"
          variant="success"
          :to="{name: 'MuscleTest', params: {patientId: patientId}}"
        >
          % de Músculo
        </b-button>
        <b-button
          size="sm"
          variant="success"
          :to="{name: 'CreateMedicalRecord', params: {patientId: patientId}}"
        >
          Crear Historial
        </b-button>
        <b-button
          size="sm"
          variant="success"
          :to="{name: 'CreateMedicalTracing', params: {patientId: patientId}}"
        >
          Historial de Seguimiento
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
      patientId: this.$route.params.patientId,
      api: 'https://back.pruebasreset.website/api/v1.0/',
      first_name: '',
      last_name: '',
      second_lastname: '',
      email: '',
      phone: '',
      gender: '',
      residence: '',
      age: '',
      weight: '',
      height: '',
      body_mass: '',
      records: []
    }
  },
  methods: {
    getPatient() {
      const path = this.api+`patients/${this.patientId}/`

      axios.get(path).then((response) => {
        this.first_name = response.data.first_name
        this.last_name = response.data.last_name
        this.second_lastname = response.data.second_lastname
        this.email = response.data.email
        this.phone = response.data.phone
        this.gender = response.data.gender
        this.residence = response.data.residence_state
        this.age = response.data.age
        this.weight = response.data.weight
        this.height = response.data.height
        this.body_mass = response.data.body_mass
        this.records = response.data.records
      })
      .catch((error) => {
        console.log(error)
      })
    },
  },

  created(){
    this.getPatient()
  }
}
</script>

<style lang="css" scoped>
</style>