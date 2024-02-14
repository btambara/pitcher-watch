<script setup lang="ts">
import CareerTable from "./CareerTable.vue";
import SeasonTable from "./SeasonTable.vue";
import pitchers from "../assets/pitchers.json";
</script>

<template>
  <v-virtual-scroll heights="400" :items="pitchers">
    <v-container>
      <v-row>
        <v-col>
          <CareerTable :stats="pitchers[0].careerStats" />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <SeasonTable :details="pitchers[0].yearByYear" />
        </v-col>
      </v-row>
    </v-container>
  </v-virtual-scroll>
</template>

<style scoped></style>
