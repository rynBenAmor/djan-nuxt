<script setup>
import { ref } from "vue";
import axios from "axios";
import { BACKEND_URL } from "~/config";

const image = ref(null);
const caption = ref("");
const loading = ref(false);

const uploadImage = async () => {
  if (!image.value){
    alert('please upload an image !')
    return;
  } 
  loading.value = true;

  try {
    const formData = new FormData();
    formData.append("image", image.value);

    const { data } = await axios.post( BACKEND_URL + "/captions/", formData, {
      headers: { "Content-Type": "multipart/form-data" }
    });

    caption.value = data.caption;
  } catch (error) {
    console.error("Error uploading image:", error);
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div class="container">
    <h1 class="text-primary text-center">img auto caption</h1>

    <div class="card shadow-sm p-4">
      <input type="file" accept="image/*" class="form-control" @change="(e) => image = e.target.files[0]" />
      <button @click="uploadImage" class="btn btn-primary mt-3">
        <i class="bi bi-upload"></i> Upload & Get Caption
      </button>
    </div>

    <div v-if="loading" class="text-center mt-3">
      <i class="bi bi-arrow-clockwise text-primary spinner-border"></i> Processing...
    </div>

    <div v-if="caption" class="alert alert-info mt-3">
      <i class="bi bi-chat-left-quote"></i> {{ caption }}
    </div>
  </div>
</template>
