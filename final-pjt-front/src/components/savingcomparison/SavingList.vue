<template>
	<div>
    <div>
      <v-row gutters class="align-center justify-center select-box">
        <v-col cols="4">
          <v-select v-model="finCoName"
          label="금융 회사명"
          :items="store.finCompanyList"
          variant="solo-inverted">
          </v-select>
        </v-col>  
        <v-col cols="4">
          <v-select v-model="savingType"
          label="적립 유형명"
          :items="['자유적립식', '정액적립식']"
          variant="solo-inverted">
          </v-select>
        </v-col>  
        <v-col cols="4">
          <v-select v-model="savingTerm"
          label="만기(개월)"
          :items="[1, 3, 6, 12, 24, 36]"
          variant="solo-inverted">
          </v-select>
        </v-col>
      </v-row>
    </div>
    <p>* 상품 클릭시 상세페이지로 이동됩니다.</p>
		<v-data-table v-if="result"
      hide-default-footer>
      <thead>
      <tr :style="{ backgroundColor: '#294197', color: 'white' }">
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
      <tr v-for="saving in result" :key="saving.id" @click="gotoDetail(saving.product_info.id)">
        <td>{{ saving.product_info.kor_co_nm }}</td>
        <td>{{ saving.product_info.fin_prdt_nm }}</td>
        <td>{{ saving.intr_rate }}</td>
        <td>{{ saving.intr_rate2 }}</td>
        <td>{{ saving.rsrv_type_nm }}</td>
        <td>{{ saving.save_trm }}</td>
        <td>{{ saving.intr_rate_type_nm }}</td>
      </tr>
      </tbody>
   </v-data-table>
	</div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted, computed } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
import { ClickOutside } from 'vuetify/lib/directives/index.mjs';


const store = useCounterStore()
const router = useRouter()
const finCoName = ref('전체보기')
const savingType = ref('자유적립식')
const savingTerm = ref(1)

const result = computed(() => {
  if (finCoName.value === '전체보기') {

    return store.savingList
      .filter((el) => el.save_trm === savingTerm.value)
      .filter((el) => el.rsrv_type_nm === savingType.value)
  } else {
    return store.savingList
      .filter((el) => el.save_trm === savingTerm.value)
      .filter((el) => el.product_info.kor_co_nm === finCoName.value)
      .filter((el) => el.rsrv_type_nm === savingType.value)
  }
  
});


const gotoDetail = (savingId) => {
  router.push({ name: 'savingDetail' , params: { id: savingId }})
}



onMounted(() => {
		store.getSavingList()
    // console.log(store.depositList);
  })
</script>

<style scoped>
.select-box{
  margin: 10px 0px 0px;
}
</style>