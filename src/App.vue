<script setup lang="ts">
import PlayerSheet from "./components/PlayerSheet.vue";
const pitchers = defineModel();

fetch("http://localhost/api/v1/players/?position=1&skip=0").then(async response => {
  const isJson = response.headers.get('content-type')?.includes('application/json');
  const data = isJson && await response.json();
  pitchers.value = data
})
</script>

<template>
  <PlayerSheet />
</template>

<style scoped></style>
