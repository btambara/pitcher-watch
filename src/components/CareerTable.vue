<script setup lang="ts">

type CareerStats = {
    stats: {
        gamesPlayed: number
        gamesStarted: number
        groundOuts: number
        airOuts: number
        runs: number
        doubles: number
        triples: number
        homeRuns: number
        strikeOuts: number
        baseOnBalls: number
        intentionalWalks: number
        hits: number
        hitByPitch: number
        avg: number
        atBats: number
        obp: number
        slg: number
        ops: number
        caughtStealing: number
        stolenBases: number
        stolenBasePercentage: number
        groundIntoDoublePlay: number
        numberOfPitches: number
        era: number
        inningsPitched: number
        wins: number
        losses: number
        saves: number
        saveOpportunities: number
        holds: number
        blownSaves: number
        earnedRuns: number
        whip: 1.00
        battersFaced: number
        outs: number
        gamesPitched: number
        completeGames: number
        shutouts: number
        strikes: number
        strikePercentage: number
        hitBatsmen: number
        balks: number
        wildPitches: number
        pickoffs: number
        totalBases: number
        groundOutsToAirouts: number
        winPercentage: number
        pitchesPerInning: number
        gamesFinished: number
        strikeoutWalkRatio: number
        strikeoutsPer9Inn: number
        walksPer9Inn: number
        hitsPer9Inn: number
        runsScoredPer9: number
        homeRunsPer9: number
        inheritedRunners: number
        inheritedRunnersScored: number
        catchersInterference: number
        sacBunts: number
        sacFlies: number
    }
}

const details = defineProps<CareerStats>();
</script>

<template>
        <v-container>
            <v-row>
                <v-col>           
                    <v-table>
                        <thead>
                            <tr>
                                <th class="text-center" v-for="key in Object.keys(details.stats)">
                                    <v-btn variant="plain">{{ key }}</v-btn>
                                </th>
                            </tr>
                        </thead>

                        <tbody>
                            <tr>
                                <td v-for="value in Object.values(details.stats)">{{ value }}</td>
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
