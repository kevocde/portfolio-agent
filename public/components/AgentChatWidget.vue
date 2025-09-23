<template>
  <div class="chat">
    <div class="chat__history">
      <div v-for="message in history" class="history__message" :class="{ 'history__message--reverse': (message.role !== 'model') }">
        <span class="message__author">{{ (message.role !== 'model') ? 'Tú' : AGENT_NAME }}:</span>
        <div class="message__content">{{ message.content }}</div>
      </div>
    </div>
    <div class="chat__actioner">
      <form action="actioner__form">
        <fieldset class="form__fieldset">
          <textarea class="fieldset__message" id="user-message" v-model="userMessage" @keypress.enter.prevent="sendMessage" placeholder="Escribe y presiona ENTER" rows="1" :maxlength="MAX_MESSAGE_LENGTH"></textarea>
          <button class="fieldset__send" :disabled="!enabledMessage" @click.prevent="sendMessage"><i class="lni lni-location-arrow-right"></i></button>
        </fieldset>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, defineModel, computed, onMounted } from 'vue';
import { initChat, sendUserMessage } from '../shared/ChatServices';
import { AGENT_NAME, MAX_MESSAGE_LENGTH } from '../shared/constans';

let userMessage = defineModel('message', {required: true, default: ''});
let history = ref([]);

onMounted(() => {
  initChat(true).then(message => {
    history.value.unshift({
      role: 'model',
      content: message.text,
      time: message.time
    });
  })
})

const sendMessage = (evt) => {
  if (isNotEmptyMessage(userMessage)) {
    const content = userMessage.value;

    // Set the message to the history
    history.value.unshift({
      role: 'user',
      content: content
    });

    userMessage.value = '';

    // Send the message
    sendUserMessage(content).then(message => {
      // Set the message to the history
      history.value.unshift(message);
    });


  }
}

const enabledMessage = computed(() => {
  return isNotEmptyMessage(userMessage, 1, MAX_MESSAGE_LENGTH);
})

const isNotEmptyMessage = (model, min = 1, max = 500) => {
  return model.value.length >= min && model.value.length <= max
}
</script>

<style lang="scss">
  .chat {
    @apply max-w-md overflow-hidden rounded-lg bg-white shadow-md md:max-w-2xl text-gray-500;

    &__history {
      @apply overflow-y-auto bg-teal-50 h-96 px-6 py-4 flex flex-col-reverse gap-y-2;

      .history__message {
        @apply flex flex-col;

        .message__author {
          @apply text-sm mb-1 text-gray-800;
        }

        &--reverse {
          @apply items-end;
        }

        .message__content {
          width: fit-content;
          overflow-wrap: break-word;
          @apply bg-white px-4 py-2 max-w-full shadow-sm rounded-lg;
        }
      }

      .history__message--reverse {
        .message__content {
          width: fit-content;
          @apply bg-indigo-50;
        }
      }
    }

    &__actioner {
      @apply bg-white p-4;

      .form__fieldset {
        @apply flex content-center;

        .fieldset__message {
          overflow-wrap: break-word;
          resize: none;
          @apply focus:outline-none text-gray-500 flex-1 px-3;
        }

        .fieldset__send {
          @apply text-xl leading-none w-auto w-12 bg-indigo-500 text-indigo-50 rounded-lg flex justify-center content-center px-4 py-4;

          &:disabled {
            @apply bg-gray-400;
          }
        }
      }
    }
  }
</style>