<template>
    <div class="finance-vocabulary">
      <h1 class="vocabulary-heading">금융 단어장</h1>
      <hr>
      <div class="vocabulary-content">
        <p class="current-word">{{ currentWord }}</p>
        <div class="current-description" v-html="currentDiscription"></div>
      </div>
    </div>
  </template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()
const currentWord = ref('');
const currentDiscription = ref('')

const stripHtmlTags = (html) => {
  const tmp = document.createElement('div');
  tmp.innerHTML = html;
  return tmp.textContent || tmp.innerText || '';
}

const updateWord = () => {
    // 현재 단어와 설명이 비어 있는 경우에만 값을 업데이트
    const index = Math.floor(Math.random() * store.vocaList.length);
    currentWord.value = store.vocaList[index].fnceDictNm;
    const description = store.vocaList[index].ksdFnceDictDescContent;
    const plainText = stripHtmlTags(description);
    console.log(currentDiscription.value);
    currentDiscription.value = plainText;
}

// updateWord 함수를 최초에 한 번 호출하여 페이지 로드 시에도 단어가 표시되도록 함
onMounted(async () => {
    await store.getVocaList();
    updateWord();
    // setInterval을 사용하여 5초마다 updateWord 함수 호출
    setInterval(updateWord, 5000);
});

</script>

<style scoped>
*{
  box-sizing: content-box;
}
.finance-vocabulary {
  height: 347px;
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  box-shadow: 0 2px 8px #DBE2EF;
  border-radius: 5px;
  overflow: hidden;
}

.vocabulary-heading {
  font-size: 24px;
  margin-bottom: 20px;
  text-align: center;
  font-family: "Nanum Gothic Coding", monospace;
  font-weight: 800;
}

.vocabulary-content {
  text-align: center;
  overflow: hidden;
  padding: 10px;
}

.current-word {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
}

.current-description {
  font-size: 16px;
  line-height: 1.5;
  text-overflow: ellipsis;
  max-height: 180px; /* 원하는 최대 높이로 설정하세요 */
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 7; /* 최대 줄 수를 설정하세요 */
}

</style>