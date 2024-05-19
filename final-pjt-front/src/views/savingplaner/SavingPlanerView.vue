<template>
<div id="chat-container">
    <div id="chat-messages"  ref="chatMessages">
        <div v-for="(message, index) in [...messages].reverse()" :key="index" class="message">
            {{ message.sender }}: {{ message.content }}
        </div>
    </div>
    <div id="user-input">
        <input type="text" placeholder="메시지를 입력하세요..." v-model.trim="userInput" @keyup.enter="sendMessage" />
        <button @click="sendMessage">전송</button>
    </div>
</div>
</template>


<script>
import axios from 'axios';

export default {
  name: 'ChatApp',
  data() {
    return {
      messages: [],
      userInput: '',

      apiEndpoint: '/openai/v1/chat/completions',
    };
  },
  methods: {
    addMessage(sender, message) {
      this.messages.push({ sender, content: message });
    },
    async fetchAIResponse(prompt) {
      const requestOptions = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.apiKey}`,
        },
        data: {
          model: 'gpt-3.5-turbo',
          messages: [{ role: 'user', content: prompt }],
          temperature: 0.8,
        },
      };

      try {
        const response = await axios('/openai/v1/chat/completions', requestOptions);
        const aiResponse = response.data.choices[0].message.content;
        return aiResponse;
      } catch (error) {
        console.error('OpenAI API 호출 중 오류 발생:', error);
        return 'OpenAI API 호출 중 오류 발생';
      }
    },
    async sendMessage() {
        const message = this.userInput.trim();
        if (message.length === 0) return;

        this.addMessage('나', message);
        this.userInput = '';

        const aiResponse = await this.fetchAIResponse(message);
        this.addMessage('챗봇', aiResponse);

        this.$nextTick(() => {
        const chatMessagesContainer = this.$refs.chatMessages;
        chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight;
  });
    },
  },
};
</script>

<style scoped>
body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}
.message {
    border-top: 1px solid #ccc;
    padding: 10px;
    margin-top: 5px;
    background-color: #e6e6e6;
}
#chat-container {
    width: 400px;
    height: 600px;
    display: flex;
    flex-direction: column;
    border: 1px solid #ccc;
}
#chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 10px;
    display: flex;
    flex-direction: column-reverse;
}
#user-input {
    display: flex;
    padding: 10px;

}
#user-input input {
    flex: 1;
    padding: 10px;
    outline: none;
}
#user-input button {
    border: none;
    background-color: #1e88e5;
    color: white;
    padding: 10px 15px;
    cursor: pointer;
}
</style>