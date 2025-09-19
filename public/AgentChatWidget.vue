<template>
  <div class="chat">
    <div class="chat__history">
      <div v-for="message in history" class="history__message" :class="{ 'history__message--reverse': (message.role !== 'model') }">
        <span class="message__author">{{ (message.role !== 'model') ? 'Tú' : 'Kevin AI' }}:</span>
        <div class="message__content">{{ message.content }}</div>
      </div>
    </div>
    <div class="chat__actioner">
      <form action="actioner__form">
        <fieldset class="form__fieldset">
          <textarea class="fieldset__message" id="user-message" v-model="userMessage" placeholder="Escribe y presiona ENTER" rows="1"></textarea>
          <button class="fieldset__send" :disabled="!enabledMessage" @click.prevent="sendMessage"><i class="lni lni-location-arrow-right"></i></button>
        </fieldset>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, defineModel, computed } from 'vue';

let userMessage = defineModel('message', {required: true, default: ''});
let history = ref([
  {
    role: 'model',
    content: 'Hola, este es un primer mensaje.'
  }
]);

const sendMessage = (evt) => {
  history.value.unshift({
    role: 'user',
    content: userMessage.value
  });
  userMessage.value = '';
}

const enabledMessage = computed(() => {
  return userMessage.value.length >= 1 && userMessage.value.length <= 500;
})
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