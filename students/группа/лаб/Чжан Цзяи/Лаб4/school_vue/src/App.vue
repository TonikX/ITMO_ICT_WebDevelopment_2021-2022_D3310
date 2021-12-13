<template>
  <v-app>
    <v-card
      class="mx-auto"
      height="300"
      width="1600"
    >
      <v-navigation-drawer
        absolute
        dark
        src="https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg"
        width="100%"
        permanent
      >
        <v-list>
          <v-list-item v-if="!isLogin" to="/login">Вход</v-list-item>
          <v-list-item v-if="!isLogin" to="/register">Регистрация</v-list-item>
          <v-list-item v-if="isLogin" to="/">Доклад</v-list-item>
          <v-list-item v-if="isLogin" to="/student">Студенты</v-list-item>
          <v-list-item v-if="isLogin" to="/schedule">Расписание</v-list-item>
          <v-list-item v-if="isLogin" to="/teacher">Приподаватель</v-list-item>
          <v-list-item v-if="isLogin" @click="logout()">Выход</v-list-item>
        </v-list>
      </v-navigation-drawer>
    </v-card>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  data () {
    return {
      isLogin: false
    }
  },
  mounted () {
    if (sessionStorage.getItem('token') && sessionStorage.getItem('username')) {
      this.isLogin = true
    }
    console.log(this.isLogin)
  },
  methods: {
    logout () {
      sessionStorage.clear()
      this.isLogin = false
      this.$router.push('/login')
    }
  }
}
</script>
