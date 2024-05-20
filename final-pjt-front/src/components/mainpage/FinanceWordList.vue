<template>
    <h1>금융 단어장</h1>
    <div>
        <p>{{ currentWord }}</p>
        <p>{{ currentDiscription }}</p>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()
const currentWord = ref('');
const currentDiscription = ref('')

// updateWord 함수를 최초에 한 번 호출하여 페이지 로드 시에도 단어가 표시되도록 함
onMounted(async () => {
    await store.getVocaList();
    updateWord();
    // setInterval을 사용하여 5초마다 updateWord 함수 호출
    setInterval(updateWord, 5000);
});

const updateWord = () => {
    if (store.vocaList && store.vocaList.length > 0 && (!currentWord.value || !currentDiscription.value)) {
        // 현재 단어와 설명이 비어 있는 경우에만 값을 업데이트
        const index = Math.floor(Math.random() * store.vocaList.length);
        currentWord.value = store.vocaList[index].fnceDictNm;
        const description = store.vocaList[index].ksdFnceDictDescContent;
        
        // Remove only HTML tags, not content inside <ksdFnceDictDescContent>
        const tempElement = document.createElement('div');
        tempElement.innerHTML = description;
        const contentInsideTags = tempElement.querySelector('ksdFnceDictDescContent').innerHTML;
        
        // Remove HTML tags and entities from the content inside <ksdFnceDictDescContent>
        const processedContent = contentInsideTags.replace(/<[^>]+>/g, '');
        
        currentDiscription.value = processedContent;
    }
};

</script>

<style scoped>

</style>
