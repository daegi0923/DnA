<template>
  <div class="background-container">
    <img src="@/assets/login.png" alt="background" class="background-image">
    <div class="login-container">
      <v-form @submit.prevent="logIn" class="login-form">
        <v-text-field clearable label="username" variant="solo-inverted" v-model.trim="username"></v-text-field>
        <v-text-field type="password" clearable label="password" variant="solo-inverted" v-model.trim="password"></v-text-field>
        <v-btn class="mt-2" type="submit" block>로그인</v-btn>
      </v-form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';

const username = ref(null);
const password = ref(null);
const store = useCounterStore();

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  };
  store.logIn(payload);
};
</script>

<style scoped>
.background-container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5); /* 배경을 반투명 검정색으로 설정 */
}

.background-image {
  position: absolute;
  top: 40%; /* 배경 이미지의 위치를 살짝 위로 조정 */
  left: 50%;
  transform: translate(-50%, -50%);
  max-width: 100%;
  max-height: 100%;
  z-index: 1;
  width: 650px;
  opacity: 0.8; /* 이미지 반투명 설정 (필요시 조정) */
}

.login-container {
  position: relative;
  z-index: 0; /* 이미지 위에 표시되도록 설정 */
  top: 20px; /* 로그인 폼을 살짝 아래로 조정 */
}

.login-form {
  width: 400px;
  background: rgba(255, 255, 255, 0.8); /* 폼 배경을 반투명 흰색으로 설정 */
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* 약간의 그림자 효과 */
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}
</style>
