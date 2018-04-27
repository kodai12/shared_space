// https://eslint.org/docs/user-guide/configuring

module.exports = {
  root: true,
  parserOptions: {
    parser: 'babel-eslint'
  },
  env: {
    browser: true,
  },
  // https://github.com/vuejs/eslint-plugin-vue#priority-a-essential-error-prevention
  // consider switching to `plugin:vue/strongly-recommended` or `plugin:vue/recommended` for stricter rules.
  extends: [
    'eslint:recommended',
    'plugin:vue/essential'
  ],
  // required to lint *.vue files
  plugins: [
    'vue'
  ],
  // add your custom rules here
  rules: {
    // allow debugger during development
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,
    "arrow-body-style": 2,
    "arrow-parens": 2,
    "arrow-spacing": 2,
    "generator-star-spacing": 2,
    "no-duplicate-imports": 2,
    "no-useless-computed-key": 2,
    "no-useless-constructor": 2,
    "no-useless-rename": 2,
    "no-var": 2,
    "object-shorthand": 2,
    "prefer-arrow-callback": 2,
    "prefer-const": 2,
    "prefer-rest-params": 2,
    "prefer-spread": 2,
    "prefer-template": 2,
    "rest-spread-spacing": 2,
    "template-curly-spacing": 2,
    "yield-star-spacing": 2,
    "semi": [2, "always"],
    "semi-spacing": [2, {"after": true, "before": false}],
    "semi-style": [2, "last"],
    "no-extra-semi": 2,
    "no-unexpected-multiline": 2,
    "no-unreachable": 2,
    "quotes": [2, "single"]
  }
}
