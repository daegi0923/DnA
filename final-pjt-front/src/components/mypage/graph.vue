<template>
  <Bar id="my-chart-id" :options="chartOptions" :data="chartData" class="graph"/>
</template>

<script setup>
import { computed, ref, onMounted, defineProps } from 'vue'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import { useProfileStore } from '@/stores/profile'


ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
const props = defineProps(
  {
    productType: {
      type: String,
      required: true
    }
  }
)
const title = computed(() => {
  if(props.productType === 'deposit') {
    return '예금'
  } else if(props.productType ==='saving') {
    return '적금'
  }
})
const pStore = useProfileStore()
const chartData = computed(() => {
  if(props.productType === 'deposit') {
    return {
      labels: pStore.depositsLabelList.value,
      datasets: [
        { label: '기본 금리', 
          data: pStore.depositsBasicRateList.value,
          backgroundColor: '#088082',
        },
        { label: '최고 금리',
         data: pStore.depositsMaxRateList.value,
         backgroundColor: '#294197',
        }
      ]
    }
  } else if(props.productType === 'saving'){
    return {
      labels: pStore.savingsLabelList.value,
      datasets: [
        { label: '기본 금리',
          data: pStore.savingsBasicRateList.value,
          backgroundColor: '#088082', 
        },
        { 
          label: '최고 금리',
          data: pStore.savingsMaxRateList.value,
          backgroundColor: '#294197', 
        }
      ]
    }

  }
})

const chartOptions = computed(() => (
  {
  responsive: true,
  plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: `가입한 ${title.value} 상품 비교`
      }
    }
  }
))
onMounted(() => {
  console.log(pStore.savingsMaxRateList)
})
</script>

<style>
.graph{
  font-family: "Nanum Gothic Coding", monospace;
  font-weight: 400;
}
</style>