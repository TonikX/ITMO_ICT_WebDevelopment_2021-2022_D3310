<template>
  <v-data-table
    :headers="headers"
    :items="students"
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
              @click="addNewStudent"
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
                      v-model="first_name"
                      :counter="10"
                      label="Имя"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="last_name"
                      :counter="10"
                      label="Фамилия"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="last_name"
                      :counter="10"
                      label="Фамилия"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      v-model="sex"
                      :items="sexes"
                      label="Пол"
                      required
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="score_math"
                      :counter="10"
                      label="Оценка по математике"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="score_chemical"
                      :counter="10"
                      label="Оценка химиката"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="score_english"
                      :counter="10"
                      label="Оценка по английскому"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="score_computer"
                      :counter="10"
                      label="Оценка по компьютеру"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="semester"
                      :counter="10"
                      label="Семестр"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="group"
                      :counter="10"
                      label="Группа"
                      required
                    ></v-text-field>
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
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-btn
        small
        @click="addStudent"
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
                      v-model="first_name"
                      :counter="10"
                      label="Имя"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="last_name"
                      :counter="10"
                      label="Фамилия"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="last_name"
                      :counter="10"
                      label="Фамилия"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      v-model="sex"
                      :items="sexes"
                      label="Пол"
                      required
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="score_math"
                      :counter="10"
                      label="Оценка по математике"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="score_chemical"
                      :counter="10"
                      label="Оценка химиката"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="score_english"
                      :counter="10"
                      label="Оценка по английскому"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="score_computer"
                      :counter="10"
                      label="Оценка по компьютеру"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="semester"
                      :counter="10"
                      label="Семестр"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="group"
                      :counter="10"
                      label="Группа"
                      required
                    ></v-text-field>
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
        @click="deleteStudent(item.id)"
      >
        удалить
      </v-btn>
    </template>
  </v-data-table>
</template>

<script>
export default {
  name: 'Student',
  data () {
    return {
      show: false,
      dialog: false,
      headers: [
        {
          text: 'Студент',
          align: 'start',
          sortable: false,
          value: 'id'
        },
        { text: 'Пол', value: 'sex' },
        { text: 'Имя', value: 'first_name' },
        { text: 'Фамилия', value: 'last_name' },
        { text: 'Оценка по математике', value: 'score_math' },
        { text: 'Оценка химиката', value: 'score_chemical' },
        { text: 'Оценка по английскому', value: 'score_english' },
        { text: 'Оценка по компьютеру', value: 'score_computer' },
        { text: 'Семестр', value: 'semester' },
        { text: 'Группа', value: 'group' },
        { text: 'Actions', value: 'actions', sortable: false }
      ],
      students: [],
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
    addNewStudent () {
      this.dialog = true
    },
    cancel () {
      this.show = false
      this.dialog = false
    },
    addStudent () {
      this.show = true
    },
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
