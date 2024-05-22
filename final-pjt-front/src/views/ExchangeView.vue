<template>
    <ExchangeCalculator />
<div class="container">
    <h1>실시간 환율 정보</h1>
    <v-table>
        <thead>
            <tr :style="{ backgroundColor: '#294197', color: 'white' }">
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
</div>

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
.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'Arial', sans-serif;
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    margin-top: 20px;
    font-family: "Nanum Gothic Coding", monospace;
    font-weight: 400;
    margin-bottom: 20px;
}
h1{
    margin: 10px;
    font-family: "Nanum Gothic Coding", monospace;
    font-weight: 800;
}
</style>