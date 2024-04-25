<template>
  <div class="home-view">
    <HomeMain></HomeMain>
  </div>
</template>

<script>
import HomeMain from '@/components/Home/HomeMain.vue';
export default {
  name: 'HomeView',
  components: {
    HomeMain,
  },
};
</script>

<style lang="less" scoped></style>
