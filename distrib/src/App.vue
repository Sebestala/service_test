<template>
  <div id="app">
    <div class="image">
      <img alt="Vue logo" src="./assets/evil-corp.png" @click="goto('/')">
    </div>
    <div class="body">
      <router-view/>
    </div>
    <footer>
      <!-- <router-link to="/home">Créer</router-link> -->
      <el-button type="text" @click="goto('/transaction')" title="Transaction sur le compte">
        Transaction
      </el-button>
      <el-button type="text" @click="goto('/createcustomer')" title="Création de compte client">
        Créer
      </el-button>
      <el-button type="text" @click="goto('/deletecustomer')" title="Suprimer un compte client">
        Supprimer
      </el-button>
      <!-- <router-link to="/deletecustomer">Supprimer</router-link> -->
      <!-- <router-link to="/transaction">Transactions</router-link> -->
    </footer>
  </div>
</template>

<script>
export default {
  name: "app",
  methods: {
    goto(path) {
      this.$router.push(path);
    }
  }
};
</script>

<style>
#app {
  font-family: "Amatic SC", cursive;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  text-align: center;
  margin-top: 60px;
}

footer span {
  font-family: "Amatic SC", cursive;
  font-weight: bold;
  font-size: 22px;
}
</style>