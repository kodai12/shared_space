<template>
  <div class="login-block">
    <form class="login__form" action="" method="POST">
      <label class="login__label--email" for="loginEmail">E-mail: </label>
      <input id="loginEmail" class="login__input--email" type="email">
      <label class="login__label--password" for="loginPassword">Password: </label>
      <input id="loginPassword" class="login__input--password" type="password">
      <button class="login__button--submit" type="submit">Login</button>
    </form>
    <p>[[ message ]]</p>
  </div>
</template>

<style lang="scss" scoped>
.login-block {
  width: 1000px;
  margin: 0 auto;
}
.login__form {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
