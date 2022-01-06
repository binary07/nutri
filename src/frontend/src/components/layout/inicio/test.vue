<template>
	<div class="container">
		<div style="margin-top:15%;">
            <br>
            <div v-if="tipo == 'lista' && !results">
            	<h2 style="text-align: center;" v-if="tipo != 'lista'">Test <small v-text="tipo.toUpperCase()"></small></h2>
		    	<h2 style="text-align: center;" v-if="tipo == 'lista'">Selecciona un test de tu interés</h2>
            	

		    	<table v-if="tipo == 'lista'" class="table">
		    		<tbody>
		    			<tr>
		    				<td style="width:10%;">
		    					<img style="border: 0px solid red; border-radius: 1rem;margin-rigth: 2%;" width="50" height="50" src="/static/assets/images/imc.png" alt="imc-imagen">
		    				</td>
		    				<td style="width:90%;">IMC (Indice de masa corporal) <br> <small class="realizar" @click="setTipo('imc')">Realizar test</small></td>
		    			</tr>
		    			<tr>
		    				<td style="width:10%;">
		    					<img style="border: 0px solid red; border-radius: 1rem;margin-rigth: 2%;" width="50" height="50" src="/static/assets/images/grasa.jpeg" alt="imc-imagen">
		    				</td>
		    				<td style="width:90%;">% Porcentaje de grasa <br> <small class="realizar" @click="setTipo('grasa')">Realizar test</small> </td>
		    			</tr>
		    			<tr>
		    				<td style="width:10%;">
		    					<img style="border: 0px solid red; border-radius: 1rem;margin-rigth: 2%;" width="50" height="50" src="/static/assets/images/musculo.png" alt="imc-imagen">
		    				</td>
		    				<td style="width:90%;">% Porcentaje de musculo <br> <small class="realizar" @click="setTipo('musculo')">Realizar test</small></td>
		    			</tr>
		    		</tbody>
		    	</table>
		    	<a class="btn btn-info" :href="'/nutriologos/'+this.$route.params.id" style="text-align: center;">Siguiente</a>
            </div>

            <div v-if="tipo != 'lista' && !results" class="php-email-form">
            <h2 style="text-align: center;">Test <small v-text="tipo.toUpperCase()"></small></h2>
	          <div class="form-row">
	            <div class="col-md-6 form-group" v-if="tipo == 'imc'">
	               <input type="text" v-model="height" class="form-control" id="estatura" placeholder="estatura">
	            </div>
	            <div class="col-md-6 form-group" v-if="tipo == 'imc'">
	              <input type="text" v-model="weight" class="form-control" id="peso" placeholder="peso">
	            </div>
	            <div class="col-md-6 form-group" v-if="tipo == 'musculo' || tipo == 'grasa'">
	              <input type="date" v-model="birthday" class="form-control" id="1" placeholder="cumpleaños">
	            </div>
	            <div class="col-md-6 form-group" v-if="tipo == 'musculo' || tipo == 'grasa'">
	              <input type="number"v-model="porcentaje"  class="form-control" id="1" placeholder="%">
	            </div>
	            <div class="col-md-6 form-group">
	              <select name="gender" class="form-control" v-model="gender">
                  	<option value="">Sexo</option>
                    <option value="Femenino">
                      Femenino
                    </option>
                    <option value="Masculino">
                      Masculino
                    </option>
                    <option value="otro">
                      Otro
                    </option>
                  </select>
	            </div>
	          </div>

	          <div class="text-center">
	          	<a style="text-align: center;padding:10px;" class="btn btn-success" href="#" @click="makeTest()">Calcular</a> 
                <a style="text-align: center;padding:10px;" class="btn btn-info" href="/nutriologos">Siguiente</a>
	          </div>
	        </div>


         
		    <div v-if="results">
		    	<h2 style="text-align: center;color: green;"><b>Resultados</b> <small v-text="tipo.toUpperCase()"></small></h2>
		    	<p style="margin: 10px;" align="center">Para la información que ingresó</p>
		    	<p style="margin: 10px;">
		    		<div style="margin: 10px;" v-if="resultsType != ''"><b>Paciente: </b><small v-text="patient.first_name+ ' '+patient.last_name+' '+patient.second_lastname"></small></div>
		    		<div style="margin: 10px;" v-if="resultsType == 'imc'"><b>Estatura: </b><small v-text="patient.height+' M'"></small><br></div>
		    		<div style="margin: 10px;" v-if="resultsType == 'imc'"><b>Peso: </b><small v-text="patient.weight+' KG'"></small><br></div>
		    		<div style="margin: 10px;" v-if="resultsType == 'musculo' || resultsType == 'grasa'"><b>Sexo: </b><small v-text="gender"></small><br></div>
		    		<div style="margin: 10px;" v-if="resultsType == 'musculo' || resultsType == 'grasa'"><b>Edad: </b><small v-text="birthday"></small><br></div>
		    		<div style="margin: 10px;" v-if="resultsType == 'musculo' || resultsType == 'grasa'"><b>Porcentaje: </b><small v-text="porcentaje"></small><br></div>
		    	</p>
		    	<p v-if="resultsType == 'imc'" style="margin: 10px;" align="justify">Su IMC es <b v-text="patient.body_mass"></b> lo que indica que su peso es
		    	 <b v-if="patient.estatus_imc == 'inferior al normal'" style="color: red;" v-text="patient.estatus_imc"></b>
		    	 <b v-if="patient.estatus_imc == 'normal'" style="color: green;" v-text="patient.estatus_imc"></b>
		    	 <b v-if="patient.estatus_imc == 'superior al normal'" style="color: orange;" v-text="patient.estatus_imc"></b>
		    	 <b v-if="patient.estatus_imc == 'obesidad'" style="color: red;" v-text="patient.estatus_imc"></b>
		    	</p>
		    	<p v-if="resultsType == 'imc'" style="margin: 10px;"> Mantener un peso saludable puede reducir el riesgo de enfermededa crónicas asociadas al sobrepeso y la obesidad. </p>
		    	<p v-if="resultsType == 'imc'" style="margin: 10px;" align="justify"> Para información sobre importancia de una alimentación saludable y actividad física para mantener un peso saludable, <b>continua</b> y encuentra a nutriólogos expertos que pueden ayudarte.</p>
		    	<div v-if="resultsType == 'musculo'" style="text-align: center;"> <span style="text-align: center;font-size: 20px;">Su porcentaje de <small style="color: blue;">MÚSCULO</small> es:</span> <br>
		    		<b v-if="patient.estatus_musculo ==  'Bajo'" style="font-size: 30px;text-align: center;color: red;" v-text="patient.estatus_musculo"></b>
		    		<b v-if="patient.estatus_musculo ==  'Normal'" style="font-size: 30px;text-align: center; color: green;" v-text="patient.estatus_musculo"></b>
		    		<b v-if="patient.estatus_musculo ==  'Alto'" style="font-size: 30px;text-align: center; color: orange;" v-text="patient.estatus_musculo"></b>
		    		<b v-if="patient.estatus_musculo ==  'Muy alto'" style="font-size: 30px;text-align: center; color: red;" v-text="patient.estatus_musculo"></b>
		    	</div>
		    	<div v-if="resultsType == 'grasa'" style="text-align: center;"> <span style="text-align: center;font-size: 20px;">Su porcentaje de <small style="color: blue;">GRASA</small> es:</span> <br>
		    		<b v-if="patient.estatus_grasa ==  'Bajo'" style="font-size: 30px;text-align: center;color: red;" v-text="patient.estatus_grasa"></b>
		    		<b v-if="patient.estatus_grasa ==  'Normal'" style="font-size: 30px;text-align: center;color: green;" v-text="patient.estatus_grasa"></b>
		    		<b v-if="patient.estatus_grasa ==  'Alto'" style="font-size: 30px;text-align: center;color: orange;" v-text="patient.estatus_grasa"></b>
		    		<b v-if="patient.estatus_grasa ==  'Muy alto'" style="font-size: 30px;text-align: center; color: red;" v-text="patient.estatus_grasa"></b>
		    	</div>
		    </div>
        </div>
        <div style="text-align: center; margin-top: 15px;" v-if="tipo != 'lista'">
        	<!-- faltariaprogramar que dependiendo el perfil vena su home... eso seria con un children en routes -->
        	<!-- <a class="btn btn-info" href="/nutriologos" style="display: inline;">siguiente</a -->
        	<a class="realizar" href="#" @click="tipo = 'lista'; results = false;">realizar otro test</a>
        </div>
	</div>
