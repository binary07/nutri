<template>
	<div class="container">
		<div>
        <!-- <div class="row"> --><br><br>
            <h2 style="text-align: center;">Iniciar Sesión</h2><br>
            <div class="auth-box" style="padding: 10px;">
                <div id="loginform" style="background: white; padding: 10%;">
                    <div class="logo" style="text-align: center;">
                        <!-- <span class="db" style="text-align:center;"><img src="static/assets/images/logos/logo-icon.png" alt="logo" /></span> -->
                        <!-- <h5 class="font-medium mb-3">Iniciar Sesión</h5> -->
                        <div class="row">
                            <div class="col-xs-12 col-sm-12 col-md-12 mt-2 text-center">
                                <div class="social">
                                    <a href="javascript:void(0)" class="btn  btn-facebook" data-toggle="tooltip" title="" data-original-title="Login with Facebook"> <i aria-hidden="true" class="fab  fa-facebook"></i> </a>
                                    <a href="javascript:void(0)" class="btn btn-googleplus" data-toggle="tooltip" title="" data-original-title="Login with Google"> <i aria-hidden="true" class="fab  fa-google-plus"></i> </a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- Form -->
                    <div class="row">
                        <div class="col-12">
                            <form class="form-horizontal mt-3" id="loginform" action="index.html">
                                <div class="input-group mb-3">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text" id="basic-addon1"><i class="ti-user"></i></span>
                                    </div>
                                    <input type="text" class="form-control form-control-lg" placeholder="Teléfono" aria-label="Teléfono" id="telefono" aria-describedby="basic-addon1" maxlength="10">
                                </div>
                                <div class="input-group mb-3">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text" id="basic-addon2"><i class="ti-pencil"></i></span>
                                    </div>
                                    <input type="password" class="form-control form-control-lg" placeholder="Contraseña" aria-label="Contraseña" id="password" aria-describedby="basic-addon1">
                                </div>
                                <div class="form-group row">
                                    <div class="col-md-12">
                                        <div class="custom-control custom-checkbox">
                                            <input type="checkbox" class="custom-control-input" id="customCheck1">
                                            <label class="custom-control-label" for="customCheck1">Recuerdame</label>
                                            <a href="/recovery" id="to-recover" class="text-dark float-right"><i class="fa fa-lock mr-1"></i> olvidaste tu pwd?</a>
                                        </div>
                                    </div>
                                </div>
                                <div class="form-group text-center">
                                    <div class="col-xs-12 pb-3">
                                        <a href="#" class="btn btn-block btn-lg btn-info" @click="login()">Inciar sesión</a>
                                    </div>
                                </div>
                                <!-- social -->
                                <div class="form-group mb-0 mt-2">
                                    <div class="col-sm-12 text-center">
                                        No tienes una cuenta? <a href="/register" class="text-info ml-1"><b>Registrate</b></a>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
                <!-- <div id="recoverform">
                    <div class="logo">
                        <span class="db"><img src="static/assets/images/logos/logo-icon.png" alt="logo" /></span>
                        <h5 class="font-medium mb-3">Recover Password</h5>
                        <span>Enter your Email and instructions will be sent to you!</span>
                    </div>
                    <div class="row mt-3">
                     
                        <form class="col-12" action="index.html">
                        
                            <div class="form-group row">
                                <div class="col-12">
                                    <input class="form-control form-control-lg" type="email" required="" placeholder="Username">
                                </div>
                            </div>
                       
                            <div class="row mt-3">
                                <div class="col-12">
                                    <button class="btn btn-block btn-lg btn-danger" type="submit" name="action">Reset</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div> -->
            </div>
        </div>
	</div>
</template>

<style lang="css" scoped>  
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
</style>


<script>
    export default {
        name: 'login',
        methods:{
            login: function () {

                var data = {telefono: $("#telefono").val(),password: $("#password").val()};
                console.log("form login", data);

                // axios.post("/post/login",data).then(err=>{
                //     if (res.data.success) {
                //         swal(success);
                //     }else{
                //         swal(error);
                //     }
                // });
            }
        }
    }
</script>