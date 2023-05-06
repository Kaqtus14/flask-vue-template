<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import { http } from '../http'

const msg = ref("");

onMounted(async () => {
    let resp = await http.get("/api/message")
    msg.value = resp.data;
});
</script>

<template>
    <div id="container">
        <h1>Hello from Vue!</h1>
        <h1>{{ msg }}</h1>
    </div>
</template>
  
<style scoped>
#container {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 3vw;
    margin: auto;
}
</style>
