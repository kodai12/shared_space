import { storiesOf } from '@storybook/vue'
import { LinksTo } from '@storybook/addon-links'
import { withKnobs, text, color } from '@storybook/addon-knobs'
import Centered from '@storybook/addon-centered'

import Header from '../components/Header.vue'
import LoginForm from '../components/LoginForm.vue'
import FileList from '../components/FileList.vue'
import UploadButton from '../components/UploadButton.vue'

storiesOf('Header', module)
  .addDecorator(Centered)
  .add('simple', () => ({
    components: { Header },
    template: `<Header></Header>`,
  }));

storiesOf('LoginForm', module)
  .addDecorator(Centered)
  .add('simple', () => ({
    components: { LoginForm },
    template: `<LoginForm></LoginForm>`,
  }));

storiesOf('FileList', module)
  .addDecorator(Centered)
  .add('simple', () => ({
    components: { FileList },
    template: `<FileList></FileList>`,
  }));

storiesOf('UploadButton', module)
  .addDecorator(Centered)
  .add('simple', () => ({
    components: { UploadButton },
    template: `<UploadButton></UploadButton>`,
  }));
