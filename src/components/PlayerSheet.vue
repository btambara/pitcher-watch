<script setup lang="ts">
import PlayerDetails from "./PlayerDetails.vue";
import PlayerStats from "./PlayerStats.vue";
import PlayerPitches from "./PlayerPitches.vue";
import positions from "../assets/positions.json";

import AthleticsLogo from "../assets/logos/oakland-athletics-logo.svg";
import PiratesLogo from "../assets/logos/pittsburgh-pirates-logo.svg";
import PadresLogo from "../assets/logos/san-diego-padres-logo.svg";
import MarinersLogo from "../assets/logos/seattle-mariners-logo.svg";
import GiantsLogo from "../assets/logos/san-francisco-giants-logo.svg";
import CardinalsLogo from "../assets/logos/st.-louis-cardinals-logo.svg";
import RaysLogo from "../assets/logos/tampa-bay-rays-logo.svg";
import RangersLogo from "../assets/logos/texas-rangers-logo.svg";
import JaysLogo from "../assets/logos/toronto-blue-jays-logo.svg";
import TwinsLogo from "../assets/logos/minnesota-twins-logo.svg";
import PhilliesLogo from "../assets/logos/philadelphia-phillies-logo.svg";
import BravesLogo from "../assets/logos/atlanta-braves-logo.svg";
import RedSoxLogo from "../assets/logos/boston-red-sox-logo.svg";
import MarlinsLogo from "../assets/logos/miami-marlins-logo.svg";
import YankeesLogo from "../assets/logos/new-york-yankees-logo.svg";
import BrewersLogo from "../assets/logos/milwaukee-brewers-logo.svg";
import AngelsLogo from "../assets/logos/los-angeles-angels-logo.svg";
import DiamondbacksLogo from "../assets/logos/arizona-diamondbacks-logo.svg";
import OriolesLogo from "../assets/logos/baltimore-orioles-logo.svg";
import WhiteSoxLogo from "../assets/logos/chicago-white-sox-logo.svg";
import CubsLogo from "../assets/logos/chicago-cubs-logo.svg";
import RedsLogo from "../assets/logos/cincinnati-reds-logo.svg";
import GuardiansLogo from "../assets/logos/cleveland-indians-logo.svg";
import RockiesLogo from "../assets/logos/colorado-rockies-logo.svg";
import TigersLogo from "../assets/logos/detroit-tigers-logo.svg";
import AstrosLogo from "../assets/logos/houston-astros-logo.svg";
import RoyalsLogo from "../assets/logos/kansas-city-royals-logo.svg";
import DodgersLogo from "../assets/logos/los-angeles-dodgers-logo.svg";
import NationalsLogo from "../assets/logos/washington-nationals-logo.svg";
import MetsLogo from "../assets/logos/new-york-mets-logo.svg";

type Pitcher = {
  fullName: string;
  primaryNumber: string;
  primaryPosition: string;
  currentTeamId: string;
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

function findLogo(currentTeamId: number) {
  switch (currentTeamId) {
    case 133:
      return AthleticsLogo;
    case 134:
      return PiratesLogo;
    case 135:
      return PadresLogo;
    case 136:
      return MarinersLogo;
    case 137:
      return GiantsLogo;
    case 138:
      return CardinalsLogo;
    case 139:
      return RaysLogo;
    case 140:
      return RangersLogo;
    case 141:
      return JaysLogo;
    case 142:
      return TwinsLogo;
    case 143:
      return PhilliesLogo;
    case 144:
      return BravesLogo;
    case 145:
      return WhiteSoxLogo;
    case 146:
      return MarlinsLogo;
    case 147:
      return YankeesLogo;
    case 158:
      return BrewersLogo;
    case 108:
      return AngelsLogo;
    case 109:
      return DiamondbacksLogo;
    case 110:
      return OriolesLogo;
    case 111:
      return RedSoxLogo;
    case 112:
      return CubsLogo;
    case 113:
      return RedsLogo;
    case 114:
      return GuardiansLogo;
    case 115:
      return RockiesLogo;
    case 116:
      return TigersLogo;
    case 117:
      return AstrosLogo;
    case 118:
      return RoyalsLogo;
    case 119:
      return DodgersLogo;
    case 120:
      return NationalsLogo;
    case 121:
      return MetsLogo;
    default:
      return "";
  }
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
            :logo="findLogo(Number(pitcher.currentTeamId))"
          />
        </v-col>
        <v-spacer class="d-none d-sm-flex"></v-spacer>
      </v-row>
      <v-row>
        <v-col>
          <v-card class="ml-4 mr-4 mb-4" rounded="lg">
            <v-tabs v-model="tab" fixed-tabs bg-color="primary">
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
                  <PlayerPitches :mlb-id="pitcher.mlbId" />
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
