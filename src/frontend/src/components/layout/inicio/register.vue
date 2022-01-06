<template>
	<div class="container">

    <div id="myModal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title" style="text-align: center;">Agregar especialidad</h4> 
                </div>
                <div class="modal-body">
                    <div class="panel-body" style="height: auto; overflow-y: scroll;padding: 0px;width: 100%;">
                        <input type="text" v-model="name" class="form-control" placeholder="tu especialidad">
                    </div>  
                </div>
                <div class="modal-footer">
                    <button @click="addEspeciality()" class="btn btn-info">Guardar</button>
                    <button type="button" class="btn btn-danger" data-dismiss="modal" id="cerrarM">Cerrar</button>
                </div>
            </div>
        </div>
    </div>

		<div style="scroll-y: auto;">
            <div class="auth-box" style="margin-top: 15%;">
                <div id="loginform" style="background: none;padding: 5%;">
                    <div class="logo" style="text-align: center;">
                        <h4 style="color: green;" v-if="!isRegisterNutrionist">Registro Paciente</h4>
                        <h4 style="color: green;" v-else>Registro Nutriólogo</h4>
                        <h5 v-if="!isRegisterNutrionist" class="font-medium mb-3">Accede al repositorio de nutriólogos expertos y comienza tu programa preferido</h5>
                        <h5 v-else class="font-medium mb-3">Aumenta tu cartera de clientes</h5>
                        <div class="row">
                            <div class="col-xs-12 col-sm-12 col-md-12 mt-2 text-center">
                               <ul class="social">
                                    <li><div class="a-facebook"><i style="font-size:35px;" class="fab fa-facebook"></i></div></li>
                                    <li><div class="a-instagram"><i style="font-size:35px;" class="fab fa-instagram"></i></div></li>
                                    <li><div class="a-google"><i style="font-size:35px;" class="fab fa-google"></i></div></li>
                                </ul>
                            </div>
                        </div>
                    </div><br><br>
                    <!-- Form -->
                    <div class="row">
                        <div class="col-md-12">
                            	<div class="form-row">
                              		<div class="col-md-4 form-group">
                                    <input type="text" class="form-control form-control-lg" placeholder="Nombre(s)" aria-label="Nombre(s)" id="nombres" v-model="nombres" aria-describedby="basic-addon1">
  	                                </div>
  	                                <div class="col-md-4 form-group">
  	                                    
                                    <input type="text" class="form-control form-control-lg" placeholder="Apellidos" aria-label="Apellidos" id="apellidos" v-model="apellidos" aria-describedby="basic-addon1">
  	                                </div>
                                    <div class="col-md-4 form-group">
                                      <input type="email" class="form-control form-control-lg" placeholder="Email" aria-label="Email" id="email" v-model="email" aria-describedby="basic-addon1">
                                  </div>
                              </div>
                              <div class="form-row">
	                                <div class="col-md-4 form-group">
	                                    <input type="text" class="form-control form-control-lg" placeholder="Teléfono" aria-label="Teléfono" id="telefono" v-model="phone" aria-describedby="basic-addon1" maxlength="10">
	                                </div>
                                  <div v-if="!isRegisterNutrionist" class="col-md-4 form-group">
                                      <select 
                                        name="gender"
                                        class="form-control"
                                        v-model="gender"
                                      >
                                        <option value="">Sexo</option>
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
                                  <div v-if="!isRegisterNutrionist" class="col-md-4 form-group">
                                      <select 
                                        name="residence_state"
                                        class="form-control"
                                        v-model="residence_state"
                                        required="" 
                                      >
                                      <option value="">Estado</option>
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
                                  <div v-if="isRegisterNutrionist" class="col-md-4 form-group">
                                      <input type="text" class="form-control form-control-lg" placeholder="Cédula" aria-label="Cédula" id="cedula" v-model="license" aria-describedby="basic-addon1">
                                  </div>
                                  <div v-if="isRegisterNutrionist" class="col-md-4 form-group">
                                      <input type="text" class="form-control form-control-lg" placeholder="Título" aria-label="Título" id="titulo" v-model="degree" aria-describedby="basic-addon1">
                                  </div>
	                                <div v-if="isRegisterNutrionist" class="input-group mb-3">
	                                    <select class="form-control" v-model="especialidades"  multiple>
	                                    	<!-- <option>Especialidad</option> -->
	                                    	<option v-for="esp in specialties" :value="esp.id" v-text="esp.name"></option>
	                                    	
	                                    </select>
	                                       <ul class="social">
                										        <li><a title="Agregar un especialidad" href="#" data-toggle="modal" data-target="#myModal"  class="a-pluss" style="background-color: gray; color: white;"><i class="fa fa-plus" style="font-size: 15px;margin-top: 10px;"></i></a></li>
                										    </ul> 
	                                </div>
                                  </div>
                                  <div class="form-row">
	                                <div class="col-md-4 form-group">
	                                    <input type="password" class="form-control form-control-lg" placeholder="Contraseña" aria-label="Contraseña" id="password" v-model="password" aria-describedby="basic-addon1">
	                                </div>
                                  <div class="col-md-4 form-group">
                                    <div class="col-md-12">
                                        <div class="custom-control custom-checkbox">
                                            <input type="checkbox" class="custom-control-input" id="customCheck1">
                                            <label class="custom-control-label" for="customCheck1" style="font-size: 15px;text-align:left;"> Acepto los términos y condiciones de uso.</label>
                                            <!-- <a href="/recovery" id="to-recover" class="text-dark float-right"><i class="fa fa-lock mr-1"></i> olvidaste tu pwd?</a> -->
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-4 form-group">
                                    <div style="text-align:center;">
                                        <a style="text-align: center;" v-if="!isRegisterNutrionist" href="#" class="btn btn-block btn-lg btn-info" @click="registerPatient()">Registro</a>
                                        <a style="text-align: center;" v-if="isRegisterNutrionist" href="#" class="btn btn-block btn-lg btn-info" @click="registerNutrionist()">Registro</a>
                                    </div>
                                </div>
                                </div>
                                
                                <!-- social -->
                                <div>
                                    <div style="text-align: center; margin: 10px;">
                                        Ya tienes una cuenta? <a href="/login" class="text-info ml-1"><b>Iniciar sesión</b></a>
                                    </div>
                                    <div v-if="!isRegisterNutrionist" style="text-align: center; margin: 10px;">
                                        Eres un nutriólogo ? <a href="#" @click="changeForm(2)" class="text-info ml-1"><b>Registro nutriólogo</b></a>
                                    </div>
                                    <div v-if="isRegisterNutrionist" style="text-align: center; margin: 0px;">
                                        Eres un paciente ? <a href="#" @click="changeForm(1)" class="text-info ml-1"><b>Registro paciente</b></a>
                                    </div>
                                </div>
                           
                        </div>
                    </div>
                </div>
            </div>
        </div>
	</div>
