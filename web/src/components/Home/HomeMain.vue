<template>
  <el-container class="home-main" direction="vertical">
    <header class="header">
      <div class="search">
        <el-input placeholder="请输入内容" v-model="input" clearable class="input"></el-input>
        <el-button type="primary" icon="el-icon-search">搜索</el-button>
        <!-- <el-button icon="el-icon-search" circle class="search-btn"></el-button> -->
      </div>
      <div class="more">《更多》</div>
    </header>

    <el-main class="main">
      <div class="sort">
        <ul>
          <li>
            <span>评分最高</span>
            <i class="el-icon-caret-bottom"></i>
            <!-- <i class="el-icon-caret-top"></i> -->
          </li>
          <li>
            <span>标签数量</span>
            <i class="el-icon-caret-bottom"></i>
            <!-- <i class="el-icon-caret-top"></i> -->
          </li>
          <li>
            <span>上传时间</span>
            <i class="el-icon-caret-bottom"></i>
            <!-- <i class="el-icon-caret-top"></i> -->
          </li>
        </ul>
      </div>

      <ul class="card-list">
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
          <div class="confirm">已读</div>
        </li>
      </ul>
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
  </el-container>
</template>

<script>
export default {
  name: 'HomeMain',
  data() {
    return {
      input: '',
    };
  },
  methods: {
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
    },
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
    },
  },
};
</script>

<style lang="less" scoped>
.home-main {
  width: 100%;
  height: 100vh;
  .header {
    .search {
      width: 50vw;
      display: flex;
      margin: 0 auto;
      margin-top: 3vh;
      .input {
      }
    }
    .more {
      // margin: 0 auto;
      text-align: center;
      margin: 15px 0;
    }
  }
  .main {
    padding: 0;
    display: flex;
    flex-direction: column;
    .sort {
      margin-bottom: 10px;
      border: 1px solid #000;
      ul {
        display: flex;
        li {
          padding: 5px 5px;
          border-right: 1px solid #000;

          &:hover {
            color: red;
            cursor: pointer;
          }
        }
      }
    }
    .card-list {
      width: 100%;
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: space-around;
      .card {
        width: 150px;
        background-color: aquamarine;
        position: relative;
        // display: flex;
        // flex-direction: column;
        // justify-content: space-between;
        .card-top {
          img {
            width: 100%;
            padding-top: 100%;
            background-color: red;
            display: block;
            margin: 0 auto;
          }
        }
        .card-bottom {
          background-color: blueviolet;
        }
        .confirm {
          background-color: aqua;
          padding: 15px 10px;
          border-radius: 50%;
          position: absolute;
          top: 0;
          right: 0;
          transform: translate(50%, -50%);
        }
      }
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
}
</style>
