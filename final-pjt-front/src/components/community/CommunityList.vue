<template>
  <div class = "container">
    <table class="table">
      <thead>
        <tr>
          <th v-for="header in headers" :key="header.value" :style="{ backgroundColor: '#294197', color: 'white' }">
            {{ header.title }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in paginatedData" :key="item.id" @click="goToDetail(item)">
          <td>{{ item.id }}</td>
          <td>{{ item.title }}<span v-if="item.comment_count>0"> [{{ item.comment_count }}]</span></td>
          <td>{{ item.username }}</td>
          <td>{{ formatDate(item.created_at) }}</td>
          <td>{{ item.views }}</td>
        </tr>
      </tbody>
    </table>
    <div class="board-nav">
      <v-btn @click="goToList" class ="btn-nav listbtn">목록</v-btn>
      <nav aria-label="..." >
        <ul class="pagination">
          <li :class="['page-item', currentPage === 1 ? 'disabled' : '']">
            <span class="btn-not-selected page-link bi bi-arrow-left" @click="prevPage"></span>
          </li>
          <li v-for="pageNumber in totalPages" :key="pageNumber" :class="['page-item', currentPage === pageNumber ? 'active' : '']">
            <span v-if="currentPage === pageNumber" class="page-link btn-nav">{{ pageNumber }}</span>
            <span v-else class="page-link btn-not-selected" @click="goToPage(pageNumber)">{{ pageNumber }}</span>
          </li>
          <li :class="['page-item', currentPage === totalPages ? 'disabled' : '']">
            <span class="page-link btn-not-selected bi bi-arrow-right " @click="nextPage"></span>
          </li>
        </ul>
      </nav>
      <v-btn @click="goToCreate" v-if="store.isLogin" class ="btn-nav"><font-awesome-icon :icon="['fas', 'pen-nib']" /></v-btn>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const router = useRouter()
const itemsPerPage = 10
const currentPage = ref(1)

const headers = ref([
  { title: '글 번호', value: 'id' },
  { title: '제목', value: 'title' },
  { title: '작성자', value: 'username' },
  { title: '작성일시', value: 'created_at' },
  { title: '조회수', value: 'views' },
])

const resultData = computed(() =>
  store.articles
    .map(el => ({
      id: el.id,
      title: el.title,
      username: el.user.username,
      views: el.views,
      comment_count: el.comment_count,
      created_at: el.created_at, // Keep original date format here
    }))
    .sort((a, b) => b.id - a.id)
)

const paginatedData = computed(() => {
  const startIndex = (currentPage.value - 1) * itemsPerPage
  const endIndex = startIndex + itemsPerPage
  return resultData.value.slice(startIndex, endIndex)
})

const totalPages = computed(() => Math.ceil(resultData.value.length / itemsPerPage))

const formatDate = (dateStr) => {
  const date = new Date(dateStr)
  const today = new Date()
  if (date.toDateString() === today.toDateString()) {
    return `${date.getHours()}:${date.getMinutes().toString().padStart(2, '0')}`
  } else {
    return `${date.getUTCFullYear()}.${(date.getMonth() + 1).toString().padStart(2, '0')}.${date.getDate().toString().padStart(2, '0')}`
  }
}

const goToDetail = (item) => {
  router.push({ name: 'community-detail', params: { id: item.id } })
}

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--
  }
}

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
  }
}

const goToPage = (pageNumber) => {
  currentPage.value = pageNumber
}
const goToList = () => {
  router.push({ name: 'community-list' })
}
const goToCreate = () => {
  router.push({ name: 'community-create' })
}

</script>
<style scoped>
.container {
  max-width: 100%px;
    font-family: "Nanum Gothic Coding", monospace;
  font-weight: 400;
}
.board-nav {
  display:flex;
  justify-content: space-between;
}
.btn-nav {
  background-color: #3F72AF;
  color: white;
  border-color:#3F72AF;
}
.btn-not-selected {
  background-color: white;
  color : #3F72AF;

}
.listbtn{
  visibility: hidden;
}

</style>