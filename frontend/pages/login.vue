<script setup>
import { ref } from "vue";
import axios from "axios";
import { BACKEND_URL } from "~/config";

const username = ref("tester"); 
const password = ref("123");
const errorMessage = ref(null);
const responseMessage = ref(null);


//on post requests use credentials to authenticate and get a token for later (so you don't have to repeat it every time browser refreshes)
const login = async () => {
  errorMessage.value = null;
  responseMessage.value = null;
  try {
    //authenticate and fetch the access and refresh tokens
    const { data } = await axios.post( BACKEND_URL + "/auth/jwt/create/", {
      username: username.value, 
      password: password.value,
    });

    localStorage.setItem("token", data.access); //
    alert("Login successful!");

    // Fetch authenticated user's data (defined below)
    await fetchUserData(data.access);
  } catch (error) {
    alert(error.response?.data);
    console.error(error.response?.data); 
    errorMessage.value = "Invalid credentials!";
  }
};


// define the function to fetch data
const fetchUserData = async (token) => {
  try {
    const { data } = await axios.get( BACKEND_URL + "/auth/users/me/", {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });
    responseMessage.value = data;
    console.log("Authenticated user data:", data);
  } catch (error) {
    console.error("Error fetching user data:", error.response?.data);
  }
};
</script>





<template>
  <div class="d-flex justify-content-center align-items-center">
    <div @keyup.enter="login" class="card p-4 shadow-sm w-50">
      <h2 class="text-center">Login</h2>

      <p v-if="errorMessage" class="alert alert-danger">{{ errorMessage }}</p>
      <p v-if="responseMessage" class="alert alert-info">{{ responseMessage }}</p>

      <div class="mb-3">
        <label class="form-label">Username</label>
        <input v-model="username" type="text" class="form-control" required />
      </div>

      <div class="mb-3">
        <label class="form-label">Password</label>
        <input v-model="password" type="password" class="form-control" required />
      </div>

      <button @click="login" class="btn btn-primary w-100">Login</button>

    </div>
  </div>
</template>


