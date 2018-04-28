<template>
  <div>
    <UploadButton></UploadButton>
    <FileList></FileList>
  </div>
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
