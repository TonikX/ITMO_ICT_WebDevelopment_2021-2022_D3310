<template>
  <div>
    <v-form @submit="submit()">
      <v-select
        v-model="teacher"
        :items="teachers"
        label="Приподаватель"
        required
      ></v-select>
      <v-select
        v-model="day"
        :items="days"
        label="День"
        required
      ></v-select>
      <v-select
        v-model="subject"
        :items="subjects"
        label="Дисциплина"
        required
      ></v-select>
      <v-select
        v-model="group"
        :items="groups"
        label="Группа"
        required
      ></v-select>
      <v-select
        v-model="classroom"
        :items="classrooms"
        label="Аудитория"
        required
      ></v-select>
      <v-text-field
      v-model="time"
      :counter="15"
      label="время"
      ></v-text-field>
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
    <div v-for="schedule in schedules" :key="schedule.id">
      <div class="shades black text-center">
        <span class="white--text">Time: {{ schedule.time }}</span>
      </div>
      <div class="shades black text-center">
        <span class="white--text">Day: {{ schedule.day }}</span>
      </div>
      <div class="shades black text-center">
        <span class="white--text">Subject: {{ schedule.subject }}</span>
      </div>
      <div class="shades black text-center">
        <span class="white--text">Group: {{ schedule.group }}</span>
      </div>
      <div class="shades black text-center">
        <span class="white--text">Teacher: {{ schedule.teacher }}</span>
      </div>
      <div class="shades black text-center">
        <span class="white--text">Classroom: {{ schedule.classroom }}</span>
      </div>
      <v-btn
        color="error"
      class="mr-4"
      @click="deleteSchedule(schedule.id)"
      >
      Удалить
      </v-btn>
      <v-form @submit="update(schedule.id)">
        <v-select
          v-model="teacher"
          :items="teachers"
          label="Приподаватель"
          required
        ></v-select>
        <v-select
          v-model="day"
          :items="days"
          label="День"
          required
        ></v-select>
        <v-select
          v-model="subject"
          :items="subjects"
          label="Дисциплина"
          required
        ></v-select>
        <v-select
          v-model="group"
          :items="groups"
          label="Группа"
          required
        ></v-select>
        <v-select
          v-model="classroom"
          :items="classrooms"
          label="Аудитория"
          required
        ></v-select>
        <v-text-field
        v-model="time"
        :counter="15"
        label="время"
        ></v-text-field>
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
  name: 'Schedule',
  props: {
    listData: {
      type: Array,
      required: true
    },
    size: {
      type: Number,
      required: false,
      default: 10
    }
  },
  data () {
    return {
      schedules: {},
      time: '',
      group: null,
      groups: [{ text: 'Выберите группу', value: null, disabled: true }],
      teacher: null,
      teachers: [{ text: 'Выберите преподавателя', value: null, disabled: true }],
      classroom: null,
      classrooms: [{ text: 'Выберите дисциплину', value: null, disabled: true }],
      subject: null,
      subjects: [
        { text: 'математика', value: 'm' },
        { text: 'химия', value: 'c' },
        { text: 'английский ', value: 'e' },
        { text: 'компьютерная наука', value: 'p' }
      ],
      day: null,
      days: [
        { text: 'понедельник', value: 'mon' },
        { text: 'вторник', value: 'tue' },
        { text: 'среда', value: 'wed' },
        { text: 'четверг', value: 'thu' },
        { text: 'пятница', value: 'fri' },
        { text: 'суббота', value: 'sat' }
      ]
    }
  },
  methods: {
    submit () {
      window.event.preventDefault()
      const data = {
        group: this.group,
        time: this.time,
        day: this.day,
        subject: this.subject,
        teacher: this.teacher,
        classroom: this.classroom
      }
      this.axios
        .post('http://127.0.0.1:8000/api/schedules/new', data)
        .then(response => { console.log(response); this.reset() })
        .catch(err => { console.log(err) })
    },
    update (id) {
      const data = {
        group: this.group,
        time: this.time,
        day: this.day,
        subject: this.subject,
        teacher: this.teacher,
        classroom: this.classroom
      }
      this.axios
        .patch('http://127.0.0.1:8000/api/schedules/update/' + id, data)
        .then(response => { console.log(response); this.reset() })
        .catch(err => { console.log(err) })
    },
    deleteSchedule (id) {
      const url = 'http://127.0.0.1:8000/api/schedules/delete/' + id
      this.axios
        .delete(url)
        .then(response => { console.log(response) })
    },
    reset () {
      this.classroom = null
      this.teacher = null
      this.day = null
      this.subject = null
      this.group = null
      this.time = ''
    },
    showGroups (groups) {
      for (let i = 0; i < groups.length; i++) {
        const group = {}
        group.value = groups[i].id
        group.text = groups[i].number

        this.groups.push(group)
      }
    },
    showTeachers (teachers) {
      for (let i = 0; i < teachers.length; i++) {
        const teacher = {}
        teacher.value = teachers[i].id
        teacher.text = teachers[i].first_name

        this.teachers.push(teacher)
      }
    },
    showClassrooms (classrooms) {
      for (let i = 0; i < classrooms.length; i++) {
        const classroom = {}
        classroom.value = classrooms[i].id
        classroom.text = classrooms[i].number

        this.classrooms.push(classroom)
      }
    },
    showSchedules (data) {
      this.schedules = []
      for (let i = 0; i < data.length; i++) {
        const schedule = {}
        schedule.id = data[i].id
        schedule.time = data[i].time
        schedule.day = data[i].day
        schedule.subject = data[i].subject
        schedule.group = data[i].group
        schedule.teacher = data[i].teacher
        schedule.classroom = data[i].classroom
        console.log(schedule)
        this.schedules.push(schedule)
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
      .get('http://127.0.0.1:8000/api/teachers/list')
      .then(response => {
        console.log(response); this.showTeachers(response.data)
      })
      .catch(err => { console.log(err) })
    this.axios
      .get('http://127.0.0.1:8000/api/classrooms/list')
      .then(response => {
        console.log(response); this.showClassrooms(response.data)
      })
      .catch(err => { console.log(err) })
    this.axios
      .get('http://127.0.0.1:8000/api/schedules/list')
      .then(response => {
        console.log(response); this.showSchedules(response.data)
      })
      .catch(err => { console.error(err) })
  }
}
</script>

<style scoped>

</style>
