<template>
  <div class="container">
    <h1>Comisiones MiniCore</h1>

    <div class="form">
      <label>Desde:</label>
      <input type="date" v-model="fechaInicio" />

      <label>Hasta:</label>
      <input type="date" v-model="fechaFin" />

      <button :disabled="cargando" @click="calcularComisiones">
        {{ cargando ? 'Calculando...' : 'Calcular' }}
      </button>
    </div>

    <p v-if="error" class="error">{{ error }}</p>

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
            <td>{{ fmtMoney(r.total_ventas) }}</td>
            <td>{{ (Number(r.porcentaje_aplicado) * 100).toFixed(2) }}%</td>
            <td>{{ fmtMoney(r.comision_calculada) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const API = import.meta.env.VITE_API_URL // <- viene de .env.production
const fechaInicio = ref('')
const fechaFin = ref('')
const resultado = ref([])
const cargando = ref(false)
const error = ref('')

const toISO = (d) => {
  // value de <input type="date"> ya viene YYYY-MM-DD en la mayoría de navegadores,
  // pero si llega dd/mm/yyyy lo convertimos.
  if (/^\d{4}-\d{2}-\d{2}$/.test(d)) return d
  const [dd, mm, yyyy] = d.split('/')
  return `${yyyy}-${mm.padStart(2, '0')}-${dd.padStart(2, '0')}`
}

const fmtMoney = (n) =>
  new Intl.NumberFormat('es-EC', { style: 'currency', currency: 'USD', maximumFractionDigits: 2 }).format(Number(n || 0))

async function calcularComisiones () {
  error.value = ''
  resultado.value = []

  if (!fechaInicio.value || !fechaFin.value) {
    error.value = 'Debes seleccionar ambas fechas'
    return
  }

  cargando.value = true
  try {
    const desde = toISO(fechaInicio.value)
    const hasta = toISO(fechaFin.value)
    const url = `${API}/comision?fecha_inicio=${desde}&fecha_fin=${hasta}`
    const res = await fetch(url)
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    const data = await res.json()
    resultado.value = data?.resultado ?? []
  } catch (e) {
    console.error(e)
    error.value = 'No se pudo conectar a la API. Revisa la URL y CORS.'
  } finally {
    cargando.value = false
  }
}
</script>

<style>
body { font-family: Arial, sans-serif; padding: 1rem; }
.container { max-width: 820px; margin: auto; }
.form { display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem; }
button[disabled] { opacity: 0.6; cursor: not-allowed; }
table { width: 100%; border-collapse: collapse; margin-top: 1rem; }
th, td { border: 1px solid #ccc; padding: 0.5rem; text-align: center; }
.error { color: #b00020; margin: 0.5rem 0; }
</style>
