<template>
  <div class="carousel-container">
    <v-carousel class="carousel">
      <v-carousel-item src="1.jpg" cover></v-carousel-item>
      <v-carousel-item src="2.jpg" cover></v-carousel-item>
      <v-carousel-item src="3.jpg" cover></v-carousel-item>
    </v-carousel>
  </div>
</template>

<script setup>
</script>

<style scoped>
.carousel-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%; /* 전체 화면 높이로 설정 */
}

.carousel {
}
</style>