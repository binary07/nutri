<template lang="html">
  <div class="container"><br>
    <div class="alert alert-info">
      <button type="button" class="close" data-dismiss="alert" aria-label="Close"> <span aria-hidden="true">×</span> </button>
      <h3 class="text-info"><i class="fa fa-check-circle"></i> Bienvenido <b v-text="patient.first_name"></b></h3> Busca a tu nutriólog@ preferido y ponte en contacto para realizar tu consulta.
  </div>
    <input type="text" style="font-size:20px;text-align: center;" @keyup="buscar()" v-model="busca" placeholder="buscar aquí. Ej. Lic. Nutrición" class="form-control">
    <div class="steamline mt-0" style="scroll-y: auto;">
        <div class="sl-item" v-for="nutrionist in nutritionists" style="margin-left: -20px;margin-bottom:0px;">
            <div style="background:#FAD7A0; display:inline-block;border-radius: .5rem;margin-right: auto;margin-left: auto;padding: 15px; padding-bottom: 45px;  max-width:auto; width: 100%;">
              <div class="sl-left" style="margin-left: 0px;"> 
                <img src="/static/assets/images/users/1.jpg" style="width: 40px; height: 40px;display: inline;border-radius: 2rem; margin-left: 0%;">
              </div>
              <a style="font-size: 18px; font-weight: bold; color: blue;" class="sl-date" v-text="nutrionist.first_name+' '+nutrionist.last_name+' '+nutrionist.second_lastname + ''"></a> 
             
              <br>
              <span  style="color: #333;font-size: 15px; font-weight: bold;padding-right: 2px; " class="mt-1 font-light" v-text="nutrionist.degree"></span> 
              <br><b style="color: #333;text-align: center;width: 100%;"> Cédula: <small v-text="nutrionist.license" style="font-size:15px;color: #333;"></small></b>
              <!-- <br> -->
                <div style="text-align: center;margin-bottom: -35px;">
                <a style="padding:0px;margin:0px;display: inline; margin-left: 5px;font-size: 20px;color: black;pointer:cursor;text-align: center;"><i class="fa fa-phone" style="color: black;max-width: 8%;" @click="makeContact(nutrionist)"></i></a>
                <div id="default-star-rating" style="font-size: 20px;">* * * * *</div>
                  <!-- <div id="read-only-stars" data-score="4"></div> -->
                  <!-- <div :class="'p'+nutrionist.id" v-bind="[setRating(nutrionist.id, 4)]" style="display: inline;text-align: center;" > -->
                  </div>
                </div>
            </div>
        </div>
    <!-- </div> -->
<!--   <div class="row">
    <div class="col text-left">
    
    <div>
      <h2>Nutriologos</h2>

      <b-button 
        size="sm"
        variant="primary"
        :to="{name: 'CreateNutritionist'}"
      >
        Crear Nutriologo
      </b-button>
    </div>

    <br>

    <div class="col-md 12">
      <b-table stripped hover :items="nutritionists" :fields="fields">
        <template v-slot:cell(action)="data">
          <b-button
            size="sm"
            variant="primary"
            :to="{name: 'EditNutritionist', params: {nutritionistId: data.item.id}}"
          >
            Editar
          </b-button>
          <b-button
            size="sm"
            variant="danger"
            :to="{name: 'DeleteNutritionist', params: {nutritionistId: data.item.id}}"
          >
            Eliminar
          </b-button>          
        </template>
      </b-table>
    </div>
    </div>
  </div> -->
  </div>
</template>


<script>
  import axios from 'axios';
  import swal from 'sweetalert';

  export default {
    data() {
      return {
        fields: [
          {key: 'first_name', label: 'Nombre(s)'},
          {key: 'last_name', label: 'Apellido Paterno'},
          {key: 'second_lastname', label: 'Apellido Materno'},
          {key: 'email', label: 'Correo'},
          {key: 'phone', label: 'Teléfono'},
          {key: 'license', label: 'Cédula'},
          {key: 'degree', label: 'Título'},
          {key: 'specialties', label: 'Especialidad(es)'},
          {key: 'action', label: ''},
        ],
        nutritionists: [],
        busca : '',
        patient:{
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
            estatus_imc:'',
            estatus_grasa:'',
            estatus_musculo:''
        },
        patient_id: this.$route.params.id,
        api: 'https://back.pruebasreset.website/api/v1.0/',
        // api: 'http://localhost:8000/api/v1.0/',
      }
    },
    created(){
      this.getNutritionists();
      this.getPatient();
    },
    methods: {
      getPatient: function () {
            axios.get(this.api+`patients/${this.patient_id}/`).then(res => {
              this.patient = res.data;
              console.log("result api patient",res.data);
            }).catch(err => {
              console.log(err);
            });
      },
        buscar () {
          const path = this.api+`nutritionists/?search=`+this.busca;
          
          axios.get(path).then((response) => {
            console.log("respuesta search", response.data);
            this.nutritionists = response.data;
          })
          .catch((error) => {
            console.log(error)
          })
      },
      getNutritionists () {
          const path = this.api+`nutritionists/`;
          axios.get(path).then((response) => {
            this.nutritionists = response.data;
          })
          .catch((error) => {
            console.log(error)
          })
      },
      makeContact: function (nutrionist) {
        // alert(this.patient_id+' nutrionist_id'+nutrionist_id); 
        var data = { patient: this.patient_id, nutrionist: nutrionist.id };
        swal({
          title: "Estas seguro de contactar a "+nutrionist.first_name+"?",
          text: "Una vez contactado, apareceras en su lista de pacientes del nutriólogo.",
          icon: "warning",
          buttons: true,
          buttons:['cancelar','sí, contactar'],
          dangerMode: true,
        })
        .then((contact) => {
          if (contact) {
            axios.get(this.api+`contact/`, data).then(res => {
              // alert("contacto realizado");
              console.log("contacto realizado", res.data);
              window.open('tel:'+nutrionist.phone, '_blank');
            })
            .catch((error) => {
              console.log(error)
            })
          }
        });

        
      }
    },

  }

</script>

<style lang="css" scoped>
  
</style>