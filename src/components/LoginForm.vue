<template>
  <el-form
    :model="loginForm"
    :rules="loginRules"
    ref="loginForm">
    <el-form-item
      label="email"
      prop="email">
      <el-input
        v-model="loginForm.email">
      </el-input>
    </el-form-item>
    <el-form-item
      label="password"
      prop="password">
      <el-input
        v-model="loginForm.password">
      </el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm('ruleForm')">Create</el-button>
      <el-button @click="resetForm('ruleForm')">Reset</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  data() {
    return {
      loginForm: {
        email: '',
        password: ''
      },
      loginRules: {
        email: [
          {
            required: true,
            message: 'Please input email',
            trigger: 'blur'
          },{
            type: 'email',
            message: 'Please input a valid email address',
            trigger: 'blur'
          }
        ],
        password: [
          {
            required: true,
            message: 'Please input password',
            trigger: 'change'
          },{
            min: 6,
            message: 'Password is too short',
            trigger: 'change'
          }
        ]
      }
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!');
        } else {
          /* eslint-disable no-console */
          console.log('error submit!!');
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
  }
};
</script>

<style lang="scss" scoped>
</style>
