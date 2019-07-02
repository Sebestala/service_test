<template>
  <div class="customers-list">
    <el-select
      :value="currentId"
      @change="handleChange($event)"
      placeholder="Name..."
      class="select"
    >
      <el-option
        v-for="customer in customers"
        class="select"
        :value="customer.id"
        :key="customer.id"
        :label="customer.name"
      ></el-option>
    </el-select>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentId: null,
      customers: []
    };
  },
  async created() {
    this.customers = this.getCustomers();
    this.$parent.$on("refreshCustomerList", () => {
      this.customers = this.getCustomers();
      this.currentId = null;
    });
  },
  methods: {
    async getCustomers() {
      this.customers = (await this.$http.get("/customers")).data;
    },
    handleChange(event) {
      this.currentId = event;
      this.$emit("change", event);
    }
  }
};
</script>

<style>
.select {
  font-size: 18px;
  font-weight: bold;
  color: #398dce;
  font-family: "Amatic SC", cursive;
}
</style>