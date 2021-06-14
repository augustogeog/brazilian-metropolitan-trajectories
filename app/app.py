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
    'Belo Horizonte'
    , 'Belém'
    , 'Brasília'
    , 'Campinas'
    , 'Curitiba'
    , 'Florianópolis'
    , 'Fortaleza'
    , 'Goiânia'
    , 'Manaus'
    , 'Porto Alegre'
    , 'Recife'
    , 'Rio de Janeiro'
    , 'Salvador'
    , 'São Paulo' 
    , 'Vitória'
    )

st.markdown(f"<h1 style='text-align: left; color: black;'>Metropolitan Economic Trajectories</h1>", unsafe_allow_html=True)

sections = ('Territories','Population','GDP','Income', 'Technology-Based Industries', 'Knowledge-Based Services', 'S&T Personnel')
section =  st.sidebar.radio(label = 'Section', options=sections)

if section == 'Territories':
    metro = st.selectbox(label='Metropolitan Area', options=metropolitan_areas)
    fig = load_metropolitan_areas(metro=metro)
    st.plotly_chart(fig, height=600, width=1400, use_container_width=True)
elif section == 'GDP':
    data_type =  st.radio(label = 'Data', options=['GDP', 'GDP per capita'])
    if data_type == 'GDP':    
        json_bar_gdp = 'https://raw.githubusercontent.com/augustogeog/brazilian-metropolitan-trajectories/main/data/economy/gdp/px_bar_gdp_02_18_dynamic.json'
        fig_bar_gdp = load_plotly_fig(json_bar_gdp)
        st.plotly_chart(fig_bar_gdp, use_container_width=True)
    else:
        json_bar_gdp = 'https://raw.githubusercontent.com/augustogeog/brazilian-metropolitan-trajectories/main/data/economy/gdp/px_bar_gdppercapita_02_18_dynamic.json'
        fig_bar_gdp = load_plotly_fig(json_bar_gdp)
        st.plotly_chart(fig_bar_gdp, use_container_width=True)

elif section == 'Population':
    plot_type =  st.radio(label = 'Plot Type', options=['Dynamic Bar', 'Line'])

    if plot_type == 'Dynamic Bar':
        json_bar_pop = 'https://raw.githubusercontent.com/augustogeog/brazilian-metropolitan-trajectories/main/data/pop/px_bar_pop_70_18_dynamic.json'
        fig_bar_pop = load_plotly_fig(json_bar_pop)
        st.plotly_chart(fig_bar_pop,use_container_width=True, height=300, width=700)
    else:
        json_line_pop = 'https://raw.githubusercontent.com/augustogeog/brazilian-metropolitan-trajectories/main/data/pop/line_pop_70_18.json' 
        fig_line_pop = load_plotly_fig(json_line_pop)
        st.plotly_chart(fig_line_pop,use_container_width=True
        , height=300
        , width=600
        )
elif section == 'Income':
    plot_type =  st.radio(label = 'Plot Type', options=['Dynamic Bar', 'Line'])

    if plot_type == 'Dynamic Bar':
        json_bar_income = 'https://raw.githubusercontent.com/augustogeog/brazilian-metropolitan-trajectories/main/data/economy/income/fig_dynamic_bar_percapita_income.json' 
        fig_bar_income = load_plotly_fig(json_bar_income)
        st.plotly_chart(fig_bar_income,use_container_width=True, height=300, width=600)

    else:
        json_line_income = 'https://raw.githubusercontent.com/augustogeog/brazilian-metropolitan-trajectories/main/data/economy/income/fig_line_percapita_income.json'
        fig_line_income = load_plotly_fig(json_line_income)
        st.plotly_chart(fig_line_income,use_container_width=True, height=300, width=700)



else:
    st.markdown(f"<h2 style='text-align: left; color: black;'>Under Development</h2>", unsafe_allow_html=True)

import plotly.express as px


