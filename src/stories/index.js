import { storiesOf } from '@storybook/vue'

import LoginForm from '../components/LoginForm.vue'

storiesOf('LoginForm', module).add('simple', () => ({
  components: { LoginForm },
  template: `<LoginForm></LoginForm>`
}));