</template>

<style scoped>
	h2{
		color: green;
	}
	p,small,b{
		font-size: 17px;
	}
	.realizar{
		cursor: pointer;
		text-decoration: underline;
		color: blue;
		display: inline;
		margin-top: 0px;
		margin: 20px;
	}

	ul{
		margin-left: -15%;
	}

	li a{
		list-style: none;
		display: inline-block;
		border: 10px solid;
		align-content: center;
		border-radius: 50%; 
		width: 55px;
		height: 55px;
		
	}
	.a-grasa{
		border-color: orange;
		border-radius: 5rem; 
	}

	.a-masa{
		border-color: green;
		border-radius: 5rem; 
	}
	.a-imc{
		border-color: #2E86C1;
		border-radius: 5rem; 
	}



</style>

<script>
	import axios from 'axios'
    import swal from 'sweetalert'

	export default {
		name: "tests",
		data () {
        	return {
		        tipo: 'lista',  //lista, imc, grasa, musculo (los tres tipos xD)
		        persona_id: this.$route.params.id,
		        results: false,
		        resultsType: false,
		        gender: '',
				weight: '',
				height: '',
				birthday:'',
				porcentaje:'',
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
				api: 'https://back.pruebasreset.website/api/v1.0/',
				// api: 'http://localhost:8000/api/v1.0/',
		    }
	    },
	    created(){
	    	// code
	    },
		methods:{
			setTipo: function (op) {
				switch(op){
					case 'imc':
						this.tipo = op;	
						this.getPatient();
					break;
					case 'grasa':
						this.tipo = op;	
						this.getPatient();
					break;
					case 'musculo':
						this.tipo = op;	
						this.getPatient();
					break;
					default:
						this.tipo = op;
					break;
				}			
			},
			calcularEstado: function (ps,p) {
				if( p < ps[0] ){
					return 'Bajo';
				}
				else if( p >= ps[1] && p <= ps[2] ){
					return 'Normal';
				}
				else if( p >= ps[3] && p <= ps[4] ){
					return 'Alto';
				}
				else if( p >= ps[5] ){
					return 'Muy alto';
				}
				else{
					return 'sin estatus-mus';
				}
			},
			makeTest:function() {
				switch(this.tipo){
					case 'imc':
						var form = {gender: this.gender, weight: this.weight, height: this.height};
						console.log("send datos test imc ...", form);
						// save data
						axios.put(this.api+`patients/${this.persona_id}/`, form).then(res => {
						  this.results = true;
						  this.resultsType = this.tipo;
						  console.log("result add imc",res.data);
						  // calculate imc
						  this.getPatient();
				        }).catch(err => {
				          console.log(err);
				        });
					break;
					case 'grasa':
						var estatus = 'sin estatus-0';
						var edades = [18,40,60,81];
						var hoy = new Date();
						var edad = hoy.getFullYear() - parseInt(this.birthday.split('-')[0]);
						var porcentaje = this.porcentaje; // porcentaje de grasa
						
						switch(this.patient.gender.toLowerCase()){
							case 'femenino':
								switch(edad){
									case 6:
										estatus = this.calcularEstado([13.8, 13.8,24.9, 25.0,27.0, 27.1], porcentaje);
									break;
									case 7:
										estatus = this.calcularEstado([14.4, 14.4,27.0, 27.1,29.6, 29.7], porcentaje);
									break;
									case 8:
										estatus = this.calcularEstado([15.1, 15.1,29.1, 29.2,31.9, 32.0], porcentaje);
									break;
									case 9:
										estatus = this.calcularEstado([15.8, 15.8,30.8, 30.9,33.8, 33.9], porcentaje);
									break;
									case 10:
										estatus = this.calcularEstado([16.1, 16.1,32.2, 32.3,35.2, 35.3], porcentaje);
									break;
									case 11:
										estatus = this.calcularEstado([16.3, 16.3,33.1, 33.2,36.0, 36.1], porcentaje);
									break;
									case 12:
										estatus = this.calcularEstado([16.4, 16.4,33.5, 33.6,36.3, 36.4], porcentaje);
									break;
									case 13:
										estatus = this.calcularEstado([16.4, 16.4,33.8, 33.9,36.5, 36.6], porcentaje);
									break;
									case 14:
										estatus = this.calcularEstado([16.3, 16.3,34.0, 34.1,36.7, 36.8], porcentaje);
									break;
									case 15:
										estatus = this.calcularEstado([16.1, 16.1,34.2, 34.3,36.9, 37.0], porcentaje);
									break;
									case 16:
										estatus = this.calcularEstado([15.8, 15.8,34.5, 34.6,37.1, 37.2], porcentaje);
									break;
									case 17:
										estatus = this.calcularEstado([15.4, 15.4,34.7, 34.8,37.3, 37.4], porcentaje);
									break;
									default:
										if( edad >= edades[0] && edad < edades[1] ){
											estatus = this.calcularEstado([21.0, 21.0,32.9,33.0,38.9, 39.0], porcentaje);
										}
										else if( edad >= edades[1] && edad < edades[2] ){
											estatus = this.calcularEstado([23.0, 23.0,33.9,34.0,39.9, 40.0], porcentaje);
										}
										else if( edad >= edades[2] && edad < edades[3] ){
											estatus = this.calcularEstado([24.0, 24.0,35.9,36.0,41.9, 42.0], porcentaje);
										}
										else{
											estatus = 'sin estatus-f';
										}
									break;
								}
							break;
							case 'masculino':
								switch(edad){
									case 6:
										estatus = this.calcularEstado([11.8, 11.8,21.7, 21.8,23.7, 23.8], porcentaje);
									break;
									case 7:
										estatus = this.calcularEstado([12.1, 12.1,23.2, 23.3,25.5, 25.6], porcentaje);
									break;
									case 8:
										estatus = this.calcularEstado([12.4, 12.4,24.8, 24.9,27.7, 27.8], porcentaje);
									break;
									case 9:
										estatus = this.calcularEstado([12.6, 12.6,26.5, 26.6,30.0, 30.1], porcentaje);
									break;
									case 10:
										estatus = this.calcularEstado([12.8, 12.8,27.9, 28.0,31.8, 31.9], porcentaje);
									break;
									case 11:
										estatus = this.calcularEstado([12.6, 12.6,28.5, 28.6,32.6, 32.7], porcentaje);
									break;
									case 12:
										estatus = this.calcularEstado([12.3, 12.3,28.2, 28.3,32.4, 32.5], porcentaje);
									break;
									case 13:
										estatus = this.calcularEstado([11.6, 11.6,27.5, 27.6,31.3, 31.4], porcentaje);
									break;
									case 14:
										estatus = this.calcularEstado([11.1, 11.1,26.4, 26.5,30.0, 30.1], porcentaje);
									break;
									case 15:
										estatus = this.calcularEstado([10.8, 10.8,25.4, 25.5,28.7, 28.8], porcentaje);
									break;
									case 16:
										estatus = this.calcularEstado([10.4, 10.4,24.7, 24.8,27.7, 27.8], porcentaje);
									break;
									case 17:
										estatus = this.calcularEstado([10.1, 10.1,24.2, 24.3,26.8, 26.9], porcentaje);
									break;
									default:
										if( edad >= edades[0] && edad < edades[1] ){
											estatus = this.calcularEstado([8.0, 8.0,19.9, 20.0,24.9, 25.0], porcentaje);
										}
										else if( edad >= edades[1] && edad < edades[2] ){
											estatus = this.calcularEstado([11.0, 11.0,21.9, 22.0,27.9, 28.0], porcentaje);
										}
										else if( edad >= edades[2] && edad < edades[3] ){
											estatus = this.calcularEstado([13.0, 13.0,24.9, 25.0,29.9, 30.0], porcentaje);
										}
										else{
											estatus = 'sin estatus-f';
										}
									break;
								}
							break;
							default:
								estatus = 'sin estatus';
							break;
						}

						this.patient.estatus_grasa = estatus;
						this.results = true;
						this.resultsType = this.tipo;
						var age = new Date(this.birthday);
						this.birthday = edad + ' años';
						
						var form = {gender: this.gender, age: age.getTime()};
						console.log("send datos test grasa ...", form, this.patient.estatus_grasa);
						// save data
						axios.put(this.api+`patients/${this.persona_id}/`, form).then(res => {
						  console.log("guardar la edad y sexo del paciente", res.data);
				        }).catch(err => {
				          console.log(err);
				        });
					break;
					case 'musculo':
						var estatus = 'sin estatus';
						var edades = [18,40,60,81];
						var hoy = new Date();
						var edad = hoy.getFullYear() - parseInt(this.birthday.split('-')[0]);
						var porcentaje = this.porcentaje; // porcentaje de músculo
						
						switch(this.patient.gender.toLowerCase()){
							case 'femenino':
								if( edad >= edades[0] && edad < edades[1] ){
									estatus = this.calcularEstado([24.3,24.4,30.3,30.4,35.3,35.4], porcentaje);
								}
								else if( edad >= edades[1] && edad < edades[2] ){
									estatus = this.calcularEstado([24.1,24.1,30.1,30.2,35.1,35.2], porcentaje);
								}
								else if( edad >= edades[2] && edad < edades[3] ){
									estatus = this.calcularEstado([23.9,23.9,29.9,30.0,34.9,35.0], porcentaje);
								}
								else{
									estatus = 'sin estatus-f';
								}
							break;
							case 'masculino':
								if(edad >= edades[0] && edad < edades[1] ){
									estatus = this.calcularEstado([33.3,33.3,39.3,39.4,44.0,44.1], porcentaje);
								}else if(edad >= edades[1] && edad < edades[2] ){
									estatus = this.calcularEstado([33.1,33.1,39.1,39.2,43.8,43.9], porcentaje);
								}else if( edad >= edades[2] && edad < edades[3] ){
									estatus = this.calcularEstado([32.9,32.9,38.9,39.0,43.6,43.7], porcentaje);
								}else{
									estatus = 'sin estatus-m';
								}
							break;
							default:
								estatus = 'sin estatus';
							break;
						}

						this.patient.estatus_musculo = estatus;
						this.results = true;
						this.resultsType = this.tipo;
						var age = new Date(this.birthday);
						this.birthday = edad + ' años';
						
						var form = {gender: this.gender, age: age.getTime()};
						console.log("send datos test musculo ...", form);
						// save data
						axios.put(this.api+`patients/${this.persona_id}/`, form).then(res => {
						  console.log("guardar la edad y sexo del paciente", res.data);
				        }).catch(err => {
				          console.log(err);
				        });
					break;
				}
			},
			getPatient: function () {
		        axios.get(this.api+`patients/${this.persona_id}/`).then(res => {
		          this.gender = res.data.gender;
		          this.weight = res.data.weight;
		          this.height = res.data.height;
		          this.patient = res.data;
		          if (res.data.age != null) {
		          	this.patient.age = this.formatDate(new Date(res.data.age));
		          	this.birthday = this.patient.age;
		          }
		          // OMS
		          if (this.patient.body_mass < 18.5) {
		          	this.patient.estatus_imc = 'inferior al normal';
		          }else if(this.patient.body_mass >= 18.5 && this.patient.body_mass < 25){
		          	this.patient.estatus_imc = 'normal';
		          }else if(this.patient.body_mass >= 25 && this.patient.body_mass < 30){
		          	this.patient.estatus_imc = 'superior al normal';
		          }else if(this.patient.body_mass >= 30){
		          	this.patient.estatus_imc = 'obesidad';
		          }
		          console.log("result api patient",res.data);
		        }).catch(err => {
		          console.log(err);
		        });
			},
			formatDate: function (date) {
			    var d = new Date(date),
			        month = '' + (d.getMonth() + 1),
			        day = '' + d.getDate(),
			        year = d.getFullYear();

			    if (month.length < 2) 
			        month = '0' + month;
			    if (day.length < 2) 
			        day = '0' + day;

			    return [year, month, day].join('-');
			}
		}
	}
</script>