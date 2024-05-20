<template>
<div class="background-container">
  <Login/>    
</div>
</template>

<script setup>
import Login from '@/components/Login.vue'
</script>

<style scoped>
*{
    box-sizing: border-box;
}

.background-container {
  background-image: url('@/assets/startpagebackground.jpg');
  background-size: cover; /* 배경 이미지를 전체 영역에 맞춤 */
  background-position: center; /* 배경 이미지를 중앙에 위치 */
  width: 100vw; /* 화면 전체 너비 */
  height: 100vh; /* 화면 전체 높이 */
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

</style>