<template>
  <img src="@/assets/login.png" alt="background">
  <v-sheet width="400" class="signupform">
    <v-form @submit.prevent="signUp">
      <v-text-field variant="solo-inverted" clearable label="아이디" v-model.trim="username"></v-text-field>
      <v-text-field type="password" label="비밀번호" variant="solo-inverted" v-model.trim="password1"></v-text-field>
      <v-text-field type="password" label="비밀번호 확인" variant="solo-inverted" v-model.trim="password2"></v-text-field>
      <v-btn type="submit" block>회원가입</v-btn>
    </v-form>
  </v-sheet>
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

<style scoped>
* {
  box-sizing: border-box;
}
.signupform {
  padding: 10px;
  border: 2px solid #112D4E;
  border-radius: 5px;
}

img {
  width: 500px;
  margin-bottom: 10px;
}
</style>
