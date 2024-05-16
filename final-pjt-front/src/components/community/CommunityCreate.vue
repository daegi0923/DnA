<template>
    <div>
      <h1 v-if="isUpdate">게시글 수정</h1>
      <h1 v-else>게시글 작성</h1>

      <form @submit.prevent="switchMethod">
        <div>
          <label for="title">제목 : </label>
          <input type="text" v-model.trim="title" id="title">
        </div>
        <div>
          <label for="content">내용 : </label>
          <textarea v-model.trim="content" id="content"></textarea>
        </div>
        <input type="submit">
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
// console.log(router);
console.log(route);
console.log(router)
console.log(route.params.id);
if (route.params.id) {
  isUpdate.value = true
  const currArticle = store.articles.find((article) => article.id == route.params.id)
  title.value = currArticle.title
  content.value = currArticle.content
}
else{
  isUpdate.value = false
}
const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/boards/create/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      console.log('게시글 생성 성공!');
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
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then(res => {
    console.log('게시글 수정 성공!');
    router.push({ name: 'community-detail' , params: { id: route.params.id } })
    
  })
}
const switchMethod = () => {
  console.log(isUpdate.value);
  if(isUpdate.value){
    updateArticle()
    console.log('update');
  } else {
    createArticle()
    console.log('create');
  }

}
</script>

<style scoped>

</style>