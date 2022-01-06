<template>
  <div>
     <div id="main-wrapper">
      <!-- ============================================================== -->
      <!-- Topbar header - style you can find in pages.scss -->
      <!-- ============================================================== -->
      <HeaderComponent/>
      <!-- ============================================================== -->
      <!-- End Topbar header -->
      <!-- ============================================================== -->
      <!-- ============================================================== -->
      <!-- Left Sidebar - style you can find in sidebar.scss  -->
      <!-- ============================================================== -->
      <LeftSidebarComponent/>
      <!-- ============================================================== -->
      <!-- End Left Sidebar - style you can find in sidebar.scss  -->
      <!-- ============================================================== -->
      <!-- ============================================================== -->
      <!-- Page wrapper  -->
      <!-- ============================================================== -->
      <div class="page-wrapper">
        <!-- ============================================================== -->
        <!-- Bread crumb and right sidebar toggle -->
        <router-view/>
        <!-- ============================================================== -->
        <!-- footer -->
        <!-- ============================================================== -->
        <FooterComponent/>
        <!-- ============================================================== -->
        <!-- End footer -->
        <!-- ============================================================== -->
      </div>
      <!-- ============================================================== -->
      <!-- End Page wrapper  -->
      <!-- ============================================================== -->
    </div>
    <RightSidebarComponent/>
  </div>
</template>


<script>

import HeaderComponent from '@/components/layout/home/header.vue';
import FooterComponent from '@/components/layout/home/footer.vue';
import LeftSidebarComponent from '@/components/layout/home/leftsidebar.vue';
import RightSidebarComponent from '@/components/layout/home/rightsidebar.vue';

export default {
  name: "Dashboard",
  components: {
    HeaderComponent,
    FooterComponent,
    LeftSidebarComponent,
    RightSidebarComponent    
  }
};
</script>