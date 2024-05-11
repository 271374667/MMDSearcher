<template>
	<el-badge value="已读" class="item" type="primary">
		<!-- <div class="confirm">已读</div> -->
		<el-card :body-style="{ padding: '0px' }">
			<img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
			<div style="padding: 14px;">
				<span>好吃的汉堡</span>
				<div style="padding-top: 10px;">
					<i>作者:</i>
					<i>级别:</i>
					<i>评分:</i>
					<!-- <el-button type="text" class="button">操作按钮</el-button> -->
				</div>
			</div>
		</el-card>
	</el-badge>
</template>

<script>
</script>

<style lang="less" scoped>
	.confirm{
		width: 70px;
		height: 70px;
		border-radius: 50%;
		background-color: aqua;
		text-align: center;
		line-height: 70px;
		font-size: 18px;
		transform: translate(263px, 50%);
	}
	.image{
		width: 100%;
		display: block;
	}
	.button{
		padding: 0;
		float: right;
	}
	span{
		font-size: 22px;
		display: block;
	}
	i{
		font-size: 16px;
		display: block;
	}
</style>