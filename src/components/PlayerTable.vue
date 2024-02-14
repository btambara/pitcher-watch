<script setup lang="ts">
import pitchTypes from "../assets/pitchTypes.json";

type Pitches = {
  year: number;
  types: {
    code: string;
    amount: number;
  }[];
};

const details = defineProps<Pitches>();

function findTooltip(code: string) {
  for (let i = 0; i < pitchTypes.length; i++) {
    if (pitchTypes[i].code === code) {
      return pitchTypes[i].description;
    }
  }

  return "UNKNOWN";
}
</script>

<template>
  <v-container>
    <v-row>
      <v-col>
        <div class="text-h5 text-center mt-2 bg-primary">
          {{ details.year }}
        </div>

        <v-table>
          <thead>
            <tr>
              <th
                class="text-center"
                v-for="pitch in details.types"
                :key="pitch.code"
              >
                <v-tooltip :text="findTooltip(pitch.code)" location="top">
                  <template v-slot:activator="{ props }">
                    <v-btn variant="plain" v-bind="props">{{
                      pitch.code
                    }}</v-btn>
                  </template>
                </v-tooltip>
              </th>
            </tr>
          </thead>

          <tbody>
            <tr>
              <td v-for="pitch in details.types">{{ pitch.amount }}</td>
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