</template>

<style scoped>
/*--------------------------------------------------------------
# Hero Section
--------------------------------------------------------------*/
#hero {
  width: 100%;
  height: 90vh;
  /*background: url("../img/hero-bg.jpg") top center;*/
  background-size: cover;
  position: relative;
  margin-bottom: -200px;
}

#hero .container {
  position: relative;
}

#hero h1 {
  margin: 0;
  font-size: 48px;
  font-weight: 700;
  line-height: 56px;
  text-transform: uppercase;
  color: #2c4964;
}

#hero h2 {
  color: #2c4964;
  margin: 10px 0 0 0;
  font-size: 24px;
}

#hero .btn-get-started {
  font-family: "Raleway", sans-serif;
  text-transform: uppercase;
  font-weight: 500;
  font-size: 14px;
  letter-spacing: 1px;
  display: inline-block;
  padding: 12px 35px;
  margin-top: 30px;
  border-radius: 50px;
  transition: 0.5s;
  color: #fff;
  background: #1977cc;
}

#hero .btn-get-started:hover {
  background: #3291e6;
}

@media (min-width: 1024px) {
  #hero {
    background-attachment: fixed;
  }
}

@media (max-width: 992px) {
  #hero {
    margin-bottom: 0;
    height: 100vh;
  }
  #hero .container {
    padding-bottom: 63px;
  }
  #hero h1 {
    font-size: 28px;
    line-height: 36px;
  }
  #hero h2 {
    font-size: 18px;
    line-height: 24px;
    margin-bottom: 30px;
  }
}

@media (max-height: 500px) {
  #hero {
    height: auto;
  }
}

.breadcrumbs {
  padding: 20px 0;
  background-color: #f1f7fd;
  min-height: 40px;
  margin-top: 120px;
}

@media (max-width: 992px) {
  .breadcrumbs {
    margin-top: 63px;
  }
}

.breadcrumbs h2 {
  font-size: 24px;
  font-weight: 300;
  margin: 0;
}

@media (max-width: 992px) {
  .breadcrumbs h2 {
    margin: 0 0 10px 0;
  }
}

.breadcrumbs ol {
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  padding: 0;
  margin: 0;
  font-size: 14px;
}

.breadcrumbs ol li + li {
  padding-left: 10px;
}

.breadcrumbs ol li + li::before {
  display: inline-block;
  padding-right: 10px;
  color: #6c757d;
  content: "/";
}

