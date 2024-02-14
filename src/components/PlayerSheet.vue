<script setup lang="ts">
import PlayerDetails from "./PlayerDetails.vue";
import PlayerStats from "./PlayerStats.vue";
import PlayerArsenal from "./PlayerArsenal.vue";
import pitchers from "../assets/pitchers.json";
import DodgerLogo from "../assets/logos/los-angeles-dodgers-logo.svg";

const tab = defineModel();
</script>

<template>
  <v-container class="d-flex align-center justify-center">
    <v-sheet width="90%" color="rgb(0, 0, 0, 0.0)">
      <v-row>
        <v-col>
          <PlayerDetails
            class="ma-4"
            full-name="Clayton Kershaw"
            primary-number="22"
            primary-position="P"
            :logo="DodgerLogo"
          />
        </v-col>
        <v-spacer class="d-none d-sm-flex"></v-spacer>
      </v-row>
      <v-row>
        <v-col>
          <v-card class="ml-4 mr-4 mb-4" rounded="lg">
            <v-tabs v-model="tab" fixed-tabs bg-color="primary">
              <v-tab>Stats</v-tab>
              <v-tab>Arsenal</v-tab>
            </v-tabs>

            <v-window v-model="tab">
              <v-window-item :key="0">
                <v-virtual-scroll height="400" :items="pitchers">
                  <PlayerStats />
                </v-virtual-scroll>
              </v-window-item>

              <v-window-item :key="1">
                <v-virtual-scroll
                  height="400"
                  :items="pitchers[0].pitchingTypes"
                >
                  <template v-slot:default="{ item }">
                    <PlayerArsenal :year="item.year" :types="item.types" />
                  </template>
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
