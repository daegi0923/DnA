<template>
	<div>
    <v-row gutters class="align-center justify-center select-box">
      <v-col cols="4">
        <v-select
        v-model="finCoName"
        label="금융 회사명"
        :items="store.finCompanyList"
        variant="solo-inverted"
        ></v-select>
      </v-col>
      <v-col cols="4">
        <v-select
        v-model="savingTerm"
        label="만기(개월)"
        :items="[1, 3, 6, 12, 24, 36]"
        variant="solo-inverted"
        ></v-select>
      </v-col>
    </v-row>
    <p>* 상품 클릭시 상세페이지로 이동됩니다.</p>
		<v-data-table v-if="result.length"
      hide-default-footer>
     <thead>
       <tr :style="{ backgroundColor: '#294197', color: 'white' }">
        <!-- <th>item</th> -->
        <th>은행</th>
        <th>상품 이름</th>
        <th>기본 금리</th>
        <th>최고 금리(우대금리 포함)</th>
        <th>만기(개월)</th>
       </tr>
     </thead>
     <tbody>
       <tr v-for="deposit in result" :key="deposit.id" @click="gotoDetail(deposit.product_info.id)">
         <td>{{ deposit.product_info.kor_co_nm }}</td>
         <td>{{ deposit.product_info.fin_prdt_nm }}</td>
         <td>{{ deposit.intr_rate }}</td>
         <td>{{ deposit.intr_rate2 }}</td>
         <td>{{ deposit.save_trm }}</td>
       </tr>
     </tbody>
   </v-data-table>
	</div>
</template>

<script setup>
import axios from 'axios'
import { computed, ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'


const store = useCounterStore()
const finCoName = ref('전체보기')
const savingTerm = ref(1)
const result = computed(() => {;
  if(finCoName.value === '전체보기'){
    return store.depositList.filter(el=>el.save_trm === savingTerm.value)
  }else{
    return store.depositList.filter(el=>el.save_trm === savingTerm.value).filter(el=> el.product_info.kor_co_nm === finCoName.value)
  }
})

const gotoDetail = (depositId) => {
  router.push({ name: 'depositDetail' , params: { id: depositId }})
}

const router = useRouter()
onMounted(() => {
    store.getDepositList()
})

</script>

<style scoped>
.select-box{
  margin: 10px 0px 0px;
}
</style>