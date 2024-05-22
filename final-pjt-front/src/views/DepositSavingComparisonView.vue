<template>
	<v-container class="container">
	  <v-row justify="center" class="mb-4">
		<v-col cols="auto">
		  <RouterLink :to="{ name: 'deposit' }">
			<v-btn
			  color="#DBE2EF"
			  class="mx-2"
			  :class="{ 'button-large': isDepositActive }"
			  @click="toggleButton('deposit')"
			>
			  예금
			</v-btn>
		  </RouterLink>
		</v-col>
		<v-col cols="auto">
		  <RouterLink :to="{ name: 'saving' }">
			<v-btn
			  color="#DBE2EF"
			  class="mx-2"
			  :class="{ 'button-large': isSavingActive }"
			  @click="toggleButton('saving')"
			>
			  적금
			</v-btn>
		  </RouterLink>
		</v-col>
	  </v-row>
	  <RouterView/>
	</v-container>
  </template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { ref } from 'vue';

const isDepositActive = ref(false);
const isSavingActive = ref(false);

const toggleButton = (buttonType) => {
  if (buttonType === 'deposit') {
    isDepositActive.value = true;
    isSavingActive.value = false;
  } else if (buttonType === 'saving') {
    isDepositActive.value = false;
    isSavingActive.value = true;
  }
};
</script>

<style scoped>
.container {
	max-width: 1100px;
    margin: 0 auto;
	font-family: "Nanum Gothic Coding", monospace;
  	font-weight: 400;
}
.text-center {
  text-align: center;
}
.button-large {
  transform: scale(1.2); /* 20% 크기 확대 */
  transition: transform 0.3s; /* 변환에 대한 부드러운 애니메이션 적용 */
}
</style>