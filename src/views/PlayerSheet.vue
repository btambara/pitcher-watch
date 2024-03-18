<script setup lang="ts">
import PlayerDetails from "../components/PlayerDetails.vue";
import PlayerStats from "../components/PlayerStats.vue";
import PlayerPitches from "../components/PlayerPitches.vue";
import positions from "../assets/positions.json";

import { getTeamColors, getTeamLogo } from "../helpers";

type Pitcher = {
  fullName: string;
  primaryNumber: string;
  primaryPosition: string;
  currentTeamId: number;
  mlbId: number;
};

const tab = defineModel();
const pitcher = defineProps<Pitcher>();

function findAbbrev(code: string) {
  for (var position of positions) {
    if (position["code"] == code) {
      return position["abbrev"];
    }
  }

  return "UNKNOWN";
}

function getBackgroundColor(currentTeamId: number) {
  var teamColors = getTeamColors(currentTeamId);
  if (teamColors && "second" in teamColors) {
    return teamColors["second"];
  }

  return "primary";
}
</script>

<template>
  <v-container class="d-flex align-center justify-center">
    <v-sheet width="90%" color="rgb(0, 0, 0, 0.0)">
      <v-row>
        <v-col>
          <PlayerDetails
            class="ma-4"
            :full-name="pitcher.fullName"
            :primary-number="pitcher.primaryNumber"
            :primary-position="findAbbrev(pitcher.primaryPosition)"
            :logo="getTeamLogo(pitcher.currentTeamId)"
            :currentTeamId="pitcher.currentTeamId"
          />
        </v-col>
        <v-spacer class="d-none d-sm-flex"></v-spacer>
      </v-row>
      <v-row>
        <v-col>
          <v-card class="ml-4 mr-4 mb-4" rounded="lg">
            <v-tabs
              v-model="tab"
              fixed-tabs
              :bg-color="getBackgroundColor(pitcher.currentTeamId)"
            >
              <v-tab>Stats</v-tab>
              <v-tab>Pitches</v-tab>
            </v-tabs>

            <v-window v-model="tab">
              <v-window-item :key="0">
                <v-virtual-scroll height="400" :items="[pitcher]">
                  <PlayerStats :mlb-id="pitcher.mlbId" />
                </v-virtual-scroll>
              </v-window-item>

              <v-window-item :key="1">
                <v-virtual-scroll height="400" :items="[pitcher]">
                  <PlayerPitches
                    :mlb-id="pitcher.mlbId"
                    :current-team-id="pitcher.currentTeamId"
                  />
                </v-virtual-scroll>
              </v-window-item>
            </v-window>
          </v-card>
        </v-col>
      </v-row>
    </v-sheet>
  </v-container>
</template>

<style scoped>
v-table {
  text-align: center;
}
</style>
