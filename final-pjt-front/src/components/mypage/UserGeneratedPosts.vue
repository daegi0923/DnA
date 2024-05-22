<template>
  <div class="container-fluid">
    <div class="col-12 mb-4">
      <div class="card">
        <h3 class="card-header text-white card-title" >작성한 게시글 목록</h3>
        <ul class="list-group list-group-flush">
          <li class="list-group-item" v-for="post in pStore.userInfo.board_set" :key="post.id">
            <router-link :to="`/community/${post.id}`">{{ post.title }}</router-link>
          </li>
        </ul>
      </div>
    </div>
    <div class="col-12">
      <div class="card">
        <h3 class="card-header text-white card-title" >작성한 댓글 목록</h3>
        <ul class="list-group list-group-flush">
          <li class="list-group-item" v-for="comment in pStore.userInfo.comment_set" :key="comment.id">
            <router-link :to="`/community/${comment.board.id}`">{{ comment.content }}</router-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useProfileStore } from '@/stores/profile'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'

const store = useCounterStore()
const pStore = useProfileStore()

const router = useRouter()
const route = useRoute()

</script>

<style scoped>
.card-title {
  background-color: #112D4E;
}
</style> 
