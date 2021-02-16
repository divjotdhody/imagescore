<template>
  <div class="container">
    <span class="mainTextSpan"><h2 class="mainText">Blinkpad Project</h2></span>
    <div class="imageContainer">
      <div class="eachImage">
        <div>
          <img
            class="individualImage"
            thumbnail
            fluid
            src="../assets/image1.jpg"
            alt="Image 1"
          />
        </div>
        <div class="counterButtons">
          <button id="score1" v-on:click="increase">
            <span class="material-icons">
              arrow_circle_up
            </span>
          </button>
          <button id="score1" v-on:click="decrease">
            <span class="material-icons">
              arrow_circle_down
            </span>
          </button>
        </div>
        <span class="counterValue">Score : {{ score1 }}</span>
      </div>
      <div class="eachImage">
        <div>
          <img
            class="individualImage"
            thumbnail
            fluid
            src="../assets/image2.jpg"
            alt="Image 2"
          />
        </div>
        <div class="counterButtons">
          <button id="score2" value="c1" v-on:click="increase">
            <span class="material-icons">
              arrow_circle_up
            </span>
          </button>
          <button id="score2" value="c1" v-on:click="decrease">
            <span class="material-icons">
              arrow_circle_down
            </span>
          </button>
        </div>
        <span class="counterValue">Score : {{ score2 }}</span>
      </div>
    </div>
    <div class="imageContainer">
      <div class="eachImage">
        <div>
          <img
            class="individualImage"
            thumbnail
            fluid
            src="../assets/image3.jpg"
            alt="Image 1"
          />
        </div>
        <div class="counterButtons">
          <button id="score3" v-on:click="increase">
            <span class="material-icons">
              arrow_circle_up
            </span>
          </button>
          <button id="score3" v-on:click="decrease">
            <span class="material-icons">
              arrow_circle_down
            </span>
          </button>
        </div>
        <span class="counterValue">Score : {{ score3 }}</span>
      </div>
      <div class="eachImage">
        <div>
          <img
            class="individualImage"
            thumbnail
            fluid
            src="../assets/image4.jpg"
            alt="Image 2"
          />
        </div>
        <div class="counterButtons">
          <button id="score4" v-on:click="increase">
            <span class="material-icons">
              arrow_circle_up
            </span>
          </button>
          <button id="score4" v-on:click="decrease">
            <span class="material-icons">
              arrow_circle_down
            </span>
          </button>
        </div>
        <span class="counterValue">Score : {{ score4 }}</span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import axios from "axios";
@Component
export default class ImagesComponent extends Vue{
    score1: number = 0
    score2: number = 0
    score3: number = 0
    score4: number = 0
    decrease(e:any):void  {
      if (e.toElement.parentElement.id === "score1") {
        this.score1 -= 1;
      } else if (e.toElement.parentElement.id === "score2") {
        this.score2 -= 1;
      } else if (e.toElement.parentElement.id === "score3") {
        this.score3 -= 1;
      } else if (e.toElement.parentElement.id === "score4") {
        this.score4 -= 1;
      }
      this.submit(e.toElement.parentElement.id);
    }
    increase(e:any): void {
      if (e.toElement.parentElement.id === "score1") {
        this.score1 += 1;
      } else if (e.toElement.parentElement.id === "score2") {
        this.score2 += 1;
      } else if (e.toElement.parentElement.id === "score3") {
        this.score3 += 1;
      } else if (e.toElement.parentElement.id === "score4") {
        this.score4 += 1;
      }
      this.submit(e.toElement.parentElement.id);
    }
    getstate(): void {
      axios
        .get("http://127.0.0.1:5000/api/getCounter")
        .then((response) => {
          const result = response.data;
          for (let res of result) {
            if (res.name === "score1") {
              this.score1 = res.count;
            } else if (res.name === "score2") {
              this.score2 = res.count;
            } else if (res.name === "score3") {
              this.score3 = res.count;
            } else if (res.name === "score4") {
              this.score4 = res.count;
            }
          }
        })
        .catch((err) => {
          console.log(err);
        });
    }
    submit(element:string):void {
      let dataElement = -1;
      if (element === "score1") {
        dataElement = this.score1;
      } else if (element === "score2") {
        dataElement = this.score2;
      } else if (element === "score3") {
        dataElement = this.score3;
      } else if (element === "score4") {
        dataElement = this.score4;
      }
      const payload = { name: element, counter: dataElement };
      axios
        .post("http://127.0.0.1:5000/api/updateCounter", payload)
        .then((response) => {
          const result = response.data;
          for (let res of result) {
            if (res.name === "score1") {
              this.score1 = res.count;
            } else if (res.name === "score2") {
              this.score2 = res.count;
            } else if (res.name === "score3") {
              this.score3 = res.count;
            } else if (res.name === "score4") {
              this.score4 = res.count;
            }
          }
        })
        .catch((err) => {
          console.log(err);
        });
    }
  created() {
    this.getstate();
  }
}
</script>

<style>
@media screen and (max-width: 999px) {
  .imageContainer {
    display: flex;
    text-align:center;
    flex-direction: column;
  }
  .eachImage {
    flex: 1 1 49%;
  }
}
.imageContainer {
  display: flex;
   text-align:center;
}
.eachImage {
  flex: 1 1 49%;
}

.counterValue {
  font-size: 16px;
  color: red;
  font-weight: 700;
}
.individualImage {
  padding: 0px;
  margin: 0px;
  width: 400px;
  height: 300px;
  border-radius: 10px;
  margin-bottom: 7px;
}
.incrementButton {
  border-color: green;
  padding: 2px;
  margin: 0 10px 10px 10px;
  width: 3vw;
  height: 4vh;
  border-radius: 10px;
}
.decrementButton {
  border-color: red;
  padding: 2px;
  margin: 0 10px 10px 10px;
  width: 3vw;
  height: 4vh;
  border-radius: 10px;
}
.counterButtons button {
  background-color: transparent;
  border: none;
}
.mainTextSpan {
    text-align: center;
}
</style>
