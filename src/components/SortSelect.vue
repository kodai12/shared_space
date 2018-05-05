<template>
  <el-select
    v-model="selectedValue"
    default-first-option
    placeholder="Sort By Author"
    @change="changeFileListByAuthor">
    <el-option
      v-for="option in options"
      :key="option.name"
      :label="option.name"
      :value="option.name">
    </el-option>
  </el-select>
</template>

<script>
import axios from 'axios';
import { mapMutations } from 'vuex';

export default {
  data() {
    return {
      selectedValue: '',
      options: [],
    };
  },
  mounted() {
    this.fetchAllUser();
  },
  methods: {
    ...mapMutations([
      'sortByAuthor',
    ]),
    fetchAllUser() {
      const url = './api/users';
      axios.get(url).then((res) => {
        this.options = res.data;
        this.options.unshift({'name': 'all'}); // optionの先頭にallを追加
      }).catch((err) => {
        /* eslint-disable no-console */
        console.log(err.message);
      });
    },
    changeFileListByAuthor(value) {
      this.selectedValue = value;
      this.sortByAuthor({ selectedAuthor: value });
    }
  },
};
</script>

<style lang="scss" scoped>
</style>
