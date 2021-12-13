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
      v-model="score_math"
      :counter="10"
      label="Баллы матиматики"
      ></v-text-field>
      <v-text-field
      v-model="score_chemical"
      :counter="10"
      label="Баллы химии"
      ></v-text-field>
      <v-text-field
      v-model="score_english"
      :counter="10"
      label="Баллы англиского"
      ></v-text-field>
      <v-text-field
      v-model="score_computer"
      :counter="10"
      label="Баллы компьютера"
      ></v-text-field>
      <v-text-field
      v-model="semester"
      :counter="2"
      label="Семестер"
      ></v-text-field>
      <v-select
      v-model="sex"
      :items="sexes"
      label="Пол"
      required
      ></v-select>
      <v-select
      v-model="group"
      :items="groups"
      label="Группа"
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
    <div v-for="student in students" :key="student.id">
      <div class="shades black text-center">
        <span class="white--text">first name: {{ student.first_name }}</span>
      </div>
      <div class="shades black text-center">
        <span class="white--text">last name: {{ student.last_name }}</span>
      </div>
      <div class="shades black text-center">
        <span class="white--text">score math: {{ student.score_math }}</span>
      </div>
      <div class="shades black text-center">
        <span class="white--text">score chemical: {{ student.score_chemical }}</span>
      </div>
      <div class="shades black text-center">
        <span class="white--text">score english: {{ student.score_english }}</span>
      </div>
      <div class="shades black text-center">
        <span class="white--text">score computer: {{ student.score_computer }}</span>
      </div>
      <div class="shades black text-center">
        <span class="white--text">semester: {{ student.semester }}</span>
      </div>
      <div class="shades black text-center">
        <span class="white--text">group: {{ student.group }}</span>
      </div>
      <v-btn
        color="error"
      class="mr-4"
      @click="deleteStudent(student.id)"
      >
      Удалить
      </v-btn>
      <v-form @submit="update(student.id)">
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
        v-model="score_math"
        :counter="10"
        label="Баллы матиматики"
        ></v-text-field>
        <v-text-field
        v-model="score_chemical"
        :counter="10"
        label="Баллы химии"
        ></v-text-field>
        <v-text-field
        v-model="score_english"
        :counter="10"
        label="Баллы англиского"
        ></v-text-field>
        <v-text-field
        v-model="score_computer"
        :counter="10"
        label="Баллы компьютера"
        ></v-text-field>
        <v-text-field
        v-model="semester"
        :counter="2"
        label="Семестер"
        ></v-text-field>
        <v-select
        v-model="sex"
        :items="sexes"
        label="Пол"
        required
        ></v-select>
        <v-select
        v-model="group"
        :items="groups"
        label="Группа"
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
    </div>
  </div>
</template>

<script>
export default {
  name: 'Student',
  data () {
    return {
      students: {},
      first_name: '',
      last_name: '',
      group: null,
      groups: [{ text: 'Выберите группу', value: null, disabled: true }],
      sex: null,
      semester: null,
      score_math: null,
      score_english: null,
      score_computer: null,
      score_chemical: null,
      sexes: [
        { text: 'Мужчина', value: 'm' },
        { text: 'Женщина', value: 's' }
      ]
    }
  },
  methods: {
    submit () {
      const data = {
        first_name: this.first_name,
        last_name: this.last_name,
        group: this.group,
        sex: this.sex,
        semester: this.semester,
        score_math: this.score_math,
        score_english: this.score_english,
        score_computer: this.score_computer
      }
      this.axios
        .post('http://127.0.0.1:8000/api/students/new', data)
        .then(response => { console.log(response); this.reset() })
        .catch(err => { console.log(err) })
    },
    update (id) {
      const data = {
        first_name: this.first_name,
        last_name: this.last_name,
        group: this.group,
        sex: this.sex,
        semester: this.semester,
        score_math: this.score_math,
        score_english: this.score_english,
        score_computer: this.score_computer
      }
      this.axios
        .patch('http://127.0.0.1:8000/api/students/update/' + id, data)
        .then(response => { console.log(response); this.reset() })
        .catch(err => { console.log(err) })
    },
    deleteStudent (id) {
      const url = 'http://127.0.0.1:8000/api/students/delete/' + id
      this.axios
        .delete(url)
        .then(response => { console.log(response) })
    },
    reset () {
      this.sex = null
      this.group = null
      this.semester = null
      this.score_math = null
      this.score_english = null
      this.score_computer = null
      this.last_name = ''
      this.first_name = ''
    },
    showGroups (groups) {
      for (let i = 0; i < groups.length; i++) {
        const group = {}
        group.value = groups[i].id
        group.text = groups[i].number

        this.groups.push(group)
      }
    },
    showStudents (data) {
      this.students = []
      for (let i = 0; i < data.length; i++) {
        const student = {}
        student.id = data[i].id
        student.first_name = data[i].first_name
        student.last_name = data[i].last_name
        student.sex = data[i].sex
        student.score_math = data[i].score_math
        student.score_chemical = data[i].score_chemical
        student.score_english = data[i].score_english
        student.score_computer = data[i].score_computer
        student.semester = data[i].semester
        student.group = data[i].group
        console.log(student)
        this.students.push(student)
      }
    }
  },
  mounted () {
    this.axios
      .get('http://127.0.0.1:8000/api/groups/list')
      .then(response => {
        console.log(response); this.showGroups(response.data)
      })
      .catch(err => { console.log(err) })
    this.axios
      .get('http://127.0.0.1:8000/api/students/list')
      .then(response => {
        console.log(response); this.showStudents(response.data)
      })
      .catch(err => { console.error(err) })
  }
}
</script>

<style scoped>

</style>
