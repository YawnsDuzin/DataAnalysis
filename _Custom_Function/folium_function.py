# 기본 라이브러리 임포트
import os
import numpy as np
import pandas as pd
import chardet
import json
import folium

# 사용자 정의함수 경로 설정
import sys
sys.path.append("G:/내 드라이브/Source/_Custom_Function")
# 사용자 정의함수 불러오기

import time

import ExcelFile_Merge as em
import ExcelFile_Read as er
import ExcelFile_EDA as ee

# 나의 루트 경로 설정
path_dateset = 'G:/내 드라이브/DataSet/'

# 자치구 정보 (geojson)
def seoul_municipalities_geo_simple():
    geo_path = path_dateset + 'seoul_municipalities_geo_simple.json'
    # encoding을 UTF-8로 지정
    with open(geo_path, 'rt', encoding='utf-8') as f:
        geo_str2 = json.load(f)
    return geo_str2

# 2024.11.13 duzin
def get_seoul_bike_road_geo():
    geo_path = path_dateset + '_최종 병합 파일\\서울시 자전거 도로 데이터\\' + 'ddareng_road.geojson'
    # geo_str = json.load(open(geo_path, encoding='cp949'))
    # encoding을 UTF-8로 지정
    with open(geo_path, 'rt', encoding='utf-8') as f:
        geo_str = json.load(f)
    return geo_str


# 지도에 자치구 이름 표시관련 - 위도/경도 정리
dic_gus = {
    '송파구': [37.5046, 127.1187],
    '강서구': [37.5642, 126.8255],
    '강남구': [37.4915, 127.0624],
    '영등포구': [37.5244, 126.9031],
    '노원구': [37.6518, 127.0737],
    '서초구': [37.4841, 127.0126],
    '마포구': [37.5568, 126.9082],
    '강동구': [37.5527, 127.1448],
    '구로구': [37.4967, 126.8454],
    '양천구': [37.5214, 126.8595],
    '종로구': [37.5949, 126.9676],
    '중랑구': [37.5971, 127.0912],
    '은평구': [37.6205, 126.9257],
    '중구': [37.5601, 126.9985],
    '성동구': [37.5511, 127.0366],
    '동대문구': [37.5840, 127.0514],
    '용산구': [37.5348, 126.9793],
    '광진구': [37.5484, 127.0854],
    '서대문구': [37.5810, 126.9378],
    '성북구': [37.6044, 127.0147],
    '관악구': [37.4689, 126.9470],
    '도봉구': [37.6716, 127.0322],
    '금천구': [37.4640, 126.9020],
    '동작구': [37.5048, 126.9508],
    '강북구': [37.6382, 127.0116]
}



# 2024.11.13 duzin
# GeoJson 스타일 함수 정의
def _style_function(feature):
    return {
        'color': feature['properties'].get('LINE_COLOR', '#3388ff'),  # 기본 색상은 파란색
        #'weight': feature['properties'].get('LINE_WEIGHT', 1),       # 기본 굵기는 2
        'weight': 2,       # 기본 굵기는 2
        'opacity': 0.7
    }
        
_popup_bike_load = folium.GeoJsonPopup(
    fields=["CONTENTS_NAME", "ADDR_NEW"],
    aliases=["CONTENTS_NAME", "ADDR_NEW"],
    localize=True,
    labels=True,
    style="background-color: yellow;",
)
_tooltip_bike_load = folium.GeoJsonTooltip(
    fields=["CONTENTS_NAME", "SUB_NAME"],
    aliases=["CONTENTS_NAME:", "SUB_NAME"],
    localize=True,
    sticky=False,
    labels=True,
    style="""
        background-color: #F0EFEF;
        border: 2px solid black;
        border-radius: 3px;
        box-shadow: 3px;
    """,
    max_width=800,
)
def folium_bike_load(_map, _name, _show = True):
    fg0 = folium.FeatureGroup(name=_name, show=False).add_to(_map)
    # 자전거 도로 표시
    # GeoJSON 파일을 불러와 스타일 적용
    folium.GeoJson(
        get_seoul_bike_road_geo(),
        style_function=_style_function,
        name=_name,
        popup=_popup_bike_load,
        tooltip=_tooltip_bike_load,        
    ).add_to(fg0)


# data의 _column_grb별 _column_val의 합계값 형식으로 변환하여 리턴
def gu_group(_data, _column_grb, _column_val):
    return _data.groupby(_column_grb)[_column_val].sum()

# folium지도에 Circle 시각화
def folium_Circle(_data, _name, _map, _show = True, _radius = 100, _color = 'black', _fill = False, _fill_color = 'blue', _fill_opacity = 0.6, _popup = '', tooltip = ''):
    fg1 = folium.FeatureGroup(name=_name, show=_show).add_to(_map)
    # 자전거 대여소 표시
    for i, row in _data.iterrows():
        folium.Circle(
          location = [row['위도'], row['경도']],
          radius = 100,
          color='black',                  # 외곽선 색상
          fill=False,                     # 채우기 여부
          fill_color='blue',             # 채우기 색상
          fill_opacity=0.6,              # 채우기 불투명도
          popup=row[_popup],             # 클릭 시 표시되는 팝업
          tooltip=row[tooltip],                 # 마우스 오버 시 표시되는 툴팁
      ).add_to(fg1)

