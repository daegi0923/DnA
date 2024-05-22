<template>
  <div class="d-flex">
    <nav id="sidebarMenu" class="d-lg-block sidebar bg-white">
      <div class="position-sticky">
        <div class="profile_area">
          <div class="profile_inner d-flex flex-column align-items-center">
            <img class="rounded-circle" src="@/assets/default.png" width="84" height="84" alt="프로필 이미지">
            <div class="profile text-center" v-if="pStore.userInfo">
              <p class="useid">{{ pStore.userInfo.username }}</p>
              <p class="usemail">{{ pStore.userInfo.email }}</p>
            </div>
          </div>
        </div>
        <ul class="list-group list-group-flush mx-3 mt-4">
          <li
            v-for="(item, index) in menuItems"
            :key="index"
            :class="['list-group-item', 'list-group-item-action', isCurrentRoute(item.route) ? 'active' : '']"
            @click="navigateTo(item.route)"
          >
            {{ item.title }}
          </li>
        </ul>
      </div>
    </nav>
    <div class="container">
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useProfileStore } from '@/stores/profile'
import { useRouter, useRoute } from 'vue-router'

const pStore = useProfileStore()
const router = useRouter()
const route = useRoute()

const menuItems = ref([
  { title: '내 프로필', route: { name: 'profile', params: { username: route.params.username } } },
  { title: '금융 프로필', route: { name: 'Finance-profile', params: { username: route.params.username } } },
  { title: '내가 쓴 글', route: { name: 'User-Posts', params: { username: route.params.username } } },
  { title: '금융 상품 맞춤 추천', route: { name: 'Recommend', params: { username: route.params.username } } },
  { title: '개인 정보 수정', route: { name: 'UpdateUser', params: { username: route.params.username } } },
])

const isCurrentRoute = (routeItem) => {
  return route.name === routeItem.name && JSON.stringify(route.params) === JSON.stringify(routeItem.params)
}

const navigateTo = (routeItem) => {
  router.push(routeItem)
}
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  font-family: "Nanum Gothic Coding", monospace;
  font-weight: 400;
}

.sidebar {
  top: 0;
  bottom: 0;
  left: 30px;
  padding: 58px 0 0; /* Height of navbar */
  box-shadow: 0 2px 5px 0 rgb(0 0 0 / 5%), 0 2px 10px 0 rgb(0 0 0 / 5%);
  width: 240px;
  z-index: 600;
}

.active {
  background-color: #112D4E;
  border:#112D4E;
}
</style>