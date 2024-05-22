<template>
  <div class="container detail-view">
    <div v-if="article" key="article">
      <h1>{{ article.title }}</h1>
      <hr>
      <div class="article-header row">
        <div class="col-md-4"><p>ID: {{ article.id }}</p></div>
        <div class="col-md-4"><p>작성자: {{ article.user.username }}</p></div>
        <div class="col-md-4"><p>작성일: {{ formatDate(article.created_at) }}</p></div>
      </div>
      <div class="article-body">
        <p>{{ article.content }}</p>
        <p class="updated-date">최근 수정일: {{ formatDate(article.updated_at) }}</p>
      </div>
    </div>
    <div class="article-actions">
      <router-link class="btn btn-secondary my-3" to="/community/list/"><font-awesome-icon :icon="['fas', 'arrow-left']" /></router-link>
      <div v-if="isWriter" class="button-group">
        <button @click="deleteBoard" class="btn btn-danger">
          <font-awesome-icon :icon="['far', 'trash-can']" />
        </button>
        <button @click="updateBoard" class="btn btn-success">
          <font-awesome-icon icon="fa-solid fa-pen" />
        </button>
      </div>
    </div>
    <div v-if="article ">
      <h3>Comments</h3>
      <transition-group name="comment-list" tag="ul" class="list-group">
      <div v-if="article.comment_set.length>0">
        <li v-for="(comment, index) in article.comment_set" :key="comment.id" class="list-group-item d-flex justify-content-between align-items-center">
          <p>{{ comment.user.username }} : {{ comment.content }}</p>
          <button v-if="store.user_name === comment.user.username" @click="deleteComment(comment.id)" class="btn btn-danger btn-sm"><font-awesome-icon :icon="['far', 'trash-can']" /></button>
        </li>
      </div>
      <div v-else class="list-group-item">
        <p>아직 댓글이 없습니다.</p>
      </div>
      </transition-group>
      
    </div>
    <form v-if= "store.isLogin" @submit.prevent="createComment" class="comment-form">
      <div class="input-group my-3">
        <input type="text" id="content" v-model.trim="content" placeholder="댓글 입력" class="form-control" />
        <button type="submit" class="btn btn-primary"><font-awesome-icon :icon="['fas', 'comment']" style="color: #ffffff;" /></button>
      </div>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const content = ref(null)

const isWriter = computed(()=>{
  return article.value&&(article.value.user.username === store.user_name)
})

const loadBoard = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/boards/${route.params.id}/`,
  })
    .then((response) => {
      article.value = response.data
      updateBoardViews()
    })
    .catch((error) => {
      console.log(error)
    })
}

onMounted(() => {
  loadBoard()
})

const deleteBoard = () => {
  if(!confirm('삭제하시면 복구할수 없습니다. \n 정말로 삭제하시겠습니까??')){
    return false;
  }
  axios({
    method: `delete`,
    url: `${store.API_URL}/boards/${route.params.id}/`,
  })
    .then((response) => {
      console.log('delete!')
      router.push({ name: 'community-list' })
    })
    .catch((error) => {
      console.log(error)
    })
}

const updateBoard = () => {
  router.push({
    name: 'community-update',
    params: {
      id: route.params.id,
      title: article.value.title,
      content: article.value.content,
    },
  })
}

const createComment = () => {
  axios({
    method: 'post',
    url: `${store.API_URL}/boards/comment/${route.params.id}/`,
    data: {
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((result) => {
      loadBoard()
      content.value = null
    })
    .catch((err) => {
      console.log(err)
    })
}

const deleteComment = (commentId) => {
  if(!confirm('삭제하시면 복구할수 없습니다. \n 정말로 삭제하시겠습니까??')){
    return false;
  }
  axios({
    method: 'delete',
    url: `${store.API_URL}/boards/comment/${commentId}/delete/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      loadBoard()
    })
    .catch((err) => {
      console.log(err)
    })
}

const updateBoardViews = () => {
  axios({
    method: 'put',
    url: `${store.API_URL}/boards/${route.params.id}/views/`,
  })
    .then((res) => {})
    .catch((err) => {
      console.log(err)
    })
}

const formatDate = (dateStr) => {
  const date = new Date(dateStr)
  return `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')}`
}
</script>

<style scoped>
.detail-view {
  max-width: 100%;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  font-family: "Nanum Gothic Coding", monospace;
  font-weight: 400;
}

.article-body .updated-date {
  text-align: right;
  color: #888;
  margin-top: 10px;
}
.article-actions {
  display : flex;
  align-items: center;
  justify-content: space-between;
}
/* 애니메이션 스타일 */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.comment-list-enter-active,
.comment-list-leave-active {
  transition: all 0.3s;
}

.comment-list-enter-from,
.comment-list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

.button-group .btn {
  margin-right: 10px; /* 버튼 간의 간격 설정 */
}

.button-group .btn:last-child {
  margin-right: 0; /* 마지막 버튼의 오른쪽 마진 제거 */
}
</style>
