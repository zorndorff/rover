<template>
  <v-list two-line>
    <v-list-tile
      v-for="(item) in items"
      :key="item.id"
      avatar
    >
    <v-list-tile-avatar>
      <v-icon>fa-robot</v-icon>
    </v-list-tile-avatar>

    <v-list-tile-content>
      <v-list-tile-title v-html="item.title"></v-list-tile-title>
      <v-list-tile-sub-title v-html="item.subtitle"></v-list-tile-sub-title>
    </v-list-tile-content>
            </v-list-tile>
  </v-list>
</template>

<script>
export default {
  data: () => ({
    data: [{
      id: 'motor_1_throttle',
      title: 'Motor 1 Throttle',
    },
    {
      id: 'motor_2_throttle',
      title: 'Motor 2 Throttle',
    },
    {
      id: 'motor_3_throttle',
      title: 'Motor 3 Throttle',
    }],
  }),
};
</script>
