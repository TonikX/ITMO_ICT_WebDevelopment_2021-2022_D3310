<template>
  <v-app>
    <v-app-bar
      app
      light
      shaped
      color="green"
      elevation="4"
      src="https://picsum.photos/1920/1080?random">
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top left, rgba(255,235,231,.5), rgba(206,239,228,1)"
        ></v-img>
      </template>

      <v-app-bar-nav-icon></v-app-bar-nav-icon>
      <v-toolbar-title>welcome to our POULTRY FARM!</v-toolbar-title>

    <v-spacer></v-spacer>

    <v-btn>
      <router-link to="/signin">Sign In</router-link>
      <v-icon
        color="pink">mdi-account
      </v-icon>
    </v-btn>

    <v-btn>
      <router-link to="/signup">Sign Up</router-link>
      <v-icon
        color="pink">mdi-account
      </v-icon>
    </v-btn>

    <v-btn>
      <router-link to="/chickenslist">Chickens</router-link>
      <v-icon
        color="blue">mdi-bird
      </v-icon>
    </v-btn>

    <v-btn>
      <router-link to="/breedslist">Breeds</router-link>
      <v-icon
        color="red">mdi-eye
      </v-icon>
    </v-btn>

    <v-btn>
      <router-link to="/cellslist">Cells</router-link>
      <v-icon
        color="red">mdi-home
      </v-icon>
    </v-btn>

    <v-btn>
      <router-link to="/settings">Settings</router-link>
      <v-icon
        color="grey">mdi-wrench
      </v-icon>
    </v-btn>
    <template v-slot:extension>
        <v-tabs align-with-title>
          <v-tab>Tab 1</v-tab>
          <v-tab>Tab 2</v-tab>
          <v-tab>Tab 3</v-tab>
        </v-tabs>
    </template>
    </v-app-bar>

    <v-main class="my-5 px-5">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'App',
  components: {},

  created () {
    if (localStorage.getItem('token')) {
      $.ajaxSetup({
        headers: {
          Authorization: 'Token' + localStorage.getItem('token')
        }
      })
    }
  }
}
</script>
