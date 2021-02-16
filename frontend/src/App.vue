<template>
  <div id="app">
    <ImagesComponent />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import ImagesComponent from './components/ImagescoreComponent.vue';

@Component({
  components: {
    ImagesComponent
  },
})
export default class App extends Vue {}
</script>
<style scoped>
#app {
  text-align:center
}
</style>
