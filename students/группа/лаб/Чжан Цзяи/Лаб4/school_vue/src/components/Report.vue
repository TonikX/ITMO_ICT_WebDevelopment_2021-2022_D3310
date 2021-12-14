<template>
  <div>
    <div v-for="id in groups" :key="id">
      <v-btn
      color="error"
      class="mr-4"
      @click="getReport(id)"
      >
      искать доклад группы {{ id }}
      </v-btn>
    </div>
    <div class="blue darken-4">
      <span class="white--text">Средний балл: {{ report.Средний_балл }}</span>
    </div>
    <div class="amber darken-4">
      <span class="white--text">Обшие люди: {{ report.Обшие_люди }}</span>
    </div>
    <div class="shades black">
      <span class="white--text">руководитель: {{ report.руководитель }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Report',
  data () {
    return {
      report: {},
      groups: [1, 2]
    }
  },
  methods: {
    showReport (data) {
      this.report = {}
      const rep = {}
      rep.Средний_балл = data.Средний_балл
      rep.Обшие_люди = data.Обшие_люди
      rep.руководитель = data.руководитель
      console.log(rep)
      this.report = rep
    },
    getReport (id) {
      const url = 'http://127.0.0.1:8000/api/report/' + id
      this.axios
        .get(url)
        .then(response => { console.log(response); this.showReport(response.data) })
        .catch(err => { console.error(err) })
    }
  }
}
</script>

<style scoped>

</style>

