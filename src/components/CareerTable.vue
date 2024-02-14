<script setup lang="ts">
import pitchStats from "../assets/pitchStats.json";

type CareerStats = {
  stats: {
    gamesPlayed: number;
    gamesStarted: number;
    groundOuts: number;
    airOuts: number;
    runs: number;
    doubles: number;
    triples: number;
    homeRuns: number;
    strikeOuts: number;
    baseOnBalls: number;
    intentionalWalks: number;
    hits: number;
    hitByPitch: number;
    avg: number;
    atBats: number;
    obp: number;
    slg: number;
    ops: number;
    caughtStealing: number;
    stolenBases: number;
    stolenBasePercentage: number;
    groundIntoDoublePlay: number;
    numberOfPitches: number;
    era: number;
    inningsPitched: number;
    wins: number;
    losses: number;
    saves: number;
    saveOpportunities: number;
    holds: number;
    blownSaves: number;
    earnedRuns: number;
    whip: 1.0;
    battersFaced: number;
    outs: number;
    gamesPitched: number;
    completeGames: number;
    shutouts: number;
    strikes: number;
    strikePercentage: number;
    hitBatsmen: number;
    balks: number;
    wildPitches: number;
    pickoffs: number;
    totalBases: number;
    groundOutsToAirouts: number;
    winPercentage: number;
    pitchesPerInning: number;
    gamesFinished: number;
    strikeoutWalkRatio: number;
    strikeoutsPer9Inn: number;
    walksPer9Inn: number;
    hitsPer9Inn: number;
    runsScoredPer9: number;
    homeRunsPer9: number;
    inheritedRunners: number;
    inheritedRunnersScored: number;
    catchersInterference: number;
    sacBunts: number;
    sacFlies: number;
  };
};

const details = defineProps<CareerStats>();

function findLookupParam(name: string) {
  for (let i = 0; i < pitchStats.length; i++) {
    if (
      pitchStats[i].name.toLowerCase() === name.toLowerCase() ||
      pitchStats[i].lookupParam.toLowerCase() == name.toLowerCase()
    ) {
      if (pitchStats[i].lookupParam) return pitchStats[i].lookupParam;
      else return pitchStats[i].label;
    }
  }

  return "";
}

function findTooltip(name: string) {
  for (let i = 0; i < pitchStats.length; i++) {
    if (pitchStats[i].name.toLowerCase() === name.toLowerCase()) {
      return pitchStats[i].label;
    }
  }

  return "UNKNOWN";
}
</script>

<template>
  <v-container>
    <v-row>
      <v-col>
        <v-table>
          <thead>
            <tr>
              <th class="text-center">
                <v-btn variant="plain">Career</v-btn>
              </th>
              <th
                class="text-center"
                v-for="(key, index) in Object.keys(details.stats)"
                v-bind:key="index"
              >
                <v-tooltip :text="findTooltip(key)" location="top">
                  <template v-slot:activator="{ props }">
                    <v-btn variant="plain" v-bind="props">{{
                      findLookupParam(key)
                    }}</v-btn>
                  </template>
                </v-tooltip>
              </th>
            </tr>
          </thead>

          <tbody>
            <tr>
              <td></td>
              <td
                v-for="(value, index) in Object.values(details.stats)"
                v-bind:key="index"
              >
                {{ value }}
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
