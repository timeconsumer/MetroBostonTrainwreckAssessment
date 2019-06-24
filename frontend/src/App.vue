<template>
  <div>
    <button
      class="btn btn-primary btn-margin"
      @click="login()">
      Login
    </button>

    <button
      class="btn btn-primary btn-margin"
      @click="getTrainLines()">
      Call Private
    </button>

    <button
      class="btn btn-primary btn-margin"
      @click="logout()">
      Logout
    </button>
    {{ message }}
    <br>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Line Name</th>
          <th scope="col">Status</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="trainline in trainlines" v-bind:key="trainline">
          <th scope="row">{{trainline.id}}</th>
          <td>{{trainline.line_name}}</td>
          <td>{{trainline.status}}</td>
          <td>
            <button class="btn btn-info" v-on:click="getTrainLine(trainline.id)">Edit</button>
            <button class="btn btn-danger" v-on:click="deleteTrainLine(trainline.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import AuthService from './auth/AuthService'
import axios from 'axios'

const API_URL = 'http://localhost:8000'
const auth = new AuthService()

export default {
  name: 'app',
  data () {
    // this.handleAuthentication()
    this.authenticated = false
    this.handleAuthentication()
    this.getTrainLines()

    auth.authNotifier.on('authChange', authState => {
      this.authenticated = authState.authenticated
    })

    return {
      authenticated: false,
      message: '',
      trainlines: []
    }
  },
  methods: {
    // this method calls the AuthService login() method
    login () {
      auth.login()
    },
    handleAuthentication () {
      auth.handleAuthentication()
    },
    logout () {
      auth.logout()
    },
    privateMessage () {
      const url = `${API_URL}/trains/private/1`
      return axios.get(url, {headers: {Authorization: `Bearer ${auth.getAuthToken()}`}}).then((response) => {
        console.log(response.data)
        this.message = response.data || ''
      })
    },
    getTrainLines() {
      const url = `${API_URL}/api/trains/`
      return axios.get(url, {headers: {Authorization: `Bearer ${auth.getAuthToken()}`}}).then((response) => {
        console.log(response.data)
        this.trainlines = response.data || []
      })
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}


@import'~bootstrap/dist/css/bootstrap.css'
</style>
