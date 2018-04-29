<template>
  <article class="main-article">
    <UploadButton></UploadButton>
    <FileList></FileList>
  </article>
</template>

<script>
import UploadButton from '@/components/UploadButton';
import FileList from '@/components/FileList';

export default {
  components: {
    UploadButton,
    FileList
  }
};
</script>

<style lang="scss" scoped>
.main-article {
  padding: 30px 50px 0;
  text-align: center;
}
</style>
