<template>
	<div>
		<h1>DepositList</h1>
		<!-- {{ store.depositList }} -->
    <div>
      <h2>검색하기</h2>
      <p>
      </p>
      <v-select v-model="finCoName"
      label="금융 회사명"
      :items="store.finCompanyList">
      </v-select>
      <v-select v-model="savingTerm"
      label="만기(개월)"
      :items="[1, 3, 6, 12, 24, 36]">
      </v-select>
      <v-btn @click="filterCoName">검색</v-btn>
    </div>

		<v-table v-if="result.length">
     <thead>
       <tr>
        <!-- <th>item</th> -->
        <th>은행</th>
        <th>상품 이름</th>
        <th>기본 금리</th>
        <th>최고 금리(우대금리 포함)</th>
        <th>만기(개월)</th>
       </tr>
     </thead>
     <tbody>
       <tr v-for="deposit in result" :key="deposit.id" @click="gotoDetail(deposit.id)">
         <td>{{ deposit.kor_co_nm }}</td>
         <td>{{ deposit.fin_prdt_nm }}</td>
         <td v-if="savingTerm">{{ deposit.depositoption_set.find(el=>el.save_trm === savingTerm).intr_rate }}</td>
         <td v-if="savingTerm">{{ deposit.depositoption_set.find(el=>el.save_trm === savingTerm).intr_rate2 }}</td>
         <td v-if="savingTerm">{{ deposit.depositoption_set.find(el=>el.save_trm === savingTerm).save_trm }}</td>
       </tr>
     </tbody>
   </v-table>
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
const result = ref([])

const selectedOption = computed((product) => {
  return product.depositoption_set.find(el=>el.save_trm === savingTerm.value)
})

const gotoDetail = (depositId) => {
  router.push({ name: 'depositDetail' , params: { id: depositId }})
}

const filterCoName = () => {
  if(finCoName.value === '전체보기'){
    result.value = store.depositList
  }else{
    result.value = store.depositList.filter(saving => saving.kor_co_nm === finCoName.value)
  }
  filterSavingTerm()
}
const filterSavingTerm = () => {
  result.value = result.value.filter(el=> {
    const hasTerm = el.depositoption_set.find(op=>{
      return op.save_trm === savingTerm.value
    })
    return hasTerm
  })
}
const sortByOption = (option) => {
  console.log('click');
  result.value = result.value.sort((a, b) => {
    console.log(a, b);


    return a[option] - b[option]
  })
}
const router = useRouter()
onMounted(() => {
    store.getDepositList()
    result.value = store.depositList
})

</script>

<style scoped>

</style>