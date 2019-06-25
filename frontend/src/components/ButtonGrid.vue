<template>
    <div>
    <edit-line-modal :myProp="selectedLine" v-if="showModal" @close="showModal = false">
    <!--
      you can use custom content here to overwrite
      default content
    -->
    <h3 slot="header">Edit {{selectedLine.line_name}}</h3>
  </edit-line-modal>
    <div class="btn-grp btn-matrix">
        <button class="btn btn-info" v-for="trainline in trainlines" v-bind:key="trainline.id" v-on:click="getTrainLine(trainline.id)"> {{trainline.line_name}} </button>

    </div>
    </div>
</template>
<script>
import axios from 'axios'
import EditLineModal from './EditLineModal'

const API_URL = 'http://localhost:8000'
  export default {
    name: 'train-grid',
    components: {'edit-line-modal': EditLineModal},
    data () {
        this.getTrainLines()
        var showModal = false
        return {
        trainlines: [],
        selectedLine: {},
        showModal: false
        }
    },
    methods: {
        getTrainLines() {
            const url = `${API_URL}/api/trains/`
            return axios.get(url).then((response) => {
                console.log(response.data)
                this.trainlines = response.data || []
            })
        },
        getTrainLine(id) {
            const url = `${API_URL}/api/trains/${id}/`
            return axios.get(url).then((response) => {
                console.log(response.data)
                this.selectedLine = response.data
                this.showModal = true;
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
