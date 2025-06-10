<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, navigateTo } from 'nuxt/app'
import axios from 'axios'
import { BACKEND_URL } from '~/config'

const route = useRoute()
const comment = ref(null)

const fetchComment = async () => {
    try {
        const { data } = await axios.get( BACKEND_URL + `/comments/${route.params.id}/`)
        comment.value = data
    } catch (error) {
        console.error("Comment not found")
        navigateTo('/')  // Redirect if comment doesn't exist
    }
}

onMounted(fetchComment)
</script>

<template>
    <div class="container mt-5">
      <h1 class="text-primary text-center">📄 Comment Details</h1>
  
      <div class="d-flex justify-content-center">
        <div class="card shadow-lg" style="width: 30rem;">
          <div class="card-body">
            <h5 class="card-title text-primary">Comment Details</h5>
            
            <div v-if="comment">
              <p class="lead"><strong>Text:</strong> {{ comment.text }}</p>

              <p class="lead">
                <strong class="me-1">Sentiment:</strong>
                <span :class="{
                  'text-success': comment.sentiment === 'positive',
                  'text-warning': comment.sentiment === 'neutral',
                  'text-danger': comment.sentiment === 'negative'
                }">
                  {{ comment.sentiment }}
                </span>
              </p>
  
              <button @click="navigateTo('/')" class="btn btn-secondary mt-3 w-100">
                Back
              </button>
            </div>
  
            <div v-else class="text-center">
              <p>Loading...</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  


