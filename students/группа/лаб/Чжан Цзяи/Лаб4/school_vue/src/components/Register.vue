<template>
  <div>
    <h1>Регистрация</h1>
    <input v-model="username" type="text" placeholder="Логин"/>
    <input v-model="password" type="password" placeholder="Пароль"/>
    <button @click="register()">Регистрация</button>
    <div>
      <router-link to="/login">Вход</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Register',
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
    register () {
      this.axios
        .post('http://127.0.0.1:8000/auth/users/', { username: this.username, password: this.password })
        .then(reponse => {
          console.log(reponse.data)
          this.$router.push('/login')
        })
    }
  }
}
</script>

<style scoped>

</style>
