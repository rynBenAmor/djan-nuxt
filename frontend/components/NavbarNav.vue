<template>

    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <ul class="navbar-nav me-auto">
                <li class="nav-item">
                    <NuxtLink class="nav-link" to="/">Home</NuxtLink>
                </li>

                <li class="nav-item">
                    <NuxtLink class="nav-link" to="/captions">Captions</NuxtLink>
                </li>
                <li class="nav-item">
                    <NuxtLink class="nav-link" to="/blog">Blog</NuxtLink>
                </li>
                <li class="nav-item">
                    <NuxtLink class="nav-link" to="/profile">Profile</NuxtLink>
                </li>
                <li class="nav-item">
                    <NuxtLink v-if="!user" class="nav-link" to="/login">Login</NuxtLink>
                    <span v-else class="nav-link">👤 {{ user.username }}</span>
                </li>
            </ul>
        </div>
    </nav>
</template>



<script>
import axios from "axios";
import { BACKEND_URL } from "./config";

export default {
    name: 'NavbarNav',
    layout: 'defaultLayout',
    data() {
        return {
            user: null,
        };
    },
    methods: {
        async fetchUser() {
            const token = localStorage.getItem(BACKEND_URL + "token"); // Retrieve token from storage
            if (!token) return; // No token, no request

            try {
                const { data } = await axios.get("/auth/users/me/", {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                });
                this.user = data; // Store user details
            } catch (error) {
                console.error("Failed to fetch user:", error);
                localStorage.removeItem("token"); // Remove invalid token
            }
        },
    },
    mounted() {
        this.fetchUser(); // Fetch user on mount
    },
};
</script>



<style scoped>
.router-link-active, .router-link-exact-active{
    color: rgb(34, 136, 252);
    font-weight: bold;
    text-decoration: underline;
}
</style>c