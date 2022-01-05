<template>
  <v-data-table
    :headers="headers"
    :items="teachers"
    item-key="id"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Список Приподаватель</v-toolbar-title>
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
              @click="addNewTeacher"
          >
              Новый приподаватель
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
                      label="Фамиля"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="b_date"
                      :counter="10"
                      label="Время начала"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="e_date"
                      :counter="10"
                      label="Время закончила"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="office"
                      :counter="10"
                      label="кабинет"
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
        @click="addTeacher"
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
                    label="Фамиля"
                    required
                  ></v-text-field>
                </v-col>
                <v-col
                  cols="12"
                  sm="6"
                  md="4"
                >
                  <v-text-field
                    v-model="b_date"
                    :counter="10"
                    label="Время начала"
                    required
                  ></v-text-field>
                </v-col>
                <v-col
                  cols="12"
                  sm="6"
                  md="4"
                >
                  <v-text-field
                    v-model="e_date"
                    :counter="10"
                    label="Время закончила"
                    required
                  ></v-text-field>
                </v-col>
                <v-col
                  cols="12"
                  sm="6"
                  md="4"
                >
                  <v-text-field
                    v-model="office"
                    :counter="10"
                    label="кабинет"
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
        @click="deleteTeacher(item.id)"
      >
        удалить
      </v-btn>
    </template>
  </v-data-table>
</template>

<script>
export default {
  name: 'Teacher',
  data () {
    return {
      show: false,
      dialog: false,
      headers: [
        {
          text: 'Приподаватель',
          align: 'start',
          sortable: false,
          value: 'id'
        },
        { text: 'Имя', value: 'first_name' },
        { text: 'Фамилия', value: 'last_name' },
        { text: 'Дисциплина', value: 'subject' },
        { text: 'Время начала', value: 'b_date' },
        { text: 'Время закончила', value: 'e_date' },
        { text: 'Кабинет', value: 'office' },
        { text: 'Actions', value: 'actions', sortable: false }
      ],
      teachers: [],
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
    addNewTeacher () {
      this.dialog = true
    },
    cancel () {
      this.show = false
      this.dialog = false
    },
    addTeacher () {
      this.show = true
    },
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
