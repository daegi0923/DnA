<template>
    <img src="@/assets/login.png" alt="background" class="background-image">
    <div>
      <v-sheet class="mx-auto" max-width="500">

        <v-form @submit.prevent="signUp" class="login-form" >
          <v-text-field label="username" v-model.trim="username"></v-text-field>
          <v-text-field type="password" label="password1" v-model.trim="password1"></v-text-field>
          <v-text-field type="password" label="password2" v-model.trim="password2"></v-text-field>
          <v-btn type="submit">회원가입</v-btn>
        </v-form>
      </v-sheet>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const username = ref(null) 
const password1 = ref(null)
const password2 = ref(null)
const store = useCounterStore()

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
}

</script>

<style>
.background-container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5); /* 배경을 반투명 검정색으로 설정 */
}
.login-form {
  width: 400px;
  background: rgba(255, 255, 255, 0.8); /* 폼 배경을 반투명 흰색으로 설정 */
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* 약간의 그림자 효과 */
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

</style>
