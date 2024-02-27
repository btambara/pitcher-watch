<script setup lang="ts">
import { ref, watchEffect } from "vue";
import pitchTypes from "../assets/pitchTypes.json";

const pitches = ref();
const ready = ref(false);
const pitcher = defineProps({
  mlbId: Number,
});

watchEffect(async () => {
  fetch(
    `http://localhost/api/v1/player/pitches/all/${pitcher.mlbId}?skip=0`,
  ).then(async (response) => {
    pitches.value = await response.json();
    if (pitches.value) {
      let seasonPitches = [];
      for (var pitchStats of pitches.value) {
        seasonPitches.push(pitchStats);
      }
      pitches.value = seasonPitches;
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
      <v-skeleton-loader type="table-heading" v-show="!ready"></v-skeleton-loader>
      <v-skeleton-loader type="table-tbody" v-show="!ready"></v-skeleton-loader>
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
