<template>
  <div class="money-distributor">
    <span class="list-customers">
      <ul>
        <li class="customer" v-for="(customer, index) in customers" :key="customer.id">
          <button :class="{selected: nameCurrentCustomer === customer}" @click.prevent="nameCurrentCustomer = customer.name, idCurrentCustomer = index" ><strong>{{ customer.name }}</strong></button>
        </li>
      </ul>
    </span>
    <input type="number" v-model="moneyRequest" placeholder="Montant désiré..">
    <button type="submit " @click="isSolvent" autofocus formmethod="post">Valider</button>
    <br>Solde de {{ this.nameCurrentCustomer }}: {{ this.customers[this.idCurrentCustomer].amount }}
    <br>moneyRequest: {{ this.moneyRequest }}
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator"; 

@Component
export default class MoneyDistributor extends Vue {
  moneyRequest: number = 0;
  nameCurrentCustomer: string = ""; 
  idCurrentCustomer: number = 0;
  textDebit: string = `Vous venez de retirer ${this.moneyRequest} euros`; // n'affiche pas la bonne valeur
  customers = [
    {
      name: "Tony",
      amount: 800,
    },
    {
      name: "Lily",
      amount: 8900,
    },
    {
      name: "Holy",
      amount: 10,
    },
  ];
  isSolvent() {
    if (this.moneyRequest < this.customers[this.idCurrentCustomer].amount) 
      this.debit();
    else 
      alert(`Vous n'avez pas les fonds sufisant !`);
  }
  debit() {
    this.customers[this.idCurrentCustomer].amount -= this.moneyRequest;
    alert(this.textDebit);
  }
}
</script>

<style>
</style>