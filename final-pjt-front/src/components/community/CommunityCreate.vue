<template>
  <div class="create-update-view">
    <h1 class="title" v-if="isUpdate">게시글 수정</h1>
    <h1 class="title" v-else>새 게시글 작성</h1>
    <form @submit.prevent="switchMethod" class="form">
      <div class="form-group">
        <label for="title">제목:</label>
        <input type="text" v-model.trim="title" id="title" class="form-control" required>
      </div>
      <div class="form-group">
        <label for="content">내용:</label>
        <textarea v-model.trim="content" id="content" class="form-control" rows="6" required></textarea>
      </div>
      <div class="form-actions">
        <button type="submit" class="btn btn-primary">{{ isUpdate ? '수정' : '작성' }}</button>
        <router-link to="/community/list" class="btn btn-secondary">취소</router-link>
      </div>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'

const store = useCounterStore()
const title = ref(null)
const content = ref(null)
const router = useRouter()
const route = useRoute()
const isUpdate = ref(false)

if (route.params.id) {
  isUpdate.value = true
  const currArticle = store.articles.find((article) => article.id == route.params.id)
  title.value = currArticle.title
  content.value = currArticle.content
} else {
  isUpdate.value = false
}

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/boards/create/`,
    data: { title: title.value, content: content.value },
    headers: { Authorization: `Token ${store.token}` }
  })
    .then((response) => {
      console.log('게시글 생성 성공!')
      router.push({ name: 'community-list' })
    })
    .catch((error) => {
      console.log(error)
    })
}

const updateArticle = () => {
  axios({
    method: 'put',
    url: `${store.API_URL}/boards/${route.params.id}/`,
    data: { title: title.value, content: content.value },
    headers: { Authorization: `Token ${store.token}` }
  })
    .then(res => {
      console.log('게시글 수정 성공!')
      router.push({ name: 'community-detail', params: { id: route.params.id } })
    })
}

const switchMethod = () => {
  if (isUpdate.value) {
    updateArticle()
  } else {
    createArticle()
  }
}
</script>

<style scoped>
.create-update-view {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 20px;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

.btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-primary {
  background-color: #294197;
  color: #fff;
}

.btn-secondary {
  background-color: #ccc;
  color: #333;
}
</style>