<template>
    <ExchangeCalculator />
<h1>환율 정보</h1>
<v-table>
    <thead>
        <tr>
            <th>국가</th>
            <th>송금받을때</th>
            <th>송금보낼때</th>
            <th>매매기준율</th>
            <th>장부가격</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="exchange in exchangeStore.exchangeInfo">
            <td>{{ exchange.cur_nm }}</td>
            <td>{{ exchange.ttb }}</td>
            <td>{{ exchange.tts }}</td>
            <td>{{ exchange.deal_bas_r }}</td>
            <td>{{ exchange.bkpr }}</td>
        </tr>
    </tbody>

</v-table>

</template>

<script setup>
import ExchangeCalculator from '@/components/exchange/ExchangeCalculator.vue';
import { useCounterStore } from '@/stores/counter';
import { onMounted } from 'vue';

const exchangeStore = useCounterStore();

onMounted(() => {
    exchangeStore.exchangeMoney();
});
</script>

<style scoped>

</style>