<!-- src/views/TouristSitesView.vue -->
<template>
  <div class="container mt-5">
    <h2>Administrar Sitios Turísticos</h2>
    <button class="btn btn-primary mb-3" @click="showAddForm = true">Agregar Sitio Turístico</button>
    
    <div v-if="showAddForm">
      <h3>Agregar Sitio Turístico</h3>
      <form @submit.prevent="addSite">
        <div class="mb-3">
          <label for="name" class="form-label">Nombre</label>
          <input type="text" class="form-control" id="name" v-model="newSite.name" required>
        </div>
        <div class="mb-3">
          <label for="description" class="form-label">Descripción</label>
          <input type="text" class="form-control" id="description" v-model="newSite.description" required>
        </div>
        <button type="submit" class="btn btn-success">Agregar</button>
        <button type="button" class="btn btn-secondary" @click="showAddForm = false">Cancelar</button>
      </form>
    </div>

    <div v-if="showEditForm">
      <h3>Editar Sitio Turístico</h3>
      <form @submit.prevent="updateSite">
        <div class="mb-3">
          <label for="editName" class="form-label">Nombre</label>
          <input type="text" class="form-control" id="editName" v-model="editSite.name" required>
        </div>
        <div class="mb-3">
          <label for="editDescription" class="form-label">Descripción</label>
          <input type="text" class="form-control" id="editDescription" v-model="editSite.description" required>
        </div>
        <button type="submit" class="btn btn-success">Actualizar</button>
        <button type="button" class="btn btn-secondary" @click="showEditForm = false">Cancelar</button>
      </form>
    </div>

    <div v-if="sites.length">
      <h3>Lista de Sitios Turísticos</h3>
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Descripción</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="site in sites" :key="site.id">
            <td>{{ site.name }}</td>
            <td>{{ site.description }}</td>
            <td>
              <button class="btn btn-warning" @click="editSiteForm(site)">Editar</button>
              &nbsp;
              
              <button class="btn btn-danger" @click="deleteSite(site.id)">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showAddForm: false,
      showEditForm: false,
      newSite: {
        name: '',
        description: ''
      },
      editSite: {
        id: null,
        name: '',
        description: ''
      },
      sites: []
    };
  },
  methods: {
    addSite() {
      if (this.newSite.name && this.newSite.description) {
        this.sites.push({ ...this.newSite, id: Date.now() });
        this.newSite.name = '';
        this.newSite.description = '';
        this.showAddForm = false;
      }
    },
    editSiteForm(site) {
      this.editSite = { ...site };
      this.showEditForm = true;
    },
    updateSite() {
      const index = this.sites.findIndex(site => site.id === this.editSite.id);
      if (index !== -1) {
        this.sites.splice(index, 1, this.editSite);
        this.showEditForm = false;
      }
    },
    deleteSite(id) {
      this.sites = this.sites.filter(site => site.id !== id);
    }
  }
};
</script>

<style scoped>
/* Agregar estilos personalizados aquí */
</style>