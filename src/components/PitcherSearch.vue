<script setup lang="ts">
import PlayerSheet from "./PlayerSheet.vue";
import { ref } from "vue";
const pitchers = defineModel();
const pitcherDialog = ref(false);
const selectedPitcher = ref();

fetch("http://localhost/api/v1/players/?position=1&skip=0").then(
  async (response) => {
    const isJson = response.headers
      .get("content-type")
      ?.includes("application/json");
    const data = isJson && (await response.json());
    let itemPlayers: any = [];
    for (var player of data) {
      itemPlayers.push({
        title: player["full_name"] + " | " + player["primary_number"],
        value: player,
      });
    }
    pitchers.value = itemPlayers;
  },
);

function handler(pitcher: any) {
  if (pitcher) {
    selectedPitcher.value = pitcher;
    pitcherDialog.value = true;
  }
}
</script>

<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="7" md="5" lg="5" xl="5">
        <v-autocomplete
          :items="pitchers"
          append-inner-icon="fas fa-magnifying-glass"
          auto-select-first
          class="flex-full-width"
          density="comfortable"
          item-props
          menu-icon=""
          placeholder="Search pitcher by full name"
          prepend-inner-icon="fas fa-baseball"
          rounded
          theme="light"
          variant="solo"
          no-data-text="No searchable pitchers."
          v-on:update:modelValue="handler"
        ></v-autocomplete>
      </v-col>
    </v-row>
    <v-dialog
      scrollable
      transition="dialog-bottom-transition"
      v-model="pitcherDialog"
    >
      <v-card color="rgb(0, 0, 0, 0.0)" border="false" elevation="0">
        <v-btn
          position="fixed"
          icon="fas fa-xmark"
          @click="pitcherDialog = false"
        ></v-btn>
        <PlayerSheet
          :full-name="selectedPitcher['full_name']"
          :primary-number="selectedPitcher['primary_number']"
          :primary-position="selectedPitcher['primary_position_code']"
        />
      </v-card>
    </v-dialog>
  </v-container>
</template>

<style scoped></style>
