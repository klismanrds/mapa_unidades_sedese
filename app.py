import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="Mapa Uberlândia-MG", layout="wide")
st.markdown("""
	<style>
		body {margin:0;}
		.block-container {padding-top:0; padding-bottom:0;}
		.main {padding:0;}
		.centered-content {display: flex; flex-direction: column; align-items: center; justify-content: center;}
		.stSelectbox, .stMarkdown, .stTitle {text-align: center !important;}
	</style>
""", unsafe_allow_html=True)

st.markdown('<div class="centered-content">', unsafe_allow_html=True)
st.title("Unidades de Uberlândia - MG")

st.markdown("<span style='font-size:20px;'>Centros Profissionalizantes, NAICAs, CRAS e CEAI</span>", unsafe_allow_html=True)

# Legenda de tipos e cores em linha única
st.markdown("""
<div style='margin: 20px 0; display: flex; align-items: center; justify-content: center; gap: 30px; font-size: 16px;'>
	<b>Legenda:</b>
	<span style='color:blue; font-weight:bold;'>■</span> Centro Profissionalizante
	<span style='color:green; font-weight:bold;'>■</span> NAICA
	<span style='color:red; font-weight:bold;'>■</span> CRAS
	<span style='color:purple; font-weight:bold;'>■</span> CEAI
</div>
""", unsafe_allow_html=True)

# Definições de cor para cada tipo
tipo_cores = {
    "Centro Profissionalizante": "blue",
    "NAICA": "green",
    "CRAS": "red",
    "CEAI": "purple"
}

# Lista de pontos (exemplo, pode ser expandida)
points = [
    {"nome": "Centro Profissionalizante Luizote", "tipo": "Centro Profissionalizante", "coords": (-18.91481, -48.33148), "regiao": "Oeste"},
    {"nome": "Centro Profissionalizante Morumbi", "tipo": "Centro Profissionalizante", "coords": (-18.9115, -48.3212), "regiao": "Oeste"},
    {"nome": "Centro Profissionalizante Lagoinha", "tipo": "Centro Profissionalizante", "coords": (-18.8955, -48.2772), "regiao": "Norte"},
    {"nome": "Centro Profissionalizante Campo Alegre", "tipo": "Centro Profissionalizante", "coords": (-18.8855, -48.2442), "regiao": "Leste"},
    {"nome": "Centro Profissionalizante Tocantins", "tipo": "Centro Profissionalizante", "coords": (-18.9005, -48.2102), "regiao": "Leste"},
    {"nome": "Centro Profissionalizante Planalto", "tipo": "Centro Profissionalizante", "coords": (-18.9305, -48.2502), "regiao": "Sul"},
    {"nome": "Centro Profissionalizante Maravilha", "tipo": "Centro Profissionalizante", "coords": (-18.9405, -48.2702), "regiao": "Sul"},
    {"nome": "NAICA Jardim Canaã", "tipo": "NAICA", "coords": (-18.8850, -48.2550), "regiao": "Leste"},
    {"nome": "CRAS Morumbi", "tipo": "CRAS", "coords": (-18.9110, -48.3200), "regiao": "Oeste"},
    {"nome": "CRAS Campo Alegre", "tipo": "CRAS", "coords": (-18.8855, -48.2442), "regiao": "Leste"},
    {"nome": "CRAS Custódio Pereira", "tipo": "CRAS", "coords": (-18.9000, -48.2200), "regiao": "Leste"},
    {"nome": "CRAS Jardim Brasília", "tipo": "CRAS", "coords": (-18.9000, -48.2300), "regiao": "Leste"},
    {"nome": "CRAS Marta Helena", "tipo": "CRAS", "coords": (-18.9000, -48.2400), "regiao": "Norte"},
    {"nome": "CEAI Luizote", "tipo": "CEAI", "coords": (-18.91481, -48.33148), "regiao": "Oeste"},
    {"nome": "CEAI Rondon", "tipo": "CEAI", "coords": (-18.9000, -48.2500), "regiao": "Sul"},
    {"nome": "CEAI Guarani", "tipo": "CEAI", "coords": (-18.9200, -48.2600), "regiao": "Sul"},
    {"nome": "CEAI Laranjeiras", "tipo": "CEAI", "coords": (-18.9300, -48.2700), "regiao": "Sul"},
]

# Opções de filtro
tipos = sorted(set(p["tipo"] for p in points))
regioes = sorted(set(p["regiao"] for p in points))

with st.sidebar:
	st.header("Filtros")
	tipo_selecionado = st.selectbox("Filtrar por tipo de ponto", ["Todos"] + tipos)
	regiao_selecionada = st.selectbox("Filtrar por região", ["Todas"] + regioes)

# Filtragem dos pontos
def filtrar_pontos(points, tipo, regiao):
	filtrados = points
	if tipo != "Todos":
		filtrados = [p for p in filtrados if p["tipo"] == tipo]
	if regiao != "Todas":
		filtrados = [p for p in filtrados if p["regiao"] == regiao]
	return filtrados

pontos_filtrados = filtrar_pontos(points, tipo_selecionado, regiao_selecionada)


# Cria o mapa centralizado em Uberlândia
mapa = folium.Map(location=[-18.9146, -48.2755], zoom_start=13)

# Coordenadas aproximadas do perímetro do Parque Trianon
trianon_coords = [
	(-18.9005, -48.2550),  # Av. Olímpio de Freitas
	(-18.9005, -48.2500),  # Av. Paulo Firmino
	(-18.9025, -48.2500),  # R. do Poe
	(-18.9025, -48.2550),  # Av. Palestina
	(-18.9005, -48.2550)   # Fechando o polígono
]


# Adiciona marcadores filtrados
for ponto in pontos_filtrados:
	folium.Marker(
		location=ponto["coords"],
		popup=f"{ponto['nome']} ({ponto['tipo']})",
		icon=folium.Icon(color=tipo_cores.get(ponto["tipo"], "gray"), icon="info-sign")
	).add_to(mapa)

st_folium(mapa, width=1200, height=800)
st.markdown('</div>', unsafe_allow_html=True)
