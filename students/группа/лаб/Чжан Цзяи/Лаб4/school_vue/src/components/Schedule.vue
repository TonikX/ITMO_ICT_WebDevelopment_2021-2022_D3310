<template>
  <v-data-table
    :headers="headers"
    :items="schedules"
    item-key="id"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Список Расписания</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <v-spacer>
            <v-btn
              color="primary"
              dark
              class="mb-2"
              @click="addNewSchedule"
            >
              Новое Расписание
            </v-btn>
        </v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <v-card>
            <v-card-title>
              <span class="text-h5"></span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="time"
                      :counter="10"
                      label="Время"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      v-model="subject"
                      :items="subjects"
                      label="Дисциплина"
                      required
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      v-model="day"
                      :items="days"
                      label="День"
                      required
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      v-model="group"
                      :items="groups"
                      label="Группа"
                      required
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      v-model="teacher"
                      :items="teachers"
                      label="Приподаватель"
                      required
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      v-model="classroom"
                      :items="classrooms"
                      label="Аудитория"
                      required
                    ></v-select>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
              color="blue darken-1"
              text
              @click="cancel"
              >
              Не
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="submit"
              >
                Сохранить
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-btn
        small
        @click="addSchedule"
      >
        Обновить
      </v-btn>
      <v-dialog
      max-width="500px"
      v-model="show"
      >
        <v-card>
            <v-card-title>
              <span class="text-h5"></span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="time"
                      :counter="10"
                      label="Время"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      v-model="subject"
                      :items="subjects"
                      label="Дисциплина"
                      required
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      v-model="day"
                      :items="days"
                      label="День"
                      required
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      v-model="group"
                      :items="groups"
                      label="Группа"
                      required
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      v-model="teacher"
                      :items="teachers"
                      label="Приподаватель"
                      required
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      v-model="classroom"
                      :items="classrooms"
                      label="Аудитория"
                      required
                    ></v-select>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="blue darken-1"
              text
              @click="cancel"
            >
              Не
            </v-btn>
            <v-btn
              color="blue darken-1"
              text
              @click="update(item.id)"
            >
              Сохранить
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-btn
        small
        @click="deleteSchedule(item.id)"
      >
        удалить
      </v-btn>
    </template>
  </v-data-table>
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
      show: false,
      dialog: false,
      headers: [
        {
          text: 'Расписание',
          align: 'start',
          sortable: false,
          value: 'id'
        },
        { text: 'Время', value: 'time' },
        { text: 'День', value: 'day' },
        { text: 'Дисциплина', value: 'subject' },
        { text: 'Группа', value: 'group' },
        { text: 'Приподаватель', value: 'teacher' },
        { text: 'Аудитория', value: 'classroom' },
        { text: 'Actions', value: 'actions', sortable: false }
      ],
      schedules: [],
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
    addNewSchedule () {
      this.dialog = true
    },
    cancel () {
      this.show = false
      this.dialog = false
    },
    addSchedule () {
      this.show = true
    },
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

