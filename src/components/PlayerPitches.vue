<script setup lang="ts">
import { ref, watchEffect } from "vue";
import pitchTypes from "../assets/pitchTypes.json";
import { getTeamColors } from "../helpers";

const pitches = ref();
const tasks = ref();
const ready = ref(false);
const pitcher = defineProps({
  mlbId: Number,
  currentTeamId: {
    type: Number,
    required: true,
  },
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

function getColorScheme(currentTeamId: number) {
  var teamColors = getTeamColors(currentTeamId);
  if (teamColors && "first" in teamColors && "second" in teamColors) {
    return { background: teamColors["first"], color: teamColors["second"] };
  }

  return "";
}
</script>

<template>
  <v-container>
    <v-row>
      <v-col v-show="!ready">
        <div class="text-h5 mb-4" v-if="tasks.length > 1">
          {{ "Downloading " + tasks.length + " seasons..." }}
        </div>
        <div class="text-h5 mb-4" v-if="tasks.length == 1">
          {{ "Downloading " + tasks.length + " season..." }}
        </div>
        <v-progress-linear
          indeterminate
          v-show="!ready && tasks && tasks.length != 0"
        ></v-progress-linear>
      </v-col>
      <v-col
        cols="12"
        v-for="(pitch, index) in pitches"
        v-bind:key="index"
        v-show="ready"
      >
        <div
          class="text-h5 text-center mt-2"
          :style="getColorScheme(pitcher.currentTeamId)"
        >
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
