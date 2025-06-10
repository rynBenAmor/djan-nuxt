<template>
    <div class="container">
        <h1 class="mb-4 text-light display-1"> <i class="bi bi-android2"></i> Nuxt Blog <br> with Django <br> TL;DR</h1>

        <!-- Form to Create a Post -->
        <div class="card p-3 mb-4" @keyup.enter="createPost">
            <input v-model="title" class="form-control mb-2" placeholder="Post Title" />
            <textarea v-model="content" class="form-control mb-2" placeholder="Post Content"></textarea>
            <button @click="createPost" class="btn btn-primary">Create Post</button>
        </div>

        <!-- Blog Posts -->
        <div v-for="post in posts" :key="post.id" class="card p-3 mb-3">
            <h3>{{ post.title }}</h3>
            <p>{{ post.content }}</p>
            <hr />
            <p><strong>TL;DR:</strong> {{ post.summary || "Generating..." }}</p>
        </div>
    </div>
</template>



<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { BACKEND_URL } from "~/config";

const posts = ref([]);
const title = ref("");
const content = ref("");

const fetchPosts = async () => {
    const { data } = await axios.get( BACKEND_URL + "/posts/");
    posts.value = data;
};

const createPost = async () => {
    await axios.post( BACKEND_URL + "/posts/", {
        title: title.value,
        content: content.value,
    });
    title.value = "";
    content.value = "";
    fetchPosts();//after creation refetch
};

onMounted(fetchPosts);// initial fetch
</script>

<style>
.container {
    max-width: 600px;
}
</style>