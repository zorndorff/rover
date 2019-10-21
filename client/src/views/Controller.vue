<template>
  <v-container>
    <v-layout row wrap>
      <v-flex md8>
        <Controls />
      </v-flex>
      <v-flex md4>
        <Telemetry />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Controls from '../components/Controls.vue';
import Telemetry from '../components/Telemetry.vue';

export default {
  components: {
    Controls,
    Telemetry,
  },
};
</script>
