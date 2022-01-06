<template lang="html">
  <div class="container">
    
    <div class="row">
      <div class="col">
        <h3>¿Deseas eliminar a este nutriologo?</h3>
        <p>Nutriologo: {{ this.element.first_name }} {{ this.element.last_name }} {{ this.element.second_lastname }}</p>
      </div>      
    </div>

    <div class="row">
      <div class="col">
        <b-button v-on:click="deleteNutritionist" variant="danger">
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
        nutritionistId: this.$route.params.nutritionistId,
        api: 'https://back.pruebasreset.website/api/v1.0/',
        element: {
          first_name: '',
          last_name: '',
          second_lastname: '',
        }
      }
    },
    methods: {

      getNutritionist() {

        const path =  this.api+`nutritionists/${this.nutritionistId}/`
        
        axios.get(path).then((response) => {

          this.element.first_name = response.data.first_name
          this.element.last_name = response.data.last_name
          this.element.second_lastname = response.data.second_lastname

        })
        .catch((error) => {
          console.log(error)
        })
      },

      deleteNutritionist() {
        const path =  this.api+`nutritionists/${this.nutritionistId}/`

        axios.delete(path).then((response) => {
          location.href = '/nutriologos'
        })
        .catch((error) => {
          swal("No es posible eliminar el libro", "", "error")
        })
      }
    },
    
    created() {
      this.getNutritionist()
    },
  }

</script>

<style lang="css">
  
</style>