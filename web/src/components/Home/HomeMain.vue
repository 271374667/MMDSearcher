<template>
  <el-container class="home-main" direction="vertical">
    <el-header height="auto">
		<div class="search">
			<el-input placeholder="请输入内容" v-model="input" clearable class="input"></el-input>
			<el-button type="primary" icon="el-icon-search">搜索</el-button>
			<!-- <el-button icon="el-icon-search" circle class="search-btn"></el-button> -->
		</div>
		<div class="more"><!-- 《更多》 -->
			<el-dropdown trigger="click" placement="bottom">
				<span class="el-dropdown-link">
					更多<i class="el-icon-arrow-down el-icon--right"></i>
				</span>
				<el-dropdown-menu slot="dropdown">
					<div class="dropdown-item">
						级别：
						<el-tag style="margin: 0 5px;">欧美</el-tag>
						<el-tag style="margin: 0 5px;" type="success">日韩</el-tag>
						<el-tag style="margin: 0 5px;" type="info">台湾</el-tag>
						<el-tag style="margin: 0 5px;" type="warning">自拍</el-tag>
						<el-tag style="margin: 0 5px;" type="danger">三级片</el-tag>
					</div>
					<div class="dropdown-item">
						时间：
						<el-date-picker
							v-model="value1"
							type="date"
							placeholder="选择日期">
						</el-date-picker>
					</div>
				</el-dropdown-menu>
			</el-dropdown>
		</div>
		<div>
			<el-radio-group v-model="radio">
				<el-radio-button label="评分最高" >评分最高
					<i class="el-icon-caret-bottom" v-if="radio=='评分最高'"></i>
				</el-radio-button>
				<el-radio-button label="标签数量">标签数量
					<i class="el-icon-caret-bottom" v-if="radio=='标签数量'"></i>
				</el-radio-button>
				<el-radio-button label="上传时间">上传时间
					<i class="el-icon-caret-bottom" v-if="radio=='上传时间'"></i>
				</el-radio-button>
			</el-radio-group>
		</div>
    </el-header>
	
    <el-main>
		<HomeCard class="item" v-for="i in 10" :key="i"></HomeCard>
    </el-main>

    <el-footer>
      <div class="block">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :page-size="100"
          layout="prev, pager, next, jumper"
          :total="1000"></el-pagination>
      </div>
    </el-footer>
	
	<div class="drawer" :style="{ transform: isOpen ? 'translateX(0)' : 'translateX(-90%)' }">
		<div class="drawer_main">
			<el-tag style="margin: 0 5px;">欧美</el-tag>
			<el-tag style="margin: 0 5px;" type="success">日韩</el-tag>
			<el-tag style="margin: 0 5px;" type="info">台湾</el-tag>
			<el-tag style="margin: 0 5px;" type="warning">自拍</el-tag>
			<el-tag style="margin: 0 5px;" type="danger">三级片</el-tag>
		</div>
		<div class="drawer_btn_box">
			<el-button icon="el-icon-arrow-right" style="border-radius: 0% 50% 50% 0%; background-color:#ecf5ff ;" @click="toggleDrawer"></el-button>
		</div>
		
	</div>
<!-- <el-button @click="drawer = true" type="primary" style="margin-left: 16px;">
点我打开
</el-button>
<el-drawer
title="我是标题"
:visible.sync="drawer"
:direction="direction"
:before-close="handleClose">
<span>我来啦!</span>
</el-drawer> -->
  </el-container>
</template>

<script>
	import HomeCard from "@/components/Home/HomeCard.vue"
export default {
  name: 'HomeMain',
  components:{HomeCard},
  data() {
    return {
      input: '',
		radio:"评分最高",
		isOpen:false,
    };
  },
  methods: {
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
    },
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
    },
	toggleDrawer() {
		this.isOpen = !this.isOpen;
	},
  },
};
</script>

<style lang="less" scoped>
	*{
		box-sizing: border-box;
	}
	.el-header {
		
		.search {
			width: 50vw;
			display: flex;
			margin: 0 auto;
			margin-top: 3vh;
		}
		.more {
			text-align: center;
			margin: 15px 0;
		}
		
	}
	.dropdown-item{
		margin: 10px 20px;
	}
	
	.el-main{
		.item{
			margin: 10px 20px;
		}
	}
	
	.el-footer {
		margin: 0 auto;
		margin-bottom: 5vh;
		.block {
		}
	}
	
	.drawer{
		width: 400px;
		height: 100%;
		position: absolute;
		left: 0;
		
		.drawer_btn_box{
			width: 10%;
			height: 100%;
			display: flex;
			justify-content: center;
			align-items: center;
			float: right;
		}
		.drawer_main{
			width: 90%;
			height: 100%;
			float: left;
			background-color: #ecf5ff;
			padding: 10px;
		}
	}
</style>
