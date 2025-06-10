<script setup>

defineProps({
  comment: Object,  // Accepts a comment object as a prop
});
</script>

<template>
  <li class="list-group-item">
    <NuxtLink :to="`/comments/${comment.id}`" class="text-decoration-none">
      {{ comment.text }}
    </NuxtLink>
    <span :class="{
      'text-success': comment.sentiment === 'positive',
      'text-warning': comment.sentiment === 'neutral',
      'text-danger': comment.sentiment === 'negative'
    }">
      ({{ comment.sentiment }})
    </span>
  </li>
</template>
