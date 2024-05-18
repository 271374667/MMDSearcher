<template>
	<el-container class="home-main">
		<el-header height="auto">
			<!-- 搜索框 -->
			<div class="search">
				<el-input v-model="input" placeholder="请输入内容"></el-input>
				<el-button type="primary" icon="el-icon-search">搜索</el-button>
			</div>

			<!-- 更多弹出框 -->
			<div class="more">
				<el-dropdown trigger="click" placement="bottom">
					<span class="el-dropdown-link">
						更多
						<i class="el-icon-arrow-down el-icon--right"></i>
					</span>

					<el-dropdown-menu slot="dropdown">
						<div class="dropdown-item">
							级别：
							<el-button type="primary">梁畜</el-button>
							<el-button type="success">竣畜</el-button>
							<el-button type="warning ">浩畜</el-button>
							<el-button type="danger ">畜梁</el-button>
							<el-button type="info">畜竣</el-button>
						</div>

						<div class="dropdown-item">
							<div class="block">
								<span class="demonstration">时间：</span>
								<el-date-picker v-model="value" type="date" placeholder="选择日期"></el-date-picker>
							</div>
						</div>
					</el-dropdown-menu>
				</el-dropdown>
			</div>
		</el-header>

		<el-main height="auto">
			<div class="radio">
				<el-radio-group v-model="radio">
					<el-radio-button label="评分最高" ref="radio" @click="reverseIcon">
						评分最高
						<i class="el-icon-caret-bottom"></i>
					</el-radio-button>

					<el-radio-button label="标签数量" @click="reverseIcon">
						标签数量
						<i class="el-icon-caret-bottom"></i>
					</el-radio-button>

					<el-radio-button label="上传时间" @click="reverseIcon">
						上传时间
						<i class="el-icon-caret-bottom"></i>
					</el-radio-button>
				</el-radio-group>
			</div>

			<div class="home-card">
				<HomeCard v-for="item in 10" :key="item" :index="item"></HomeCard>
			</div>
		</el-main>

		<el-footer height="auto">
			<div class="block">
				<!-- total总条目数/page-size每页显示个数=有几页 -->
				<el-pagination
					@size-change="handleSizeChange"
					@current-change="handleCurrentChange"
					:current-page.sync="currentPage"
					:page-size="25"
					layout="prev, pager, next, jumper"
					:total="100"
					:pager-count="5"></el-pagination>
			</div>
		</el-footer>
	</el-container>
</template>

<script>
import HomeCard from '@/components/Home/HomeCard.vue';
export default {
	name: 'HomeMain',
	components: {
		HomeCard,
	},
	data() {
		return {
			// 必须：输入框需要v-model绑定的值
			input: '',

			// 必须：分页默认值
			currentPage: 1,

			// 必须：时间选择器默认值
			value: '',

			// 必须：单选框默认值
			radio: '评分最高',
		};
	},
	methods: {
		// 必须：handleSizeChange	handleCurrentChange 分页触发的回调函数
		handleSizeChange(val) {
			console.log(`每页 ${val} 条`);
		},
		handleCurrentChange(val) {
			console.log(`当前页: ${val}`);
		},
		// *********************************************************

		reverseIcon() {
			// console.log(this.$refs.radio);
			console.log(123);
		},
	},
};
</script>

<style lang="less" scoped>
.el-container {
	min-height: 100vh;
}

.el-header {
	display: flex;
	flex-direction: column;
	align-items: center;
	.search {
		width: 70vw;
		display: flex;
		margin-top: 3vh;
	}
}

.el-main {
	flex: 1;
	padding: 0;
	.radio {
		margin-top: 1vh;
		margin-bottom: 2vh;
	}
	.home-card {
		display: flex;
		flex-wrap: wrap;
		justify-content: space-evenly;
	}
}


.el-footer {
	display: flex;
	justify-content: center;
	margin-bottom: 3vh;
}
</style>
