<template>
	<div>
		<h1>DepositList</h1>
		<!-- {{ store.depositList }} -->
		<v-table v-if="store.depositList">
     <thead>
       <tr>
         <!-- <th>item</th> -->
         <th>ID</th>
         <th>은행</th>
         <th>상품코드</th>
         <th>상품 이름</th>
       </tr>
     </thead>
     <tbody>
       <tr v-for="deposit in store.depositList" :key="deposit.id" @click="gotoDetail(deposit.id)">
			 	 <!-- <td>{{ deposit }}</td> -->
         <td>{{ deposit.fin_prdt_cd }}</td>
         <td>{{ deposit.fin_co_no }}</td>
         <td>{{ deposit.kor_co_nm }}</td>
         <td>{{ deposit.fin_prdt_nm }}</td>
       </tr>
     </tbody>
   </v-table>
	</div>
</template>

<script setup>
import axios from 'axios'
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
import CommunityListItem from '@/components/community/CommunityListItem.vue'


const store = useCounterStore()
const router = useRouter()
onMounted(() => {
		store.getDepositList()
})

const gotoDetail = (depositId) => {
  router.push({ name: 'depositDetail' , params: { id: depositId }})
}


</script>

<style scoped>

</style>