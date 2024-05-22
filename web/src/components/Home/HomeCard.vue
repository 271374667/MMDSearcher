<template>
	<div class="card">
		<el-badge value="已读" type="primary" :hidden="status">
			<el-card>
				<img
					:src="pic_url"
					class="image" />
				<div style="padding: 14px">
					<span>id:{{id}}</span>
					<div>
						<div class="confirm">
							<span>作者:{{author}}</span>
							<span>级别:{{rating}}</span>
							<span>评分:{{score}}</span>
						</div>
					</div>
				</div>
			</el-card>
		</el-badge>
	</div>
</template>

<script>
	export default{
		name:'HomeCard',
		props:{
			id:Number,
			author:String,
			rating:String,
			score:Number,
			pic_url:String,
			status:Boolean
		}
	}
</script>

<style lang="less">
.card {
	margin: 1.5rem;
	img{
		width: 250px;
	}

	// 这个.el-card__body样式不准删！！！！！！！！
	.el-card__body {
		padding: 0;
	}

	.confirm {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		font-size: 1rem;
		color: #999;
	}
}
</style>
