<template>
  <div class="money-distributor">
    <div id="register">
      <h3>Créer un nouveau client ?</h3>
      <input type="text" placeholder="Prénom" v-model="register.name">
      <input type="number" placeholder="Argent" v-model="register.count" required pattern="[^-]">
      <button @click="addCustomer">Créer</button>
    </div>
    <br>
    <p>------------</p>
    <div v-if="customers.length">
      <div>
        <span class="customer" v-for="(customer, index) in customers" :key="customer.id">
          <button @click.prevent="currentCustomer = customer, currentId = index">
            <strong>{{ customer.name }}</strong>
          </button>
        </span>
      </div>
      {{ currentCustomer.id }}
      <br>
      <button @click="deleteUser">Delete User</button>
      <p>------------</p>
      <div>
        <br>
        <label>Pour retirer, nombre positif. Pour déposer, nombre négatif.</label>
        <br>
        <input type="number" v-model="moneyRequest" placeholder="Montant désiré..">
        <button type="submit" @click="isSolvent">Valider</button>
        <br>
        <br>
        Solde de {{ currentCustomer.name }}: {{ currentCustomer.count }}
        <br>
        moneyRequest: {{ moneyRequest }}
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";

@Component
export default class MoneyDistributor extends Vue {
  register: object = {
    name: null,
    count: null
  };
  moneyRequest: number = 0;
  currentId: number = -1;
  currentCustomer: any = {};
  customers: any[] = [];
  async created() {
    this.customers = (await this.$http.get("/customers")).data;
  }
  async getCustomer() {
    this.customers = (await this.$http.get("/customers")).data;
  }
  isSolvent() {
    if (
      (this.moneyRequest > 0 &&
        this.moneyRequest <= this.currentCustomer["count"]) ||
      this.moneyRequest < 0
    )
      this.debit();
    else alert(`Vous n'avez pas les fonds sufisant !`);
  }
  debit() {
    if (this.moneyRequest > 0) {
      this.currentCustomer["count"] -= this.moneyRequest;
      alert(`Vous venez de retirer ${this.moneyRequest} euros`);
    } else {
      this.currentCustomer["count"] -= this.moneyRequest;
      alert(`Vous venez d'ajouter ${-this.moneyRequest} euros`);
    }
    this.transaction();
  }
  async addCustomer() {
    const data = this.register;
    const response = await this.$http.post("/customers", data);
    this.getCustomer();
  }
  async transaction() {
    const data = {
      index: this.currentId,
      customer: this.customers[this.currentId]
    };
    const response = await this.$http.put("/customers", data);
    this.getCustomer();
  }
  async deleteUser() {
    const data = {
      params: {
        id: this.currentCustomer.id
      }
    };
    //  const datas = this.currentCustomer.id;
    const response = await this.$http.delete("/customers", data);
    this.getCustomer();
    //  data['params']['id'] = null;
  }
}
</script>

<style>
</style>