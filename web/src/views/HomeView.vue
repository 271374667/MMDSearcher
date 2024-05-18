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
</style>
