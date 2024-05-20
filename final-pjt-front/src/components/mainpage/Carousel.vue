<template>
<div id="carouselExample" class="carousel slide">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="@/assets/1.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="@/assets/2.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="@/assets/3.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="@/assets/4.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="@/assets/5.jpg" class="d-block w-100" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
  </template>
  
  <script setup>
  </script>
  
<style scoped>
img {
  height: 500px; /* Set the height as per your requirement */
  object-fit: cover; /* Ensure the image covers the entire container */
}
</style>
  