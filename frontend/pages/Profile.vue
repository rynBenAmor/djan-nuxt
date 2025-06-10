<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { BACKEND_URL } from "~/config";

const profiles = ref([]);
const cityChoices = ref([]);
const weatherData = ref({});

const fetchProfiles = async () => {
  try {
    const { data } = await axios.get( BACKEND_URL + "/profiles/");

    // If the API response contains one object, extract profiles from it
    if (Array.isArray(data) && data.length > 0) {
      profiles.value = data.map(({ city_choices, ...profile }) => profile); // Extract only profile data
      cityChoices.value = data[0].city_choices || []; // Get city choices from the first object
    }
  } catch (error) {
    console.error("Error fetching profiles:", error);
  }
};

const fetchWeather = async (city, profileId) => {
  if (!city) return;
  const apiKey = "6c5d9dc608d427307991785efd838ebd";
  const { data } = await axios.get(
    `https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid=6c5d9dc608d427307991785efd838ebd&units=metric`
  );
  weatherData.value[profileId] = data;
};

const updateCity = async (profileId, newCity) => {
  await axios.patch( BACKEND_URL + `/profiles/${profileId}/`, {
    city: newCity,
  });
  fetchWeather(newCity, profileId);
};

onMounted(fetchProfiles);
</script>



<template>
    <div class="container p-5">
      <h1 class="text-primary">🌍 User Profiles</h1>
  
   
        <div v-for="profile in profiles" :key="profile.id" class="card p-3 mb-3">
          <h3>{{ profile.name }}</h3>
  
          <div>
            <label for="city">Select City:</label>
            <select v-model="profile.city" class="form-select" @change="updateCity(profile.id, profile.city)">
              <option v-for="choice in cityChoices" :key="choice[0]" :value="choice[0]">
                {{ choice[1] }}
              </option>
            </select>
          </div>
  
          <div v-if="weatherData[profile.id]" class="mt-3">
            <h4>🌤 Weather in {{ weatherData[profile.id].name }}</h4>
            <p>🌡 Temperature: {{ weatherData[profile.id].main.temp }}°C</p>
            <p>💨 Wind: {{ weatherData[profile.id].wind.speed }} m/s</p>
            <p>☁ Condition: {{ weatherData[profile.id].weather[0].description }}</p>
          </div>
        </div>

  

    </div>
  </template>
  

<style scoped>
.card {
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
}
</style>
