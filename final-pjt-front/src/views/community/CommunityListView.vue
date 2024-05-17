<template>
  <div>
      <CommunityList/>
  </div>
</template>

<script setup>
import CommunityCreateView from '@/views/community/CommunityCreateView.vue'
import CommunityList from '@/components/community/CommunityList.vue'
import { onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
onMounted(() => {
store.getBoardsList()
})

</script>

<style scoped>

</style>