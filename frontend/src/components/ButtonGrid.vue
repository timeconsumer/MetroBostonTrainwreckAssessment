<template>
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
</template>
<script>
import axios from 'axios'

const API_URL = 'http://localhost:8000'
  export default {
    name: 'train-grid',
    data () {
        this.getTrainLines()

        return {
        trainlines: []
        }
    },
    methods: {
        getTrainLines() {
        const url = `${API_URL}/api/trains/`
        return axios.get(url).then((response) => {
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
