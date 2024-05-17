<template>
<p>exchange</p>
<h1>환율 정보</h1>
<ExchangeCalculator />
<div v-for="exchange in exchangeStore.exchangeInfo">
    <p>국가: {{ exchange.cur_nm }}</p>
    <p>국가코드: {{ exchange.cur_unit }}</p>
    <p>송금받을때 : {{ exchange.ttb }}</p>
    <p>송금보낼때 : {{ exchange.tts }}</p>
    <p>매매기준율 : {{ exchange.deal_bas_r }}</p>
    <p>장부가격 : {{ exchange.bkpr }}</p>
    <hr>
</div>
</template>

<script setup>
import ExchangeCalculator from '@/components/exchange/ExchangeCalculator..vue';
import { useCounterStore } from '@/stores/counter';
import { onMounted } from 'vue';

const exchangeStore = useCounterStore();

onMounted(() => {
    exchangeStore.exchangeMoney();
});
</script>

<style scoped>

</style>