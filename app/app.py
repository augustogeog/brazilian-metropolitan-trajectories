import streamlit as st
import plotly.io as pio
import urllib.request
import json 
import requests
st.set_page_config(layout="wide") 

@st.cache(suppress_st_warning=True)
def load_metropolitan_areas(metro='Curitiba'):
    """
    Loads Plotly mapbox figures of selected metropolitan areas
    """
    dict_metro = {
        'Manaus':'manaus'
        , 'Belém':'belem'
        , 'Fortaleza':'fortaleza'
        , 'Recife':'recife'
        , 'Salvador':'salvador'
        , 'Belo Horizonte':'belo_horizonte'
        , 'Vitória':'vitoria'
        , 'Rio de Janeiro':'rio_de_janeiro'
        , 'São Paulo':'sao_paulo'
        , 'Campinas':'campinas'
        , 'Curitiba':'curitiba'
        , 'Florianópolis':'florianópolis'
        , 'Porto Alegre':'porto_Alegre'
        , 'Goiânia':'goiania'
        , 'Brasília':'brasília'
        }

    url = f'https://raw.githubusercontent.com/augustogeog/brazilian-metropolitan-trajectories/main/data/territory/json/plotly_fig/{dict_metro[metro]}.json'
    
    r = requests.get(url, allow_redirects=True)
    dict_json = r.json()
    
    figure_structure = json.dumps(dict_json)
    
    fig = pio.from_json(figure_structure)

#    r = requests.get(url, allow_redirects=True)
#    with urllib.request.urlopen(') as url:
#        data = json.loads(url
#            url.read().decode()
#            )
    
#    fig = pio.read_json(file)


    return fig


metropolitan_areas = (
    'Manaus'
    , 'Belém'
    , 'Fortaleza'
    , 'Recife'
    , 'Salvador'
    , 'Belo Horizonte'
    , 'Vitória'
    , 'Rio de Janeiro'
    , 'São Paulo'
    , 'Campinas'
    , 'Curitiba'
    , 'Florianópolis'
    , 'Porto Alegre'
    , 'Goiânia'
    , 'Brasília'
    )

st.markdown(
    f"<h1 style='text-align: left; color: black;'>Metropolitan Economic Trajectories</h1>", unsafe_allow_html=True
)

metro = st.selectbox(label='Metropolitan Area', options=metropolitan_areas)
fig = load_metropolitan_areas(metro=metro)
st.plotly_chart(fig)