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
          <!-- <v-col  cols = '12'>
            <v-date-input label="Birthday" variant="outlined" v-model = "birthday" 
            >
            </v-date-input>
          </v-col> -->
          <v-col cols = '12'>
            <v-text-field v-model = "annualIncome" label="연 수입"
            placeholder="" clearable></v-text-field>
          </v-col>
          <v-col cols = '12'>
            <v-select
              label="주 거래 은행"
              :items="bankList"
              v-model = "primaryBank"
            ></v-select>
          </v-col>
          <v-col cols = '12'>
            <v-select
              label="거주지"
              :items="provinceInput"
              v-model = "address"
            ></v-select>
          </v-col>
          <v-col cols = '12'>
            <v-select
              label="성별"
              :items="['남성','여성', '미선택']"
              v-model = "gender"
            ></v-select>
          </v-col>
        </v-row>
        <v-btn class="mt-2" type ='submit' block>제출하기</v-btn>
      </v-form>
    </v-sheet>
    <hr>
    <v-btn @click="deleteUser">회원 탈퇴</v-btn>
  </div>
</template>

<script setup>
import axios from 'axios' 
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'
import { VDateInput } from 'vuetify/labs/VDateInput'

const store = useCounterStore()

const router = useRouter()
const route = useRoute()

const emailInput = ref(null)
const annualIncome = ref(null)
const primaryBank = ref(null)
const targetSavings = ref(null)
const birthday = ref(null)
const address = ref(null)
const gender = ref(null)

const bankList = [
    '우리은행', '한국스탠다드차타드은행', '대구은행', '부산은행',
    '광주은행', '제주은행', '전북은행', '경남은행', '중소기업은행',
    '한국산업은행', '국민은행', '신한은행', '농협은행주식회사',
    '하나은행', '수협은행', '주식회사 케이뱅크',
    '주식회사 카카오뱅크', '토스뱅크 주식회사'
]


const provinceInput = ['서울특별시', '부산광역시', '대구광역시', '인천광역시',
    '광주광역시', '대전광역시', '울산광역시', '세종특별자치시',
    '경기도', '충청북도', '충청남도', '전라북도', '전라남도',
    '경상북도', '경상남도', '제주특별자치도', '강원도']
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
    birthday.value = res.data.birthday
    address.value = res.data.address
    gender.value = res.data.gender
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
      target_savings: targetSavings.value,
      // birthday: birthday.value,
      address: address.value,
      gender: gender.value,
    }
  })
  .then(()=>{
    console.log('update user info');
    console.log(route);
    router.push({name: 'profile', params: {id: store.username}})
  })
  .catch((err) => {
    console.log(err);
  })
}

const deleteUser = () => {
  axios({
    method: 'delete',
    url: 'http://127.0.0.1:8000/accounts/custom/delete/',
    headers: {
      'Authorization': `Token ${store.token}`,
    }
  })
  .then(res=>{
    console.log(res);
    store.logOut()
    router.push({name: 'login'})
  })
  .catch((err) => {
    console.log(err);
  })

}
onMounted(() => {
  getUserInfo()
})
</script>

<style scoped>

</style>