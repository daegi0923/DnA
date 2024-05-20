<template>
<img src="@/assets/login.png" alt="background">
<v-sheet width="400" class="loginform">
  <v-form @submit.prevent="logIn">
    <v-text-field clearable label="username" variant="solo-inverted" v-model.trim="username"></v-text-field>
    <v-text-field type="password" clearable label="password" variant="solo-inverted" v-model.trim="password"></v-text-field>
    <v-btn class="mt-2" type="submit" block>로그인</v-btn>
  </v-form>
</v-sheet>
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
*{
  box-sizing: border-box;
}
.loginform{
  padding: 10px;
  border-radius: 5px;
  border: 2px solid #ec9d5c
}
img{
  width: 500px;
  margin-bottom: 0;
}
</style>
