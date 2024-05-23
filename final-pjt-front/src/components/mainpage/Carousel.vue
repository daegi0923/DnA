<template>
  <div id="carouselExample" class="carousel-container carousel slide" data-bs-ride="carousel" data-bs-interval="3000">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="/carousel/001.png" class=" d-block w-100" alt="...">
      </div>
      <div class="carousel-item">
        <img src="/carousel/002.png" class="d-block w-100" alt="...">
      </div>
      <div class="carousel-item">
        <img src="/carousel/003.png" class="d-block w-100" alt="...">
      </div>
      <div class="carousel-item">
        <img src="/carousel/004.png" class="d-block w-100" alt="...">
      </div>
      <!-- 추가 이미지들을 여기에 넣을 수 있습니다 -->
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
.carousel-container {
  box-shadow: 0 2px 8px #DBE2EF;
  border-radius: 5px;
  display: flex;
  justify-content: center;
  align-items: center;
  /* height: 957px; Viewport height to center vertically */
  background-color: #f8f9fa; /* Optional: background color */
}

.carousel {
  width: 100%; /* Adjust width as needed */
}
</style>
