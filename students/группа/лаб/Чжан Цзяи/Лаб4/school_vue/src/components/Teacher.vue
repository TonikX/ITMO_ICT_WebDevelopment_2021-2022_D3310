<template>
  <div>
    <v-form @submit="submit()">
      <v-text-field
      v-model="first_name"
      :counter="10"
      label="Имя"
      required
      ></v-text-field>
      <v-text-field
      v-model="last_name"
      :counter="10"
      label="Фамиля"
      required
      ></v-text-field>
      <v-text-field
      v-model="b_date"
      :counter="10"
      label="Время начала"
      required
      ></v-text-field>
      <v-text-field
      v-model="e_date"
      :counter="10"
      label="Время закончила"
      required
      ></v-text-field>
      <v-text-field
      v-model="office"
      :counter="10"
      label="кабинет"
      ></v-text-field>
      <v-select
      v-model="subject"
      :items="subjects"
      label="Дисциплина"
      required
      ></v-select>
      <v-btn
        color="success"
        class="mr-4"
        type="submit"
      >
        Сохранить
      </v-btn>
      <v-btn
        color="error"
      class="mr-4"
      @click="reset"
      >
      Сбросить
      </v-btn>
    </v-form>
    <div v-for="teacher in teachers" :key="teacher.id">
      <div class="shades black text-center">
        <span class="white--text">first name: {{ teacher.first_name }}</span>
      </div>
      <div class="shades black text-center">
        <span class="white--text">last name: {{ teacher.last_name }}</span>
      </div>
      <div class="shades black text-center">
        <span class="white--text">b_date:  {{ teacher.b_date }}</span>
      </div>
      <div class="shades black text-center">
        <span class="white--text">e_date: {{ teacher.e_date }}</span>
      </div>
      <div class="shades black text-center">
        <span class="white--text">office: {{ teacher.office }}</span>
      </div>
      <div class="shades black text-center">
        <span class="white--text">subject: {{ teacher.subject }}</span>
      </div>
      <v-btn
        color="error"
      class="mr-4"
      @click="deleteTeacher(teacher.id)"
      >
      Удалить
      </v-btn>
      <div>
        <v-form @submit="update(teacher.id)">
          <v-text-field
          v-model="first_name"
          :counter="10"
          label="Имя"
          required
          ></v-text-field>
          <v-text-field
          v-model="last_name"
          :counter="10"
          label="Фамиля"
          required
          ></v-text-field>
          <v-text-field
          v-model="b_date"
          :counter="10"
          label="Время начала"
          required
          ></v-text-field>
          <v-text-field
          v-model="e_date"
          :counter="10"
          label="Время закончила"
          required
          ></v-text-field>
          <v-text-field
          v-model="office"
          :counter="10"
          label="кабинет"
          ></v-text-field>
          <v-select
          v-model="subject"
          :items="subjects"
          label="Дисциплина"
          required
          ></v-select>
          <v-btn
            color="success"
            class="mr-4"
            type="submit"
          >
            Обновить
          </v-btn>
          <v-btn
            color="error"
          class="mr-4"
          @click="reset"
          >
          Сбросить
          </v-btn>
        </v-form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Teacher',
  data () {
    return {
      teachers: {},
      first_name: '',
      last_name: '',
      b_date: '',
      e_date: '',
      office: null,
      subject: null,
      subjects: [
        { text: 'математика', value: 'm' },
        { text: 'химия', value: 'c' },
        { text: 'английский ', value: 'e' },
        { text: 'компьютерная наука', value: 'p' }
      ]
    }
  },
  methods: {
    submit () {
      window.event.preventDefault()
      const data = {
        first_name: this.first_name,
        last_name: this.last_name,
        b_date: this.b_date,
        e_date: this.e_date,
        subject: this.subject,
        office: this.office
      }
      this.axios
        .post('http://127.0.0.1:8000/api/teachers/new', data)
        .then(response => { console.log(response); this.reset() })
        .catch(err => { console.log(err) })
    },
    update (id) {
      const data = {
        first_name: this.first_name,
        last_name: this.last_name,
        b_date: this.b_date,
        e_date: this.e_date,
        subject: this.subject,
        office: this.office
      }
      this.axios
        .patch('http://127.0.0.1:8000/api/teachers/update/' + id, data)
        .then(response => { console.log(response); this.reset() })
        .catch(err => { console.log(err) })
    },
    deleteTeacher (id) {
      const url = 'http://127.0.0.1:8000/api/teachers/delete/' + id
      this.axios
        .delete(url)
        .then(response => { console.log(response) })
    },
    reset () {
      this.subject = null
      this.last_name = ''
      this.first_name = ''
      this.b_date = ''
      this.e_date = ''
      this.office = null
    },
    showTeachers (data) {
      this.teachers = []
      for (let i = 0; i < data.length; i++) {
        const teacher = {}
        teacher.id = data[i].id
        teacher.first_name = data[i].first_name
        teacher.last_name = data[i].last_name
        teacher.b_date = data[i].b_date
        teacher.e_date = data[i].e_date
        teacher.office = data[i].office
        teacher.subject = data[i].subject
        console.log(teacher)
        this.teachers.push(teacher)
      }
    }
  },
  mounted () {
    this.axios
      .get('http://127.0.0.1:8000/api/teachers/list')
      .then(response => {
        console.log(response); this.showTeachers(response.data)
      })
      .catch(err => { console.error(err) })
  }
}
</script>

<style scoped>

</style>
