<template>
  <div class="background-container">
    <img src="@/assets/Logo.png" class="img" alt="startpage">
    <div class="router-container">
        <RouterLink :to="{name: 'login'}" class="link-button">로그인</RouterLink>
        <RouterLink :to="{name: 'signup'}" class="link-button">회원가입</RouterLink>
    </div>
  </div>
</template>

<script setup>

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
.img{
    width: 500px
}
.router-container {
    margin: 30px
}
.link-button {
  display: inline-block;
  text-align: center; /* 텍스트를 가운데 정렬 */
  margin: 0px 20px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  border: 1px solid #ec9d5c;
  border-radius: 10px;
  background-color: #ec9d5c;
  color: white;
  width: 130px;
  text-decoration: none;
}
</style>