@media (max-width: 768px) {
  .breadcrumbs .d-flex {
    display: block !important;
  }
  .breadcrumbs ol {
    display: block;
  }
  .breadcrumbs ol li {
    display: inline-block;
  }
}

    .social li {
      display: inline-block;
      padding-right: 16px;
      text-align: center;
    }
    .social li:last-child { padding-right: 0; }
    .social li a {
      display: block;
      background: transparent;
      width: 35px;
      height: 35px;
      line-height: 35px;
      border: 1px solid #c1c6c8;
      color: #c1c6c8;
      border-radius: 50%;
      transition: all 0.3s ease-in-out;
    }
    .social2 li a {
      display: block;
      background: gray;
      width: 25px;
      height: 25px;
      line-height: 35px;
      border: 1px solid #c1c6c8;
      color: #c1c6c8;
      border-radius: 50%;
      transition: all 0.3s ease-in-out;
    }
    .social li .a-facebook:hover {
      background: #3b5998;
      color: #fff;
      border-color: #3b5998;
    }
    .social li .a-twitter:hover {
      background: #55acee;
      color: #fff;
      border-color: #55acee;
    }
    .social li .a-google-plus:hover {
      background: #dc4e41;
      color: #fff;
      border-color: #dc4e41;
    }
    .social li .a-pluss:hover {
      background: gray;
      color: #000;
      border-color: #dc4e41;
    }
</style>

<script>
    
    import axios from 'axios'
    import swal from 'sweetalert'

    export default {
        name: 'register',
        data () {
        	return {
		        isRegisterNutrionist: false,
            api: 'https://back.pruebasreset.website/api/v1.0/',
            // api: 'http://localhost:8000/api/v1.0/',
		        specialties: [],
            nombres: '',
            apellidos: '',
            email: '',
            phone: '',
            license: '',
            degree: '',
            especialidades: [],
            gender: '',
            residence_state: '',
            password: '',
            name: ''
		    }
	    },
	    created(){
	    	this.getEspecialidades();  
	    },
        methods:{
            addEspeciality: function () {

              var form = {
                name: this.name
              }

              console.log("form register patient", form);
              axios.post(this.api+'specialties/', form).then((res) => {
                console.log("response especialidad",res.data);
                this.specialties.push(res.data);
                this.name = '';
                swal("Especialidad agregada correctamente", "", "success");
              }).catch((error) => {
                swal("Ooops", "Hubo un error", "error")
              });

            },
            registerPatient: function () {
            	var apellidos = this.apellidos;

              var last_name = apellidos.split(' ')[0];
              var second_lastname = apellidos.split(' ')[1];

              var form = {
                username: this.phone,
                first_name: this.nombres,
                last_name: last_name,
                second_lastname: second_lastname,
                email: this.email,
                phone: this.phone,
                gender: this.gender,
                residence_state: this.residence_state,
                password: this.password
              }

              console.log("form register patient", form);
              axios.post(this.api+'patients/', form).then((res) => {
                window.location = '/test/'+res.data.id+'/';
                console.log(res.data);
                swal("Bienvenido paciente, tu registro se realizó exitosamente", "", "success");
              }).catch((error) => {
                swal("Ooops", "Hubo un error", "error")
              });
            },
            registerNutrionist: function () {
            	var apellidos = this.apellidos;

            	var last_name = apellidos.split(' ')[0];
            	var second_lastname = apellidos.split(' ')[1];

                var form = {
                  username: this.phone,
                  first_name: this.nombres,
                  last_name: last_name,
                  second_lastname: second_lastname,
                  email: this.email,
                  phone: this.phone,
                  license: this.license,
                  degree: this.degree,
                  specialties: this.especialidades,
                  password: this.password
                }

                console.log("form register nutrionist", form);

                axios.post(this.api+'nutritionists/', form).then((res) => {
                  window.location = '/pacientes';
                  swal("Bienvenido nutriologo, tu registro se realizó exitosamente", "", "success");
                }).catch((error) => {
                  swal("Ooops", "Hubo un error", "error")
                });
            },
            changeForm: function (op) {
            	switch(op){
            		case 1:
            			this.isRegisterNutrionist = false;
            			console.log("case 1");
            		break;
            		case 2:
            			this.isRegisterNutrionist = true;
            			console.log("case 2");
            		break;
            		default:
            			this.isRegisterNutrionist = false;
            		break;
            	}
            },
            getEspecialidades: function () {
            	const path = this.api+`specialties/`;
                axios.get(path).then((response) => {
                  this.specialties = response.data
                  // console.log(this.specialties)
                })
                .catch((error) => {
                  console.log(error)
                })
            }
        }
    }
</script>