import streamlit as st
import plotly.io as pio
import urllib.request
import json 
import requests
st.set_page_config(layout="wide") 

#@st.cache(suppress_st_warning=True)
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

    
    return fig

#@st.cache(suppress_st_warning=True)
def load_plotly_fig(url):
    """
    Loads Plotly Figures saved as json in a given url

    """    
    r = requests.get(url, allow_redirects=True)
    dict_json = r.json()
    figure_structure = json.dumps(dict_json)
    fig = pio.from_json(figure_structure)

    
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

st.markdown(f"<h1 style='text-align: left; color: black;'>Metropolitan Economic Trajectories</h1>", unsafe_allow_html=True)

sections = ('Territories','Population','GDP','Income', 'Technology-Based Industries', 'Knowledge-Based Services', 'S&T Personnel')
section =  st.sidebar.radio(label = 'Section', options=sections)

if section == 'Territories':
    metro = st.selectbox(label='Metropolitan Area', options=metropolitan_areas)
    fig = load_metropolitan_areas(metro=metro)
    st.plotly_chart(fig, height=600, width=1400)
elif section == 'GDP':
    json_bar_gdp = 'https://raw.githubusercontent.com/augustogeog/brazilian-metropolitan-trajectories/main/data/economy/gdp/px_bar_gdp_dynamic.json'
    fig_bar_gdp = load_plotly_fig(json_bar_gdp)
    st.plotly_chart(
        fig_bar_gdp
        )
elif section == 'Population':
    json_bar_gdp = 'https://raw.githubusercontent.com/augustogeog/brazilian-metropolitan-trajectories/main/data/pop/px_bar_pop_1970_2010_dynamic.json'
    fig_bar_pop = load_plotly_fig(json_bar_gdp)
    st.plotly_chart(
        fig_bar_pop
        )

else:
    st.markdown(f"<h2 style='text-align: left; color: black;'>Under Development</h2>", unsafe_allow_html=True)

import plotly.express as px


