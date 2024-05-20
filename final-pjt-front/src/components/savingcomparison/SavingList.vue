<template>
	<div>
		<h1>SavingList</h1>
		<!-- {{ store.depositList }} -->
    <div>
        <h2>검색하기</h2>
        <p>
        </p>
        <v-select v-model="finCoName"
        label="금융 회사명"
        :items="store.finCompanyList">
        </v-select>
        <v-select v-model="savingType"
        label="적립 유형명"
        :items="['자유적립식', '정액적립식']">
        </v-select>
        <v-select v-model="savingTerm"
        label="만기(개월)"
        :items="[1, 3, 6, 12, 24, 36]">
        </v-select>
        <v-btn @click="filterCoName">검색</v-btn>
    </div>
		<v-data-table v-if="result">
      <thead>
      <tr>
        <!-- <th>item</th> -->
        <th>은행</th>
        <th>상품 이름</th>
        <th>기본 금리</th>
        <th>최고 금리(우대금리 포함)</th>
        <th>적립 유형명</th>
        <th>만기(개월)</th>
        <th>이자 계산방식</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="saving in result" :key="saving.id" @click="gotoDetail(saving.id)">
        <td>{{ saving.kor_co_nm }}</td>
        <td>{{ saving.fin_prdt_nm }}</td>
        <td>{{ saving.savingoption_set.filter(el=>el.save_trm===savingTerm).find((el)=>el.rsrv_type_nm ===savingType).intr_rate }}</td>
        <td>{{ saving.savingoption_set.filter(el=>el.save_trm===savingTerm).find((el)=>el.rsrv_type_nm ===savingType).intr_rate2 }}</td>
        <td>{{ saving.savingoption_set.filter(el=>el.save_trm===savingTerm).find((el)=>el.rsrv_type_nm ===savingType).rsrv_type_nm }}</td>
        <td>{{ saving.savingoption_set.filter(el=>el.save_trm===savingTerm).find((el)=>el.rsrv_type_nm ===savingType).save_trm }}</td>
        <td>{{ saving.savingoption_set.filter(el=>el.save_trm===savingTerm).find((el)=>el.rsrv_type_nm ===savingType).intr_rate_type_nm }}</td>
      </tr>
      </tbody>
   </v-data-table>
	</div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
import { ClickOutside } from 'vuetify/lib/directives/index.mjs';


const store = useCounterStore()
const router = useRouter()
const result = ref([])
const finCoName = ref('전체보기')
const savingType = ref('자유적립식')
const savingTerm = ref(1)


const gotoDetail = (savingId) => {
  router.push({ name: 'savingDetail' , params: { id: savingId }})
}

const filterCoName = () => {
  if(finCoName.value === '전체보기'){
    result.value = store.savingList
  }else{
  result.value = store.savingList.filter(saving => saving.kor_co_nm === finCoName.value)
  }
  filterSavingtype()
  filterSavingTerm()
}

const filterSavingtype = () => {
  result.value = result.value.filter(el=> {
      const hasOption = el.savingoption_set.find(op=>{
        return op.rsrv_type_nm === savingType.value
      })
      return hasOption
  })
}

const filterSavingTerm = () => {
  result.value = result.value.filter(el=> {
      const hasTerm = el.savingoption_set.find(op=>{
        return op.save_trm === savingTerm.value
      })
      return hasTerm
  })
}


onMounted(() => {
		store.getSavingList()
    result.value = store.savingList
    filterSavingtype()
    filterSavingTerm()
  })
</script>

<style scoped>

</style>