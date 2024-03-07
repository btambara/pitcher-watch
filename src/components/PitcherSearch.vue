<script setup lang="ts">
import PlayerSheet from "./PlayerSheet.vue";
import pitchersJSON from "../assets/pitchers.json";
import { ref } from "vue";
const pitchers = defineModel();
const pitcherDialog = ref(false);
const selectedPitcher = ref();
const ready = ref(false);

fetch(`http://localhost/api/v1/players/?position=1&skip=0`)
  .then(async (response) => {
    const isJson = response.headers
      .get("content-type")
      ?.includes("application/json");
    const data = isJson && (await response.json());
    let itemPlayers: Array<{ title: string; value: object }> = [];
    for (var player of data) {
      itemPlayers.push({
        title: player["full_name"] + " | " + player["primary_number"],
        value: player,
      });
    }

    pitchers.value = itemPlayers;
    ready.value = true;
  })
  .catch(() => {
    let itemPlayers: Array<{ title: string; value: object }> = [];
    for (var player of pitchersJSON) {
      itemPlayers.push({
        title: player["full_name"] + " | " + player["primary_number"],
        value: player,
      });
    }
    pitchers.value = itemPlayers;
    ready.value = true;
  });

function handler(pitcher: object) {
  if (pitcher) {
    selectedPitcher.value = pitcher;
    pitcherDialog.value = true;
  }
}
</script>

<template>
  <v-container>
    <v-row justify="center" align-center>
      <v-col cols="12" sm="7" md="5" lg="5" xl="5">
        <v-progress-linear indeterminate v-show="!ready"></v-progress-linear>
        <div class="text-h3 mb-4" v-show="ready">Search</div>
        <v-autocomplete
          v-show="ready"
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
          :current-team-id="selectedPitcher['current_team_id']"
          :primary-number="selectedPitcher['primary_number']"
          :primary-position="selectedPitcher['primary_position_code']"
          :mlb-id="selectedPitcher['mlb_id']"
        />
      </v-card>
    </v-dialog>
  </v-container>
</template>

<style scoped></style>