# folium지도에 CircleMarker 시각화
def folium_CircleMarker(_data, _name, _map, _show = True, _radius = 2, _color = 'purple', _fill = True, _fill_color = 'purple', _fill_opacity = 0.6, _popup = '', tooltip = ''):
    fg3 = folium.FeatureGroup(name=_name, show=_show).add_to(_map)
    # 버스정류장 표시
    for i, row in _data.iterrows():
      folium.CircleMarker(
          location = [row['위도'], row['경도']],
          # radius=2,                     # 반지름 (픽셀 단위)
          # color='purple',                  # 외곽선 색상
          # fill=True,                     # 채우기 여부
          # fill_color='purple',             # 채우기 색상
          # fill_opacity=0.6,              # 채우기 불투명도
          # popup=row['정류소명'],             # 클릭 시 표시되는 팝업
          # tooltip=row['정류소명']                 # 마우스 오버 시 표시되는 툴팁
          radius=_radius,                     # 반지름 (픽셀 단위)
          color=_color,                  # 외곽선 색상
          fill=_fill,                     # 채우기 여부
          fill_color=_fill_color,             # 채우기 색상
          fill_opacity=_fill_opacity,              # 채우기 불투명도
          popup=row[_popup],             # 클릭 시 표시되는 팝업
          tooltip=row[tooltip]                 # 마우스 오버 시 표시되는 툴팁  
      ).add_to(fg3)


# folium지도 시각화 관련 - 자치구별 밀도 표시
def folium_gu_density(_geo_data, _data, _name, _fill_color = 'Blues', fill_opacity = 0.7, _columns = None):
    choropleth = folium.Choropleth(geo_data = _geo_data,
                  data = _data,
                  columns=_columns,
                  name = _name,
                  key_on = 'feature.properties.SIG_KOR_NM',
                  fill_color = _fill_color,
                  fill_opacity=fill_opacity              # 채우기 불투명도
                )
    return choropleth

# folium지도 시각화 관련 - 자치구별 밀도 표시
def folium_gu_density(_geo_data, _data, _name, _fill_color = 'Blues', fill_opacity = 0.7):
    choropleth = folium.Choropleth(geo_data = _geo_data,
                  data = _data,
                  name = _name,
                  key_on = 'feature.properties.SIG_KOR_NM',
                  fill_color = _fill_color,
                  fill_opacity=fill_opacity              # 채우기 불투명도
                )
    return choropleth

# folium지도 시각화 관련 - 자치구별 이름 표시
def folium_gu_name(_name, _map, _show = True):
    fg1 = folium.FeatureGroup(name=_name, show=_show).add_to(_map)
    for _gu, _location in dic_gus.items():
        folium.Marker(
            location=_location,
            popup=_gu,
            name = _name,
            icon=folium.DivIcon(html=f"<div style='font-size: 7pt; color: black; font-family: Arial; font-weight: bold;'>{_gu}</div>")
        ).add_to(fg1)

# folium지도 시각화 관련 - 각 구의 중심에, 자치구별 합계 표시
def folium_gu_display_sum(_data, _name, _map, _show = True):
    fg2 = folium.FeatureGroup(name=_name, show=_show).add_to(_map)
    for idx, val in zip(_data.index, _data.values):
        folium.Marker(
            location=[dic_gus[idx][0] + 0.0055, dic_gus[idx][1]],
            popup=val,
            icon=folium.DivIcon(html=f"<div style='font-size: 7pt; color: black; font-family: Arial; font-weight: bold;'>{val}</div>")
        ).add_to(fg2)

# folium지도 시각화 관련 - 각 구의 중심에, 자치구별 비율 표시
def folium_gu_display_per(_data, _name, _map, _show = True):
    total_data = _data.sum()
    # 각 자치구의 대여수를 비율로 변환
    Per_data = round((_data / total_data) * 100, 2)

    fg3 = folium.FeatureGroup(name=_name, show=_show).add_to(_map)
    for idx, val in zip(Per_data.index, Per_data.values):
        folium.Marker(
            location=[dic_gus[idx][0] + 0.003, dic_gus[idx][1]],
            popup=val,
            icon=folium.DivIcon(html=f"<div style='font-size: 7pt; color: black; font-family: Arial; font-weight: bold;'>{val}</div>")
        ).add_to(fg3)

# folium지도 시각화 관련 - 각 구의 중심에, 랭킹 표시
def folium_gu_display_rank(_data, _name, _map, _show = True):
    fg2 = folium.FeatureGroup(name=_name, show=_show).add_to(_map)
    cnt = 1
    for idx, val in zip(_data.index, _data.values):
        folium.Marker(
            location=[dic_gus[idx][0] + 0.0055, dic_gus[idx][1]],
            popup=cnt,
            icon=folium.DivIcon(html=f"<div style='font-size: 7pt; color: black; font-family: Arial; font-weight: bold;'>{cnt}</div>")
        ).add_to(fg2)
        cnt = cnt + 1

