<!-- src/views/LoginView.vue -->
<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="card">
          <div class="card-header text-center">
            <h2>Login</h2>
          </div>
          <div class="card-body">
            <form @submit.prevent="login">
              <div class="mb-3">
                <label for="username" class="form-label">Username</label>
                <input type="text" class="form-control" id="username" v-model="username" required>
              </div>
              <div class="mb-3">
                <label for="password" class="form-label">Password</label>
                <input type="password" class="form-control" id="password" v-model="password" required>
              </div>
              <button type="submit" class="btn btn-primary w-100">Login</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    async login() {
      try {
        console.log('Iniciando sesión con:', this.username, this.password)
        const response = await axios.post('http://localhost:5000/auth/login', {
          username: this.username,
          password: this.password
        })
        console.log('Respuesta del servidor:', response.data) // Verificar la respuesta del servidor
        const token = response.data.access_token
        if (token) {
          localStorage.setItem('token', token)
          console.log('Token almacenado:', token)
          this.$router.push('/sites') // Redirigir a la vista de sitios turísticos
        } else {
          console.error('Token no recibido')
        }
      } catch (error) {
        console.error('Error en la solicitud de login:', error)
      }
    }
  }
}
</script>

<style>
/* Agrega estilos personalizados si es necesario */
</style>