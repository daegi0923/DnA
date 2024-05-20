<template>
  <div>
    <h1>회원정보 수정</h1>
    <v-sheet class="mx-auto" max-width="500">
      <v-form  @submit.prevent="updateUserInfo">
        <v-row>
          <v-col cols = '12'>
            <v-text-field v-model = "emailInput" label="Email address"
            placeholder=""  clearable></v-text-field>
          </v-col>
          <v-col  cols = '12'>
            <v-text-field v-model = "targetSavings" label="목표 저축 금액"
            placeholder=""  clearable></v-text-field>
          </v-col>
          <v-col>
            <v-text-field v-model = "annualIncome" label="연 수입"
            placeholder="" clearable></v-text-field>
          </v-col>
          <v-col cols = '12'>
            <v-text-field v-model = "primaryBank" label="주 거래 은행"
            placeholder=""  clearable></v-text-field>
          </v-col>
        </v-row>
        <v-btn class="mt-2" type ='submit' block>제출하기</v-btn>
      </v-form>
    </v-sheet>
  </div>
</template>

<script setup>
import axios from 'axios' 
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'
const store = useCounterStore()

const router = useRouter()
const route = useRoute()

const emailInput = ref('')
const annualIncome = ref('')
const primaryBank = ref('')
const targetSavings = ref('')

const getUserInfo = () => {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/accounts/custom/update-user/',
    headers: {
      'Authorization': `Token ${store.token}`,
    }
  })
  .then((res) => {
    // console.log(res.data);
    emailInput.value = res.data.email
    annualIncome.value = res.data.annual_income
    primaryBank.value = res.data.primary_bank
    targetSavings.value = res.data.target_savings
  })
  .catch((err) => {
    console.log(err);
  })
}

const updateUserInfo = () => {
  axios({
    method: 'put',
    url: 'http://127.0.0.1:8000/accounts/custom/update-user/',
    headers: {
      'Authorization': `Token ${store.token}`,
    },
    data: {
      email: emailInput.value,
      annual_income: annualIncome.value,
      primary_bank: primaryBank.value,
      target_savings: targetSavings.value
    }
  })
  .then(()=>{
    console.log('update user info');
  })
  .error((err) => {
    console.log(err);
  })
}
onMounted(() => {
  getUserInfo()
})
</script>

<style scoped>

</style>