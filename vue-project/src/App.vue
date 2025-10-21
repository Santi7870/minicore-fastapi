<template>
  <div class="container">
    <h1>Comisiones MiniCore</h1>

    <div class="form">
      <label>Desde:</label>
      <input type="date" v-model="fechaInicio" />

      <label>Hasta:</label>
      <input type="date" v-model="fechaFin" />

      <button @click="calcularComisiones">Calcular</button>
    </div>

    <div v-if="resultado.length > 0" class="resultado">
      <h2>Resultado</h2>
      <table>
        <thead>
          <tr>
            <th>Usuario</th>
            <th>Total Ventas</th>
            <th>% Comisión</th>
            <th>Comisión</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="r in resultado" :key="r.usuario">
            <td>{{ r.usuario }}</td>
            <td>{{ r.total_ventas }}</td>
            <td>{{ (r.porcentaje_aplicado * 100).toFixed(2) }}%</td>
            <td>{{ r.comision_calculada }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const fechaInicio = ref('')
const fechaFin = ref('')
const resultado = ref([])

async function calcularComisiones() {
  if (!fechaInicio.value || !fechaFin.value) {
    alert('Debes seleccionar ambas fechas')
    return
  }

  try {
    const res = await fetch(`http://localhost:8000/comision?fecha_inicio=${fechaInicio.value}&fecha_fin=${fechaFin.value}`)
    const data = await res.json()
    resultado.value = data.resultado
  } catch (err) {
    alert('Error al conectar con el servidor')
    console.error(err)
  }
}
</script>

<style>
body {
  font-family: Arial, sans-serif;
  padding: 1rem;
}
.container {
  max-width: 800px;
  margin: auto;
}
.form {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}
th, td {
  border: 1px solid #ccc;
  padding: 0.5rem;
  text-align: center;
}
</style>
