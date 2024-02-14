<script setup lang="ts">
type Player = {
    fullName: string;
    primaryNumber: string;
    primaryPosition: string;
    logo: string
}

const details = defineProps<Player>();
</script>

<template>
    <v-sheet rounded="xl" color="primary" elevation="12">
        <v-row align="center" justify="center">
            <v-col cols="12" align="center" justify="center">
                <v-avatar color="white" size="70">
                    <img :src="logo" height="90%"/>
                </v-avatar>
            </v-col>
            <v-col>
                <div class="text-h5 text-center">{{ details.fullName }}</div>
                <div class="text-h6 text-center">#{{ details.primaryNumber }} | {{ details.primaryPosition }}</div>
            </v-col>
        </v-row>
    </v-sheet>
</template>

<style scoped></style>
