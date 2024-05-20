<template>
    <div class="background-container">
        <div class="login-container">
            <Login/>
        </div>

    </div>
</template>

<script setup>
import Login from '@/components/Login.vue'
</script>

<style scoped>
*{
    box-sizing: border-box;
}

.login-container {
  display: flex;
  justify-content: center; /* 수평 중앙 정렬 */
  align-items: center; /* 수직 중앙 정렬 */
  background-color: #f8f9fa; /* 배경색 (필요에 따라 변경 가능) */
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