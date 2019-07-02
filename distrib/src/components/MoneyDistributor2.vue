<template>
  <div class="money-distributor">
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
    <div class="column">
      <el-row>
        <el-col :span="24">
          <div class="grid-content bg-purple-dark"></div>
        </el-col>
      </el-row>
    </div>
    <div class="delete">
      <el-select v-model="value" class="select">
        <el-option v-for="customer in customers" :key="customer.id" :label="customer.name"></el-option>
      </el-select>
      <el-button @click="deleteCustomer" type="danger" class="button-delete">Supprimer</el-button>
    </div>
    <div class="column2">
      <el-row>
        <el-col :span="24">
          <div class="grid-content bg-purple-dark"></div>
        </el-col>
      </el-row>
    </div>
    <div class="money">
      <h3>Solde de {{ currentCustomer.name }}: {{ currentCustomer.count }}</h3>
      <el-form :model="form" class="block-request-money">
        <el-input placeholder="Montant désiré.." v-model="moneyRequest" class="input-request-money"></el-input>
        <el-button @click="isSolvent" type="primary" class="button-delete">Valider</el-button>
      </el-form>
      <h5>*Pour retirer: nombre positif. Pour déposer: nombre négatif.</h5>
    </div>
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
      console.log("TESTEEEEEEEEEEEEEEEEUUH");
      const data = this.register;
      print("TESTEEEEEEEEEEEEEEEEUUH");
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
.money-distributor {
  font-family: "Amatic SC", cursive;
  margin: auto;
}

.form-register {
  margin: auto;
  width: 200px;
}

.form-input-register {
  height: 50px;
}

.delete {
  display: inline-flex;
}

.el-button span {
  font-size: 22px;
  font-weight: 700;
  font-family: "Amatic SC", cursive;
}

.button-delete {
  margin-left: 5px !important;
}

.block-request-money {
  display: inline-flex;
}

.column,
.column2,
.money {
  margin: auto;
  width: 200px;
}

.grid-content {
  border-radius: 50px;
  min-height: 5px;
}

.bg-purple-dark {
  background: #dbe9f3;
}

.column {
  margin-bottom: 26px;
}

.column2 {  
  margin-top: 26px;
}
</style>