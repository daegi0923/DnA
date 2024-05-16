<template>
  <div>
      <h1>DetailView</h1>
      <div v-if="article">
      <!-- {{ article }} -->
      <p>{{ article.id }}</p>
      <p>{{ article.title }}</p>
      <p>{{ article.content }}</p>
      <p>{{ article.created_at }}</p>
      <p>{{ article.updated_at }}</p>
      <p>
        <!-- {{ article.comment_set }} -->
      </p>
      </div>
      <button @click="delete_board">Delete</button>
      <button @click="update_board">Update</button>
      <router-link to="/community-list">Back</router-link>

      <div v-if="article">
        <ul v-for="(comment, index) in article.comment_set" :key="index">
          <li>{{ comment.content }}</li>
        </ul>
      </div>
      <form  @submit.prevent="create_comment">
        <input type="text" id = "content" v-model.trim="content">
        <input type="submit">
      </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'
import CommunityComment from '@/components/community/CommunityComment.vue'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const comments = ref(null)
const content = ref(null)

const loadBoard = () => {
  axios({
  method: 'get',
  url: `${store.API_URL}/boards/${route.params.id}/`
})
  .then((response) => {
    console.log(response.data)
    article.value = response.data
  })
  .catch((error) => {
    console.log(error)
  })

}

onMounted(() => {
  loadBoard()
})

const delete_board = () =>{
  axios({
    method: `delete`,
    url: `${store.API_URL}/boards/${route.params.id}/`
  }).then((response) => {
    console.log('delete!');
    router.push({ name: 'community-list' })
  })
  .catch(error => {
    console.log(error);
  })
}

const update_board = () => {
  console.log(article.value);
  router.push({ name: 'community-update', 
  params: {   id: route.params.id ,
     title : article.value.title, 
     content : article.value.content
    } })
    console.log(route)
}

const create_comment = () => {
  console.log(route.params.id);
  axios({
    method : 'post',
    url : `${store.API_URL}/boards/comment/${route.params.id}/`,
    data : {
      content : content.value
    },
    headers: {
      Authorization: `Token ${store.token}`,
    }
  })
  .then((result) => {
    loadBoard()
    console.log(result.data);
    content.value = null;
  }).catch((err) => {
    console.log(err);
  });

}

</script>

<style scoped>

</style>