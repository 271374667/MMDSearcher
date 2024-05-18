<template>
	<div class="card">
		<el-badge value="已读" type="primary">
			<el-card>
				<img
					src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
					class="image" />
				<div style="padding: 14px">
					<span>好吃的汉堡</span>
					<div>
						<div class="confirm">
							<span>作者:</span>
							<span>级别:</span>
							<span>评分:</span>
						</div>
					</div>
				</div>
			</el-card>
		</el-badge>
	</div>
</template>

<script></script>

<style lang="less">
.card {
	margin: 1.5rem;

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
