<template>
  <div class="news-container">
    <h1 class="news-heading">경제 뉴스 헤드라인</h1>
    <hr>
    <ul class="news-list">
      <li v-for="news in limitedNewsData" :key="news.title" class="news-item">
        <div class="news-thumbnail">
          <img v-if="news.thumbnailUrl" :src="news.thumbnailUrl" :alt="news.title" />
          <img v-else src="@/assets/noimage.png" alt="">
        </div>
        <div class="news-content">
          <h2 class="news-title">
            <a :href="news.url" target="_blank">{{ news.title }}</a>
          </h2>
          <p class="news-source">출처: {{ news.source }}</p>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted, computed } from 'vue'

const url = '/api/section/101';
const newsData = ref([]);
const limitedNewsData = computed(() => newsData.value.slice(0, 5));

const getNewsHeadlines = async () => {
  try {
    const response = await axios.get(url);
    const html = response.data;
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    const newsElements = Array.from(doc.querySelectorAll('.sa_text_strong'));
    newsData.value = newsElements.map((element) => {
      const newsItem = element.closest('.sa_item');
      const thumbnailElement = newsItem.querySelector('._LAZY_LOADING._LAZY_LOADING_INIT_HIDE');
      const thumbnailUrl = thumbnailElement ? thumbnailElement.getAttribute('data-src') : '';
      const sourceElement = newsItem.querySelector('.sa_text_press');
      const source = sourceElement ? sourceElement.textContent.trim() : '';
      return {
        title: element.textContent.trim(),
        url: element.closest('a').href,
        thumbnailUrl,
        source
      };
    });
  } catch (error) {
    console.error('Error fetching news headlines:', error);
  }
};

onMounted(() => {
  getNewsHeadlines();
});
</script>

<style scoped>
.news-container {
  box-shadow: 0 2px 8px #DBE2EF;
  border-radius: 5px;
  width: 100%;
  margin: 0 auto;
  padding: 20px;
  overflow: hidden; /* 컨테이너를 벗어나는 내용을 숨기기 위해 추가 */
  font-family: "Nanum Gothic Coding", monospace;
  font-weight: 500;
}

.news-heading {
  font-size: 24px;
  margin-bottom: 20px;
  font-family: "Nanum Gothic Coding", monospace;
  font-weight: 800;
}

.news-list {
  list-style: none;
  padding: 0;
}

.news-item {
  display: flex;
  margin-bottom: 20px;
}

.news-thumbnail img {
  width: 100px;
  height: auto;
  border-radius: 5px;
  margin-right: 20px;
}

.news-content {
  flex: 1;
  overflow: hidden; /* 컨텐츠 영역에서 넘치는 텍스트를 숨기기 위해 추가 */
}

.news-title {
  font-size: 20px;
  margin: 0 0 10px;
  white-space: nowrap; /* 한 줄로 표시하기 위해 추가 */
  overflow: hidden; /* 넘치는 텍스트를 숨기기 위해 추가 */
  text-overflow: ellipsis; /* 넘치는 텍스트를 ...로 표시하기 위해 추가 */
  font-family: "Nanum Gothic Coding", monospace;
}

.news-title a {
  text-decoration: none;
  color: #333;
  font-family: "Nanum Gothic Coding", monospace;
  font-weight: 500;
}

.news-source {
  font-size: 14px;
  color: #666;
  margin: 0;
  white-space: nowrap; /* 한 줄로 표시하기 위해 추가 */
  overflow: hidden; /* 넘치는 텍스트를 숨기기 위해 추가 */
  text-overflow: ellipsis; /* 넘치는 텍스트를 ...로 표시하기 위해 추가 */
  
}
</style>
