<template>
  <div class="home-view">
    <HomeMain></HomeMain>
  </div>
</template>

<script>
import HomeMain from '@/components/Home/HomeMain.vue';
// import HomeHead from "@/components/Home/HomeHead.vue"
export default {
  name: 'HomeView',
  components: {
    HomeMain,
	// HomeHead,
  },
};
</script>

<style lang="less" scoped>
	.home-view{
		// width: 90%;
		width: 1702px;
		margin: 0 auto;
	}
</style>
