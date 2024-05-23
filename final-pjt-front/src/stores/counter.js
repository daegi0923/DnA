import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])

  const API_URL = 'http://54.206.86.165:8000'
  const token = ref(null)
  const user_id = ref(null)
  const user_name = ref(null)
  const user_nickname = ref(null)
  const depositList = ref([])
  const savingList = ref([])
  const finCompanyList = ref(['전체보기', 
  '우리은행',
  '한국스탠다드차타드은행',
  '대구은행',
  '부산은행',
  '광주은행',
  '제주은행',
  '전북은행',
  '경남은행',
  '중소기업은행',
  '한국산업은행',
  '국민은행',
  '신한은행',
  '농협은행',
  'KEB하나은행',
  '수협은행',
  '주식회사 카카오뱅크',
  '주식회사 케이뱅크',
  '토스뱅크 주식회사',
  '기타'
  ])
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  const router = useRouter()

  const getBoardsList = function () {
    axios({
      method: 'get',
      url: `${API_URL}/boards/list/`,
    })
      .then((response) => {
        // console.log(response.data);
        articles.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }
  

  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
     .then((response) => {
       console.log('회원가입 성공!')
       const password = password1
       logIn({ username, password })
     })
     .catch((error) => {
       console.log(error)
     })
  }

  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        console.log(response);
        console.log(response.data);
        console.log('login success!');
        token.value = response.data.key
        console.log(username);
        user_name.value = username
        router.push({ name : 'main' })
        console.log(user_name.value);
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const logOut = () => {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
    .then((response) => {
      console.log('logout success!');
      token.value = null
      user_id.value = null
      user_name.value = null
      user_nickname.value = null
      router.push({ name: 'start' })
    })
    .catch((error) => {
      console.log(error);
    })
  }

  const exchangeInfo = ref(null)
  const exchangeMoney = function() {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/exchanges/'
    })
    .then((response) => {
      exchangeInfo.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }

  const vocaList = ref([])
  const getVocaList = function () {
    axios({
      method: 'get',
      url: `${API_URL}/finance_vocabs/get_finance_vocas/`,
    })
     .then((response) => {
        // console.log(response.data);
        vocaList.value = response.data
      })
     .catch((error) => {
        console.log(error)
      })
    }


  const getDepositList = ()=>{
    axios({
      method: 'get',
      url: `${API_URL}/products/deposit-products/`,
    })
     .then((response) => {
        depositList.value = response.data
        console.log(depositList.value)
      })
     .catch((error) => {
        console.log(error)
      })
  }
  
  const getSavingList = ()=>{
    axios({
      method: 'get',
      url: `${API_URL}/products/saving-products/`,
    })
     .then((response) => {
        savingList.value = response.data
      })
     .catch((error) => {
        console.log(error)
      })
  }
  return { articles, API_URL, getBoardsList, signUp, logIn, token, isLogin, logOut
    , user_id, user_name, user_nickname, depositList, savingList, getDepositList,
    getSavingList,  exchangeMoney, exchangeInfo, finCompanyList, vocaList, getVocaList}

   
}, { 
  persist: {storage : sessionStorage}
 })
