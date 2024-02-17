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
          <CareerTable
            :games-played="pitchers[0].careerStats.gamesPlayed"
            :games-started="pitchers[0].careerStats.gamesStarted"
            :ground-outs="pitchers[0].careerStats.groundOuts"
            :air-outs="pitchers[0].careerStats.airOuts"
            :runs="pitchers[0].careerStats.runs"
            :doubles="pitchers[0].careerStats.doubles"
            :triples="pitchers[0].careerStats.triples"
            :home-runs="pitchers[0].careerStats.homeRuns"
            :strike-outs="pitchers[0].careerStats.strikeOuts"
            :base-on-balls="pitchers[0].careerStats.baseOnBalls"
            :intentional-walks="pitchers[0].careerStats.intentionalWalks"
            :hits="pitchers[0].careerStats.hits"
            :hit-by-pitch="pitchers[0].careerStats.hitByPitch"
            :avg="pitchers[0].careerStats.avg"
            :at-bats="pitchers[0].careerStats.atBats"
            :obp="pitchers[0].careerStats.obp"
            :slg="pitchers[0].careerStats.slg"
            :ops="pitchers[0].careerStats.ops"
            :caught-stealing="pitchers[0].careerStats.caughtStealing"
            :stolen-bases="pitchers[0].careerStats.stolenBases"
            :stolen-base-percentage="
              pitchers[0].careerStats.stolenBasePercentage
            "
            :ground-into-double-play="
              pitchers[0].careerStats.groundIntoDoublePlay
            "
            :number-of-pitches="pitchers[0].careerStats.numberOfPitches"
            :era="pitchers[0].careerStats.era"
            :innings-pitched="pitchers[0].careerStats.inningsPitched"
            :wins="pitchers[0].careerStats.wins"
            :losses="pitchers[0].careerStats.losses"
            :saves="pitchers[0].careerStats.saves"
            :save-opportunities="pitchers[0].careerStats.saveOpportunities"
            :holds="pitchers[0].careerStats.holds"
            :blown-saves="pitchers[0].careerStats.blownSaves"
            :earned-runs="pitchers[0].careerStats.earnedRuns"
            :whip="pitchers[0].careerStats.whip"
            :batters-faced="pitchers[0].careerStats.battersFaced"
            :outs="pitchers[0].careerStats.outs"
            :games-pitched="pitchers[0].careerStats.gamesPitched"
            :complete-games="pitchers[0].careerStats.completeGames"
            :shutouts="pitchers[0].careerStats.shutouts"
            :strikes="pitchers[0].careerStats.strikes"
            :strike-percentage="pitchers[0].careerStats.strikePercentage"
            :hit-batsmen="pitchers[0].careerStats.hitBatsmen"
            :balks="pitchers[0].careerStats.balks"
            :wild-pitches="pitchers[0].careerStats.wildPitches"
            :pickoffs="pitchers[0].careerStats.pickoffs"
            :total-bases="pitchers[0].careerStats.totalBases"
            :ground-outs-to-airouts="
              pitchers[0].careerStats.groundOutsToAirouts
            "
            :win-percentage="pitchers[0].careerStats.winPercentage"
            :pitches-per-inning="pitchers[0].careerStats.pitchesPerInning"
            :games-finished="pitchers[0].careerStats.gamesFinished"
            :strikeout-walk-ratio="pitchers[0].careerStats.strikeoutWalkRatio"
            :strikeouts-per9-inn="pitchers[0].careerStats.strikeoutsPer9Inn"
            :walks-per9-inn="pitchers[0].careerStats.walksPer9Inn"
            :hits-per9-inn="pitchers[0].careerStats.hitsPer9Inn"
            :runs-scored-per9="pitchers[0].careerStats.runsScoredPer9"
            :home-runs-per9="pitchers[0].careerStats.homeRunsPer9"
            :inherited-runners="pitchers[0].careerStats.inheritedRunners"
            :inherited-runners-scored="
              pitchers[0].careerStats.inheritedRunnersScored
            "
            :catchers-interference="
              pitchers[0].careerStats.catchersInterference
            "
            :sac-bunts="pitchers[0].careerStats.sacBunts"
            :sac-flies="pitchers[0].careerStats.sacFlies"
          />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <SeasonTable :info="pitchers[0].yearByYear" />
        </v-col>
      </v-row>
    </v-container>
  </v-virtual-scroll>
</template>

<style scoped></style>
