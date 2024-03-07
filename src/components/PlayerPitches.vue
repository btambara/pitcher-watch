<script setup lang="ts">
import { ref, watchEffect } from "vue";
import pitchTypes from "../assets/pitchTypes.json";

const pitches = ref();
const tasks = ref();
const ready = ref(false);
const pitcher = defineProps({
  mlbId: Number,
});

watchEffect(async () => {
  fetch(
    `http://localhost/api/v1/player/pitches/all/${pitcher.mlbId}?skip=0`,
  ).then(async (response) => {
    const answer = await response.json();

    for (var item of answer) {
      if ("UUID" in item) {
        tasks.value = answer;
        break;
      }
    }

    if (tasks.value) {
      let tasksInterval = setInterval(() => {
        for (var task of tasks.value) {
          fetch(`http://localhost/api/v1/celery/?id=${task["UUID"]}`).then(
            async (response) => {
              let result = await response.json();

              if ("result" in result && result["result"] == true) {
                const index = tasks.value.indexOf(task);
                tasks.value.splice(index, 1);
              }
            },
          );
        }

        if (!tasks.value || tasks.value.length == 0) {
          fetch(
            `http://localhost/api/v1/player/pitches/all/${pitcher.mlbId}?skip=0`,
          ).then(async (response) => {
            const answer = await response.json();
            pitches.value = answer;
            ready.value = true;
            clearInterval(tasksInterval);
          });
        }
      }, 14000);
    } else {
      pitches.value = answer;
      ready.value = true;
    }
  });
});

function findTooltip(code: string) {
  for (let i = 0; i < pitchTypes.length; i++) {
    if (pitchTypes[i].code.toLowerCase() === code.toLowerCase()) {
      return pitchTypes[i].description;
    }
  }

  return "UNKNOWN";
}
</script>

<template>
  <v-container>
    <v-row>
      <v-col v-show="!ready">
        <div class="text-h5 mb-4" v-if="tasks">
          {{ "Downloading " + (tasks.length + 1) + " seasons..." }}
        </div>
        <v-progress-linear
          indeterminate
          v-show="!ready && tasks"
        ></v-progress-linear>
      </v-col>
      <v-col
        v-for="(pitch, index) in pitches"
        v-bind:key="index"
        v-show="ready"
      >
        <div class="text-h5 text-center mt-2 bg-primary">
          {{ pitch["season"] }}
        </div>

        <v-table v-show="ready">
          <thead>
            <tr>
              <th
                class="text-center"
                v-for="pitchStat in pitch.pitches"
                :key="pitchStat.code"
              >
                <v-tooltip :text="findTooltip(pitchStat.code)" location="top">
                  <template v-slot:activator="{ props }">
                    <v-btn variant="plain" v-bind="props">{{
                      pitchStat.code
                    }}</v-btn>
                  </template>
                </v-tooltip>
              </th>
            </tr>
          </thead>

          <tbody>
            <tr>
              <td
                v-for="(pitchStat, index) in pitch.pitches"
                v-bind:key="index"
              >
                {{ pitchStat.amount }}
              </td>
            </tr>
          </tbody>
        </v-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
td {
  text-align: center;
}
</style>
