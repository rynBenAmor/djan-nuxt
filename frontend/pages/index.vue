<script setup>
    import { ref, onMounted } from 'vue'
    import axios from 'axios'
    import { BACKEND_URL } from '~/config'

    const comments = ref([])
    const newComment = ref("")

    const fetchComments = async () => {
        const { data } = await axios.get(BACKEND_URL + "/comments/")
        comments.value = data
    }

    const postComment = async () => {
        if (newComment.value.trim()) {
            await axios.post( BACKEND_URL + "/comments/", { text: newComment.value })
            newComment.value = ""
            fetchComments()  // Refresh after posting
        }
    }

    onMounted(fetchComments)
</script>

<template>
    <div class="container">
        <Counter></Counter>
        <h1 class="text-primary">💬 Real-Time Comments</h1>

        <div class="input-group mb-3">
            <input v-model="newComment" @keyup.enter="postComment" type="text" class="form-control" placeholder="Write a comment..." />
            <button @click="postComment" class="btn btn-primary">Post</button>
        </div>

        <ul class="list-group">
            <CommentItem v-for="comment in comments" :key="comment.id" :comment="comment" />
        </ul>
    </div>
</template>

