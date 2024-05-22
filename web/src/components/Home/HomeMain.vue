<template>
	<el-container class="home-main">
		<el-header height="auto">
			<!-- 搜索框 -->
			<div class="search">
				<el-input v-model="searchInput" placeholder="请输入内容" @keydown.enter.native="searchRequest()"></el-input>
				<el-button type="primary" icon="el-icon-search" @click="searchRequest">搜索</el-button>

			</div>

			<!-- 更多弹出框 -->
			<div class="more">
				<el-popover
					placement="bottom"
					width="480"
					trigger="manual"
					v-model="visible">
					<span slot="reference" class="el-dropdown-link" @click="visible = !visible">
						更多
						<i class="el-icon-arrow-down el-icon--right"></i>
					</span>
					<div class="dropdown-item">
						级别：
						<!-- <el-checkbox-group v-model="searchRates">
							<el-checkbox-button v-for="(value,key) in rates" :label="key" :key="key">{{value}}</el-checkbox-button>
						</el-checkbox-group> -->
						<el-radio-group v-model="searchRates">
							<el-radio-button v-for="(value,key) in rates" :label="key" :key="key">{{value}}</el-radio-button>
						</el-radio-group>
					</div>
					<div class="dropdown-item">
						<div class="block">
							<span class="demonstration">时间：</span>
							<el-date-picker
								v-model="searchTime"
								type="daterange"
								range-separator="至"
								start-placeholder="开始日期"
								end-placeholder="结束日期">
							</el-date-picker>
						</div>
					</div>
				</el-popover>
				<!-- <el-dropdown trigger="click" placement="bottom">
					<span class="el-dropdown-link">
						更多
						<i class="el-icon-arrow-down el-icon--right"></i>
					</span> -->
					
					<!-- <el-dropdown-menu slot="dropdown">
						<div class="dropdown-item">
							级别：
							<el-checkbox-group v-model="ratesCheckbox">
								<el-checkbox-button v-for="rate in rates" :label="rate" :key="rate">{{rate}}</el-checkbox-button>
							</el-checkbox-group>
						</div>

						<div class="dropdown-item">
							<div class="block">
								<span class="demonstration">时间：</span>
								<el-date-picker v-model="value" type="date" placeholder="选择日期"></el-date-picker>
							</div>
						</div>
					</el-dropdown-menu> -->
				<!-- </el-dropdown> -->
			</div>
		</el-header>

		<el-main height="auto">
			<div class="radio">
				<el-radio-group v-model="radio">
					<el-radio-button label="1" v-show="radio!=1">
						评分
						<i class="el-icon-caret-bottom"></i>
					</el-radio-button>
					<el-radio-button label="2" v-show="radio!=2 && radio==1">
						评分
						<i class="el-icon-caret-top"></i>
					</el-radio-button>
					<el-radio-button label="3" v-show="radio!=3">
						标签数量
						<i class="el-icon-caret-bottom"></i>
					</el-radio-button>
					<el-radio-button label="4" v-show="radio!=4 && radio==3">
						标签数量
						<i class="el-icon-caret-top"></i>
					</el-radio-button>

					<el-radio-button label="5" v-show="radio!=5">
						上传时间
						<i class="el-icon-caret-bottom"></i>
					</el-radio-button>
					<el-radio-button label="6" v-show="radio!=6&&radio==5">
						上传时间
						<i class="el-icon-caret-top"></i>
					</el-radio-button>
				</el-radio-group>
			</div>

			<div class="home-card">
				<HomeCard 
					v-for="item in itemlist" 
					:key="item.id" 
					:index="item.id"
					:id="item.id"
					:author="item.author"
					:rating="item.rating"
					:score="item.score"
					:pic_url="item.pic_url"
					:status="!!item.status"
				></HomeCard>
			</div>
		</el-main>

		<el-footer height="auto">
			<div class="block">
				<!-- total总条目数/page-size每页显示个数=有几页 -->
				<el-pagination
					@size-change="handleSizeChange"
					@current-change="handleCurrentChange"
					:current-page.sync="currentPage"
					:page-size="18"
					layout="prev, pager, next, jumper"
					:total=total
					:pager-count="5"></el-pagination>
			</div>
		</el-footer>
	</el-container>
</template>

<script>
import HomeCard from '@/components/Home/HomeCard.vue';
import {getCardContent} from '@/apis/api.js';
export default {
	name: 'HomeMain',
	components: {
		HomeCard,
	},
	data() {
		return {
			// 必须：输入框需要v-model绑定的值
			searchInput: '',

			// 必须：分页默认值
			currentPage: 1,

			// 必须：时间选择器默认值
			searchTime: [undefined,undefined],

			// 必须：排序单选框默认值
			radio: 0,
			//itemlist
			itemlist:[],
			//后端item总数
			total:0,
			//级别列表
			rates:{"r13":"r13","Questionable":"r15","r18":"r18"},
			//已选级别
			searchRates:undefined,
			//展示更多
			visible:false
		};
	},
	methods: {
		// 必须：handleSizeChange	handleCurrentChange 分页触发的回调函数
		handleSizeChange(val) {
			console.log(`每页 ${val} 条`);
		},
		handleCurrentChange(val) {
			console.log(`当前页: ${val}`);
			getCardContent({page:val-1}).then(
			response=>{
				this.itemlist=response.data.data.mmd_list
			},
			error=>{
				console.log('请求失败了',error.message)
			})
		},
		// *********************************************************

		// reverseIcon() {
		// 	// console.log(this.$refs.radio);
		// 	console.log(123);
		// },
		searchRequest(){
			this.visible=false
			this.radio=0
			getCardContent({
				mmd_id:this.searchInput,
				post_time_search_begin:this.searchTime[0],
				post_time_search_end:this.searchTime[1],
				rating:this.searchRates}).then(
					response=>{
						this.itemlist=response.data.data.mmd_list
						this.total=response.data.data.total
					},
					error=>{
						console.log('请求失败了',error.message)
					}
				)
		}
	},
	mounted() {
		// 获取item
		getCardContent().then(
			response=>{
				console.log('请求成功了',response.data)
				this.itemlist=response.data.data.mmd_list
				this.total=response.data.data.total
			},
			error=>{
				console.log('请求失败了',error.message)
			}
		)
	},
	watch: {
		radio(newValue) {
			// console.log("111",newValue,oldValue)
			getCardContent({
				mmd_id:this.searchInput,
				post_time_search_begin:this.searchTime[0],
				post_time_search_end:this.searchTime[1],
				rating:this.searchRates,
				sort_by:newValue
				}).then(
					response=>{
						this.itemlist=response.data.data.mmd_list
						this.total=response.data.data.total
					},
					error=>{
						console.log('请求失败了',error.message)
					}
				)
		}
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

.dropdown-item{
	// 这一句放不到.el-header里面
		margin: 10px 20px;
		.el-checkbox-group{
			display: inline-block;
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
