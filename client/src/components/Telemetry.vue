<template>
  <v-card>
    <v-list dense>
      <span v-bind="JSON.stringify(data)"></span>
      <v-list-item
        v-for="(item) in data"
        :key="item.id"
      >
        <v-list-item-content>
          <v-list-item-title v-html="item.title"></v-list-item-title>
        </v-list-item-content>
        <v-list-item-content class="align-end">{{ item.value }}</v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
  </template>

<script>
export default {
  data: () => ({
    data: [{
      id: 'motor_1_throttle',
      title: 'Motor 1 Throttle',
      value: 0,
    },
    {
      id: 'motor_2_throttle',
      title: 'Motor 2 Throttle',
      value: 0,
    },
    {
      id: 'motor_3_throttle',
      title: 'Motor 3 Throttle',
      value: 0,
    }],
  }),
};
</script>
