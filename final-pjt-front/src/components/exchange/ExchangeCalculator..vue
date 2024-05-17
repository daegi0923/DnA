<template>
    <div>
      <h2>환율 계산기</h2>
      <div>
        <label for="sendCountry">보내는 국가:</label>
        <select id="sendCountry" v-model="selectedSendCountry">
          <option v-for="exchange in exchangeStore.exchangeInfo" :key="exchange.cur_unit" :value="exchange">
            {{ exchange.cur_nm }}
          </option>
        </select>
      </div>
      <div>
        <label for="amount">보내는 금액({{ selectedSendCountry ? selectedSendCountry.cur_unit : '' }}):</label>
        <input id="amount" type="number" v-model.number="amount" />
      </div>
      <i @click="swapCountries" class="fa-solid fa-arrow-right-arrow-left"></i>
      <div>
        <label for="receiveCountry">받는 국가:</label>
        <select id="receiveCountry" v-model="selectedReceiveCountry">
          <option v-for="exchange in exchangeStore.exchangeInfo" :key="exchange.cur_unit" :value="exchange">
            {{ exchange.cur_nm }}
          </option>
        </select>
      </div>
      <button @click="calculateConversion">환전 계산</button>
      <p>환전 금액: {{ convertedAmount.toFixed(2) }}</p>
      <div v-if="convertedAmount !== null">
      </div>
    </div>
  </template>
  
<script setup>
import { ref, computed } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { parse } from 'vue/compiler-sfc';


const exchangeStore = useCounterStore();
const selectedSendCountry = ref(null);
const selectedReceiveCountry = ref(null);
const amount = ref(0);
const convertedAmount = ref(0);

const parseRate = (rate) => {
  // 쉼표를 제거하고 숫자로 변환
  return parseFloat(rate.replace(/,/g, ''));
};


const calculateConversion = () => {
      if (selectedSendCountry.value && selectedReceiveCountry.value && amount.value > 0) {
        const sendRate = parseRate(selectedSendCountry.value.deal_bas_r);
        const receiveRate = parseRate(selectedReceiveCountry.value.deal_bas_r)

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
