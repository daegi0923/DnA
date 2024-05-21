<template>
  <div class="container exchange-calculator">
    <h2 class="text-center my-4">환율 계산기</h2>
    <div class="row mb-4">
      <div class="col-md-6 d-flex align-items-center">
        <img v-if="selectedSendCountry" :src="getFlagUrl(selectedSendCountry.cur_nm)" :alt="selectedSendCountry.cur_nm" class="flag-img rounded-circle me-3">
        <div class="form-group">
          <label for="sendCountry" class="form-label">보내는 국가 :</label>
          <select id="sendCountry" class="form-select" v-model="selectedSendCountry">
            <option v-for="exchange in exchangeStore.exchangeInfo" :key="exchange.cur_unit" :value="exchange">
              {{ exchange.cur_nm }}
            </option>
          </select>
        </div>
      </div>
      <div class="col-md-6 d-flex align-items-center">
        <div class="form-group w-100">
          <label for="amount" class="form-label">보내는 금액 {{ selectedSendCountry ? selectedSendCountry.cur_unit : '' }} :</label>
          <input id="amount" type="number" class="form-control" v-model.number="amount" />
        </div>
      </div>
    </div>
    <div class="text-center mb-4">
      <button class="btn btn-primary rounded-pill" @click="swapCountries">
        <i class="fas fa-exchange-alt"></i>
      </button>
    </div>
    <div class="row mb-4">
      <div class="col-md-6 d-flex align-items-center">
        <img v-if="selectedReceiveCountry" :src="getFlagUrl(selectedReceiveCountry.cur_nm)" :alt="selectedReceiveCountry.cur_nm" class="flag-img rounded-circle me-3">
        <div class="form-group">
          <label for="receiveCountry" class="form-label">받는 국가 :</label>
          <select id="receiveCountry" class="form-select" v-model="selectedReceiveCountry">
            <option v-for="exchange in exchangeStore.exchangeInfo" :key="exchange.cur_unit" :value="exchange">
              {{ exchange.cur_nm }}
            </option>
          </select>
        </div>
      </div>
      <div class="col-md-6 d-flex justify-content-center align-items-center">
        <p class="text-center display-6 mb-0 mt-md-3">
          {{ convertedAmount !== null ? convertedAmount.toFixed(0) : '0.00' }}{{ selectedReceiveCountry ? selectedReceiveCountry.cur_unit : '' }}
        </p>
        <p class="text-muted mb-0"></p>
      </div>
    </div>
    <div class="text-center">
      <button class="btn btn-lg btn-primary rounded-pill" @click="calculateConversion">환전 계산</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';

const exchangeStore = useCounterStore();
const selectedSendCountry = ref(null);
const selectedReceiveCountry = ref(null);
const amount = ref(0);
const convertedAmount = ref(null);

const getFlagUrl = (countryName) => {
  const countryCodes = {
    '한국 원': '/flag/한국.png',
    '아랍에미리트 디르함': '/flag/아랍에미리트 디르함.jpg',
    '호주 달러': '/flag/호주.jpg',
    '바레인 디나르': '/flag/바레인.jpg',
    '브루나이 달러': '/flag/브루나이.jpg',
    '캐나다 달러': '/flag/캐나다.jpg',
    '스위스 프랑': '/flag/스위스.jpg',
    '위안화': '/flag/위안.jpg',
    '덴마아크 크로네': '/flag/덴마크.jpg',
    '유로': '/flag/유럽기.png',
    '영국 파운드': '/flag/영국.jpg',
    '인도네시아 루피아': '/flag/인도네시아.jpg',
    '일본 옌': '/flag/일본.jpg',
    '쿠웨이트 디나르': '/flag/쿠웨이트.jpg',
    '말레이지아 링기트': '/flag/말레이시아.jpg',
    '노르웨이 크로네': '/flag/노르웨이.jpg',
    '뉴질랜드 달러': '/flag/뉴질랜드.jpg',
    '사우디 리얄': '/flag/사우디.jpg',
    '스웨덴 크로나': '/flag/스웨덴.jpg',
    '싱가포르 달러': '/flag/싱가포르.jpg',
    '태국 바트': '/flag/태국.jpg',
    '미국 달러': '/flag/미국.jpg',
    '홍콩 달러': '/flag/홍콩.png',
  };
  return countryCodes[countryName] || '';
};

const parseRate = (rate) => {
  return parseFloat(rate.replace(/,/g, ''));
};

const calculateConversion = () => {
  if (selectedSendCountry.value && selectedReceiveCountry.value && amount.value > 0) {
    const sendRate = parseRate(selectedSendCountry.value.deal_bas_r);
    const receiveRate = parseRate(selectedReceiveCountry.value.deal_bas_r);

    if (selectedSendCountry.value.cur_unit === 'JPY(100)' && selectedReceiveCountry.value.cur_unit === 'KRW') {
      convertedAmount.value = (amount.value * sendRate) / 100;
    } else if (selectedSendCountry.value.cur_unit === 'IDR(100)' && selectedReceiveCountry.value.cur_unit === 'KRW') {
      convertedAmount.value = (amount.value * sendRate) / 100;
    } else if (selectedSendCountry.value.cur_unit === 'KRW' && selectedReceiveCountry.value.cur_unit == 'JPY(100)') {
      convertedAmount.value = (amount.value * 100) / receiveRate;
    } else if (selectedSendCountry.value.cur_unit === 'KRW' && selectedReceiveCountry.value.cur_unit == 'IDR(100)') {
      convertedAmount.value = (amount.value * 100) / receiveRate;
    } else {
      convertedAmount.value = (amount.value * sendRate) / receiveRate;
    }
  } else {
    convertedAmount.value = null;
  }
};

const swapCountries = () => {
  const temp = selectedSendCountry.value;
  selectedSendCountry.value = selectedReceiveCountry.value;
  selectedReceiveCountry.value = temp;
};
</script>

<style scoped>
.exchange-calculator {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.flag-img {
  width: 40px;
  height: 30px;
}

.bi-arrow-left-right {
  font-size: 24px;
}
</style>
