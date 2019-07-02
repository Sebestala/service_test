<template>
  <div class="del">
    <h2>Selectionnez un compte à supprimer.</h2>
    <div class="delete">
      <customers-list @change="currentId = $event"/>
      <el-button @click="deleteCustomer" type="danger" class="button-delete">Supprimer</el-button>
    </div>
  </div>
</template>

<script>
import CustomersList from "./CustomersList.vue";

export default {
  components: { CustomersList },
  data() {
    return {
      currentId: null,
      customers: []
    };
  },
  async created() {
    this.customers = (await this.$http.get("/customers")).data;
  },
  methods: {
    async getCustomer() {
      this.customers = (await this.$http.get("/customers")).data;
    },
    async deleteCustomer() {
      const data = {
        params: {
          id: this.currentId
        }
      };
      const response = await this.$http.delete("/customers", data);
      this.currentId = null;
      this.getCustomer();
      this.$emit("refreshCustomerList");
    }
  }
};
</script>

<style>
.delete {
  margin-bottom: 1em;
  font-weight: bold;
  display: inline-flex;
}

.button-delete {
  font-size: 22px;
  height: 32px;
  width: 84px;
  margin-left: 5px;
  line-height: 5px;
  padding: 7px;
}

.select {
  font-size: 18px;
  font-weight: bold;
  color: #398dce;
  font-family: "Amatic SC", cursive;
}
</style>