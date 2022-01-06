import Vue from 'vue'
import Router from 'vue-router'


// import PatientList from '@/components/patients/PatientList'
// import CreatePatient from '@/components/patients/CreatePatient'
import Patient from '@/components/patients/Patient'
// import EditPatient from '@/components/patients/EditPatient'
// import DeletePatient from '@/components/patients/DeletePatient'
import IMCTest from '@/components/patients/IMCTest'
import FatTest from '@/components/patients/FatTest'
import MuscleTest from '@/components/patients/MuscleTest'

// import NutritionistList from '@/components/nutritionists/NutritionistList'
// import CreateNutritionist from '@/components/nutritionists/CreateNutritionist'
// import EditNutritionist from '@/components/nutritionists/EditNutritionist'
// import DeleteNutritionist from '@/components/nutritionists/DeleteNutritionist'


Vue.use(Router)

const router =  new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: () => import("@/components/layout/inicio/index.vue"),
      meta: {
        isPublic: true
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import("@/components/layout/inicio/sigin.vue"),
      meta: {
        isPublic: true
      }
    },
    {
      path: '/register',
      name: 'Register',
      component: () => import("@/components/layout/inicio/register.vue"),
      meta: {
        isPublic: true
      }
    },
    {
      path: '/test/:id',
      name: 'Test',
      component: () => import("@/components/layout/inicio/test.vue"),
      meta: {
        isPublic: true
      }
    },
    // {
    //   path: '/home',
    //   name: 'Home',
    //   component: Home,
    //   meta: {
    //     isPublic: false
    //   }
    // },
    {
      path: '/pacientes/',
      name: 'PatientList',
      component: () => import("@/components/patients/PatientList"),
      meta: {
        isPublic: false
      }
    },
    {
      path: '/pacientes/nuevo/',
      name: 'CreatePatient',
      component: () => import("@/components/patients/CreatePatient"),
      meta: {
        isPublic: false
      }
    },
    {
      path: '/pacientes/:patientId/',
      name: 'Patient',
      component: Patient
    },
    {
      path: '/pacientes/:patientId/editar/',
      name: 'EditPatient',
      component: () => import("@/components/patients/EditPatient"),
      meta: {
        isPublic: false
      }
    },
    {
      path: '/pacientes/:patientId/historial/nuevo/',
      name: 'CreateMedicalRecord',
      component: () => import("@/components/patients/CreateMedicalRecord"),
      meta: {
        isPublic: false
      }
    },
    {
      path: '/pacientes/:patientId/seguimiento/nuevo/',
      name: 'CreateMedicalTracing',
      component: () => import("@/components/patients/CreateMedicalTracing"),
      meta: {
        isPublic: false
      }
    },
    {
      path: '/historiales/:recordId/',
      name: 'Record',
      component: () => import("@/components/patients/Record"),
      meta: {
        isPublic: false
      }
    },
    {
      path: '/pacientes/:patientId/eliminar/',
      name: 'DeletePatient',
      component: () => import("@/components/patients/DeletePatient"),
      meta: {
        isPublic: false
      }
    },
    {
      path: '/pacientes/:patientId/imc/',
      name: 'IMCTest',
      component: IMCTest
    },
    {
      path: '/pacientes/:patientId/grasa/',
      name: 'FatTest',
      component: FatTest
    },
    {
      path: '/pacientes/:patientId/musculo/',
      name: 'MuscleTest',
      component: MuscleTest
    },
    {
      path: '/contactos/:id', //patient_id
      name: 'NutritionistList',
      component: () => import("@/components/nutritionists/NutritionistList"),
      meta: {
        isPublic: false
      }
    },
    {
      path: '/nutriologos/:id', //patient_id
      name: 'NutritionistList',
      component: () => import("@/components/nutritionists/NutritionistList"),
      meta: {
        isPublic: false
      }
    },
    {
      path: '/nutriologos/nuevo/',
      name: 'CreateNutritionist',
      component: () => import("@/components/nutritionists/CreateNutritionist"),
      meta: {
        isPublic: false
      }
    },
    {
      path: '/nutriologos/:nutritionistId/editar/',
      name: 'EditNutritionist',
      component: () => import("@/components/nutritionists/EditNutritionist"),
      meta: {
        isPublic: false
      }
    },
    {
      path: '/nutriologos/:nutritionistId/eliminar/',
      name: 'DeleteNutritionist',
      component: () => import("@/components/nutritionists/DeleteNutritionist"),
      meta: {
        isPublic: false
      }
    },
  ],
  mode: 'history',
})

// aqui agregamos la lógica para verificación de token
function existToken() {
  // por ejemplo lo devueldo en true (estoy autenticado)
  return true;
}

// creo un interceptor para autenticación y 
router.beforeEach((to, from, next) => {
    if (to.path != '/login' && existToken()) {
      // console.log("se envia a la ruta solicitada");
      next();
    } else {
      // console.log("se envia al login papu");
      next();
    }
});

export default router