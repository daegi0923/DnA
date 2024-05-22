<template>
    <div class="container">
        <h1>게시판</h1>
        <RouterView class='community-view'></RouterView>
    </div>
</template>

<script setup>
import CommunityCreateView from '@/views/community/CommunityCreateView.vue'
import CommunityList from '@/components/community/CommunityList.vue'
import { onMounted } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
onMounted(() => {
  store.getBoardsList()
})
const router = useRouter()
</script>

<style scoped>
.container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
h1{
  font-family: "Nanum Gothic Coding", monospace;
  font-weight: 800;
  margin-bottom: 20px;
}
</style>