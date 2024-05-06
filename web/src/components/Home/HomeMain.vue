<template>
  <el-container class="home-main" direction="vertical">
    <header class="header">
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
		<!-- <el-col :span="14"> -->

		<!-- </el-col> -->
	</div>
    </header>
	


    <el-main class="main">
    <!-- <div class="sort">
        <ul>
          <li>
            <span>评分最高</span>
            <i class="el-icon-caret-bottom"></i>
            
          </li>
          <li>
            <span>标签数量</span>
            <i class="el-icon-caret-bottom"></i>
            
          </li>
          <li>
            <span>上传时间</span>
            <i class="el-icon-caret-bottom"></i>
            
          </li>
        </ul>
      </div> -->
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

<!--      <ul class="card-list">
        <li class="card">
          <div class="card-top">
            <img src="" alt="" />
          </div>
          <div class="card-bottom">
            <p>标题:</p>
            <p>标签:</p>
            <p>上传时间:</p>
            <p>评分:</p>
          </div>
          
        </li>
      </ul> -->
		<!-- <el-row>
		<el-col :span="8" v-for="(o, index) in 2" :key="o" :offset="index > 0 ? 2 : 0"> -->
		<div class="card-item">
			<div class="confirm">已读</div>
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
		</div>
		
		<!-- </el-col>
		</el-row> -->
    </el-main>

    <footer class="footer">
      <div class="block">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :page-size="100"
          layout="prev, pager, next, jumper"
          :total="1000"></el-pagination>
      </div>
    </footer>
	
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
export default {
  name: 'HomeMain',
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
	.header {
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
	.card-item{
		width: 300px;
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
	}
	.footer {
		margin: 0 auto;
		margin-bottom: 5vh;
		// position: fixed;
		// bottom: 5vh;
		// left: 50%;
		// transform: translateX(-50%);
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

// 	.clearfix:before,
// 	.clearfix:after {
// 		display: table;
// 		content: "";
// 	}
// 	.clearfix:after {
// 		clear: both
// 	}
// .home-main {
//   width: 100%;
//   height: 100vh;

//   .main {
//     padding: 0;
//     display: flex;
//     flex-direction: column;
//     .sort {
//       margin-bottom: 10px;
//       border: 1px solid #000;
//       ul {
//         display: flex;
//         li {
//           padding: 5px 5px;
//           border-right: 1px solid #000;

//           &:hover {
//             color: red;
//             cursor: pointer;
//           }
//         }
//       }
//     }
//     .card-list {
//       width: 100%;
//       flex: 1;
//       display: flex;
//       align-items: center;
//       justify-content: space-around;
//       .card {
//         width: 150px;
//         background-color: aquamarine;
//         position: relative;
//         // display: flex;
//         // flex-direction: column;
//         // justify-content: space-between;
//         .card-top {
//           img {
//             width: 100%;
//             padding-top: 100%;
//             background-color: red;
//             display: block;
//             margin: 0 auto;
//           }
//         }
//         .card-bottom {
//           background-color: blueviolet;
//         }
//         .confirm {
//           background-color: aqua;
//           padding: 15px 10px;
//           border-radius: 50%;
//           position: absolute;
//           top: 0;
//           right: 0;
//           transform: translate(50%, -50%);
//         }
//       }
//     }
//   }

// }
</style>
