<script setup lang="ts">
import { getTeamColors } from "../helpers";
type Player = {
  fullName: string;
  primaryNumber: string;
  primaryPosition: string;
  logo: string;
  currentTeamId: number;
};

const details = defineProps<Player>();

function getBackgroundColor(currentTeamId: number) {
  var teamColors = getTeamColors(currentTeamId);
  if (teamColors && "first" in teamColors) {
    return teamColors["first"];
  }

  return "primary";
}

function getLogoBackgroundColor(currentTeamId: number) {
  var teamColors = getTeamColors(currentTeamId);
  if (teamColors && "third" in teamColors) {
    return teamColors["third"];
  }

  return "white";
}
</script>

<template>
  <v-sheet
    rounded="xl"
    :color="getBackgroundColor(details.currentTeamId)"
    elevation="12"
  >
    <v-row align="center" justify="center">
      <v-col cols="12" align="center" justify="center">
        <v-avatar
          :color="getLogoBackgroundColor(details.currentTeamId)"
          size="70"
        >
          <img :src="logo" height="60%" />
        </v-avatar>
      </v-col>
      <v-col>
        <div class="text-h5 text-center">{{ details.fullName }}</div>
        <div class="text-h6 text-center">
          #{{ details.primaryNumber }} | {{ details.primaryPosition }}
        </div>
      </v-col>
    </v-row>
  </v-sheet>
</template>

<style scoped></style>
../helpers
