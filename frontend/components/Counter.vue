<script setup>
import { useCounterStore } from "@/stores/counter"; // Import the store

const counter = useCounterStore(); // Access the store
</script>

<template>
  <div class="container text-center my-5">
    <h1 class="text-light fw-bold">Counter: {{ counter.count }}</h1>
    <button class="btn btn-primary mx-2" @click="counter.increment">➕ Increment</button>
    <button class="btn btn-danger mx-2" @click="counter.decrement">➖ Decrement</button>
    <button class="btn btn-warning mx-2" @click="counter.reset">🔄 Reset</button>
    <hr class="border border-2 border-light">
  </div>
</template>
