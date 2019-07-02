<template>
    <div class="register">
      <el-form>
        <h2>Créer un nouveau client ?</h2>
        <el-form-item class="form-register">
          <el-input placeholder="Prénom" v-model="register.name" class="form-input-register"></el-input>
          <el-input
            placeholder="Argent"
            v-model="register.count"
            required
            pattern="[^-]"
            class="form-input-register"
          ></el-input>
          <el-button @click="addCustomer" type="primary" class="button-register">Créer</el-button>
        </el-form-item>
      </el-form>
    </div>
</template>

<script>
export default {
  data() {
    return {
      register: {
        name: "",
        count: null
      },
      moneyRequest: 0,
      currentId: -1,
      currentCustomer: {},
      customers: []
    };
  },
  methods: {
    async created() {
      this.customers = (await this.$http.get("/customers")).data;
    },
    async getCustomer() {
      this.customers = (await this.$http.get("/customers")).data;
    },
    isSolvent() {
      if (
        (this.moneyRequest > 0 &&
          this.moneyRequest <= this.currentCustomer["count"]) ||
        this.moneyRequest < 0
      )
        this.debit();
      else alert(`Vous n'avez pas les fonds sufisant !`);
    },
    debit() {
      if (this.moneyRequest > 0) {
        this.currentCustomer["count"] -= this.moneyRequest;
        alert(`Vous venez de retirer ${this.moneyRequest} euros`);
      } else {
        this.currentCustomer["count"] -= this.moneyRequest;
        alert(`Vous venez d'ajouter ${-this.moneyRequest} euros`);
      }
      this.transaction();
    },
    async addCustomer() {
      // console.log("TESTEEEEEEEEEEEEEEEEUUH");
      const data = this.register;
      const response = await this.$http.post("/customers", data);
      this.getCustomer();
    },
    async transaction() {
      const data = {
        index: this.currentId,
        customer: this.customers[this.currentId]
      };
      const response = await this.$http.put("/customers", data);
      this.getCustomer();
    },
    async deleteCustomer() {
      const data = {
        params: {
          id: this.currentCustomer.id
        }
      };
      const response = await this.$http.delete("/customers", data);
      this.getCustomer();
    }
  }
};
</script>

<style>
.form-register {
  margin: auto;
  width: 200px;
}

.form-input-register {
  height: 50px;
}

.el-button span {
  font-size: 22px;
  font-weight: bold;
  font-family: "Amatic SC", cursive;
}
</style>
