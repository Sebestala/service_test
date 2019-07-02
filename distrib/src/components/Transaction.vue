<template>
  <div>
    <h2>Selectionnez un compte pour effectuer une transaction.</h2>
    <div class="transaction">
      <customers-list @change="currentId = $event"/>
      <div>
        <h3 v-if="currentId">Vous avez un solde de : {{ getCurrentcustomer.count }}€</h3>
        <h3 v-else>Aucun compte sélectionné.</h3>
      </div>
      <el-form class="block-request-money">
        <el-input placeholder="Montant désiré.." v-model="moneyRequest" class="input-request-money"></el-input>
        <el-button @click="isSolvent" type="primary" class="button-validate">Valider</el-button>
      </el-form>
      <h5>*Pour retirer: nombre positif. Pour déposer: nombre négatif.</h5>
    </div>
  </div>
</template>

<script>
import CustomersList from "./CustomersList.vue";

export default {
  components: { CustomersList },
  data() {
    return {
      currentId: 0,
      moneyRequest: 0,
      countCurrentCustomer: "",
      customers: []
    };
  },
  async created() {
    this.customers = (await this.$http.get("/customers")).data;
  },
  computed: {
    getCurrentcustomer() {
      for (let i = 0; i < this.customers.length; i++) {
        if (this.customers[i].id === this.currentId) {
          return this.customers[i];
        }
      }
    }
  },
  methods: {
    async getCustomer() {
      this.customers = (await this.$http.get("/customers")).data;
    },
    isSolvent() {
      if (
        (this.moneyRequest > 0 &&
          this.moneyRequest <= this.getCurrentcustomer.count) ||
        this.moneyRequest < 0
      )
        this.debit();
      else alert(`Vous n'avez pas les fonds sufisant !`);
    },
    debit() {
      if (this.moneyRequest > 0) {
        this.getCurrentcustomer.count -= this.moneyRequest;
        alert(`Vous venez de retirer ${this.moneyRequest} euros`);
      } else {
        this.getCurrentcustomer.count -= this.moneyRequest;
        alert(`Vous venez d'ajouter ${-this.moneyRequest} euros`);
      }
      this.transaction();
    },
    async transaction() {
      const data = {
        count: this.getCurrentcustomer.count,
        name: this.getCurrentcustomer.name
      };
      console.log(data);
      const response = await this.$http.put("/customers", data);
      this.getCustomer();
    }
  }
};
</script>

<style>
.button-validate {
  font-size: 22px;
  height: 32px;
  width: 80px;
  margin-left: 5px;
  line-height: 5px;
  padding: 7px;
}

.block-request-money {
  display: inline-flex;
}
</style>