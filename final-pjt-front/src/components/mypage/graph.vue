<template>
  <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
</template>

<script setup>
import { computed, ref, onUpdated } from 'vue'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import { useProfileStore } from '@/stores/profile'


ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const pStore = useProfileStore()
const chartData = computed(() => {
  return {
    labels: pStore.labels.value,
    datasets: [
      { label: '기본 금리', data: pStore.basicRates.value },
      { label: '최고 금리', data: pStore.maxRates.value }
    ]
  }
})

const chartOptions = computed(() => ({
  responsive: true
}))
</script>