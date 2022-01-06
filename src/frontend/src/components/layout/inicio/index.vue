<template>
	<div>
		<section id="hero" class="d-flex align-items-center">
			<div class="container">
				<h1>Bienvenido a Nutrición</h1>
			    <h2>Somos un equipo con una gran número de nutriólogos para ayudarte con tu nutrición</h2>
			    <a href="/register" class="btn-get-started scrollto">Empezar</a>
			</div>
		</section>	
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