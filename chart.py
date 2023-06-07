import pandas as pd
import os
import streamlit as st
import streamlit.components.v1 as components

data = pd.read_csv('cleaned_data.csv')
data['Stream'] = data['Stream'].str.split().str[-1]
import plotly.express as px
fig = px.sunburst(data, path=['Stream','Building'], values='Weight',color='Stream',
                  color_discrete_map={'Landfill':'#cacbcc', 'Compost':'#8dd08a', 'Recycling':'#2cb4f8'})
fig.update_traces(hovertemplate="<b>Total Weight in lbs: %{value}</b>")
fig.update_layout(
    width=800,
    height=600,
    showlegend=True,
    title="Waste Distribution by Buildings",
    title_x=0.1,
    title_y=0.97,
    template='plotly_white',
    title_font=dict(size=30,family='Balto'),
)

tab1, tab2 = st.tabs(["Description", "Chart"])
with tab1:
    p = open("base.html")
    components.html(p.read())
    st.title("Waste Management Across Various SCU Buildings: A Visual Exploration")
    st.title("About the Assignment")
    st.write(
        "Upon examining the dataset, I initially found it unclear what insights could be derived from it. However, upon closer inspection, I discovered that it contained information about the waste generated at SCU (Santa Clara University). My initial intention was to analyze which event produced the highest amount of waste. Unfortunately, I noticed that the dataset did not include any information about the specific event associated with the waste collection. As a result, I shifted my focus and realized that there might be an intriguing pattern in the distribution of waste streams throughout the campus.I have cleaned the data and used that dataset. I have added that cleaned dataset to the zipfile.When you hover over a sector in the chart, it displays the total weight of waste associated with that particular combination of stream and building.")
    st.title("Project Display")
    st.write(
        "It uses this data to generate a 'SUNBURST CHART', where the waste streams and buildings are organized in a hierarchical structure.")
    st.write(
        "The size of each sector in the chart represents the weight of waste associated with that particular combination of stream and building.")
    st.write(
        "The circular layout of the sunburst visually conveys the proportions and relationships between waste types and buildings.")
    st.title("Size and Color")
    st.write(
        "The size of the visualization is set to 1100x850 pixels to provide a spacious canvas for the chart and ensure optimal visibility of the data.")
    st.write(
        "Color plays a crucial role in conveying information effectively. In this visualization, I have used a specific color scheme to represent each waste type: ")
    st.markdown("Landfill: #cacbcc (a light gray shade)")
    st.markdown("Compost: #8dd08a (a green shade)")
    st.markdown("Recycling: #2cb4f8 (a blue shade)")
    st.title("Other Visual Elements")
    st.write("To improve the user experience, I have incorporated interactive features: ")
    st.markdown("Hover Information: When users hover over a specific segment, a tooltip displays the total weight of waste for that particular waste type and building. ")
    st.markdown("Legend: A legend is included to provide a clear understanding of the color coding for each waste type. ")



with tab2:
    st.plotly_chart(fig, use_container_width=False)
