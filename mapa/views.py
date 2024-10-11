import geopandas as gpd
import pandas as pd
import folium
from django.shortcuts import render
from django.http import HttpResponse

def mapa_view(request):
    # Leer el archivo Shapefile
    barrios_shp = gpd.read_file('mapa\BarrioVereda_2014.shp')
    barrios_shp.set_crs(epsg=4326, inplace=True)

    # Leer el CSV con los precios
    precios = pd.read_csv('arima-test\medellin_properties_with_ids.csv')
    promedio_precios = precios.groupby('neighbourhood')['price'].mean().reset_index()

    # Limpiar y normalizar los nombres para el cruce de datos
    barrios_shp['NOMBRE'] = barrios_shp['NOMBRE'].str.lower().str.strip()
    promedio_precios['neighbourhood'] = promedio_precios['neighbourhood'].str.lower().str.strip()

    # Unir los datos de precios con los polígonos de los barrios
    barrios_con_precios = barrios_shp.merge(promedio_precios, left_on='NOMBRE', right_on='neighbourhood', how='left')
    barrios_con_precios['price'].fillna(0, inplace=True)  # Reemplazar NaN por 0

    # Crear el mapa centrado en Medellín
    mapa = folium.Map(location=[6.2442, -75.5812], zoom_start=12)

    # Añadir el choropleth (mapa de calor)
    choropleth = folium.Choropleth(
        geo_data=barrios_con_precios,
        name='choropleth',
        data=barrios_con_precios,
        columns=['NOMBRE', 'price'],  
        key_on='feature.properties.NOMBRE',  
        fill_color='YlOrRd', 
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Precio Promedio de Vivienda'
    ).add_to(mapa)

    # Definir el estilo sin borde
    style_function = lambda x: {
        'fillOpacity': 0,
        'color': 'transparent', 
        'weight': 0
    }

    # Añadir los tooltips con información de los barrios y precios
    folium.GeoJson(
        barrios_con_precios,
        style_function=style_function,
        tooltip=folium.GeoJsonTooltip(
            fields=['NOMBRE', 'price'],
            aliases=['Barrio: ', 'Precio promedio: '],
            localize=True
        )
    ).add_to(mapa)

    # Convertir el mapa a HTML
    mapa_html = mapa._repr_html_()  # Este método convierte el mapa en HTML para ser usado en plantillas

    # Pasar el mapa como contexto a la plantilla
    context = {'mapa_html': mapa_html}
    return render(request, 'mapa.html', context)