<script setup lang="ts">
import CareerTable from "./CareerTable.vue";
import CareerStats from "./CareerTable.vue";
import SeasonTable from "./SeasonTable.vue";
import pitchers from "../assets/pitchers.json";
import { watchEffect, ref } from "vue";

const stats = ref();
const career = ref(CareerStats);
const season = ref();
const ready = ref(false);
const pitcher = defineProps({
  mlbId: Number,
});

watchEffect(async () => {
  fetch(
    `http://localhost/api/v1/player/stats/all/${pitcher.mlbId}?skip=0`,
  ).then(async (response) => {
    stats.value = await response.json();
    if (stats.value) {
      let seasonStats = [];
      for (var stat of stats.value) {
        if (stat["season"] == -1 && stat["team_id"] == -1) {
          career.value = stat;
        } else {
          seasonStats.push(stat);
        }
      }
      season.value = seasonStats;
      ready.value = true;
    }
  });
});
</script>

<template>
  <v-virtual-scroll heights="400" :items="pitchers">
    <v-container>
      <v-row>
        <v-col>
          <v-skeleton-loader
            type="table-thead"
            v-show="!ready"
          ></v-skeleton-loader>
          <v-skeleton-loader
            type="table-tbody"
            v-show="!ready"
          ></v-skeleton-loader>
          <CareerTable :stats="career['stats']" v-show="ready" />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <SeasonTable :info="season" v-show="ready" />
        </v-col>
      </v-row>
    </v-container>
  </v-virtual-scroll>
</template>

<style scoped></style>
