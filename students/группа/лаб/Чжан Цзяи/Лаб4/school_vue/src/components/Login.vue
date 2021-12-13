<template>
  <div>
    <h1>Вход</h1>
    <input v-model="username" type="text" placeholder="Логин"/>
    <input v-model="password" type="password" placeholder="Пароль"/>
    <button @click="login()">Вход</button>
    <div>
      <router-link to="/register">Регистрация</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  mounted () {
    if (sessionStorage.getItem('username') && sessionStorage.getItem('token')) {
      this.$router.push('/')
    }
  },
  methods: {
    login () {
      this.axios
        .post('http://127.0.0.1:8000/auth/token/login/', { username: this.username, password: this.password })
        .then(response => {
          sessionStorage.setItem('token',response.data.token)
          sessionStorage.setItem('username',this.username)
          this.$router.push('/')
        })
    }
  }
}
</script>

<style scoped>

</style>
