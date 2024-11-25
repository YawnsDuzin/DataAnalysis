# 기본 라이브러리 임포트
import os
import numpy as np
import pandas as pd
import chardet
import json
import folium

import matplotlib.pyplot as plt
import seaborn as sns

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

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows의 경우
plt.rcParams['axes.unicode_minus'] = False  # 한글 폰트 사용 시, 마이너스 기호 깨짐 방지

# 1개의 bar plot을 그립니다.
def plot_single_bar(_data, _groub1, _val):
    # 데이터 준비
    data = pd.DataFrame(_data[[_groub1, _val]])
    # 그래프 그리기
    plt.figure(figsize=(12, 6))
    plt.bar(_data[_groub1], _data[_val])
    
    # 그래프 제목과 축 레이블 추가
    plt.title(_groub1 + "별 " + _val)
    plt.xlabel(_groub1)
    plt.ylabel(_val)
    
    # x축 레이블 각도 조정
    plt.xticks(rotation=45)
    plt.grid(True)
    
    # 그래프 표시
    plt.show()


# 1개의 plot을 그립니다.
def plot_single_plot(_data, _groub1, _val):
    # 데이터 준비
    data = pd.DataFrame(_data[[_groub1, _val]])
    # 그래프 그리기
    plt.figure(figsize=(12, 6))
    plt.plot(data[_groub1], data[_val], marker='o', linestyle='-', color='b')
    
    # 그래프 제목과 축 레이블 추가
    plt.title(_groub1 + "별 " + _val)
    plt.xlabel(_groub1)
    plt.ylabel(_val)
    
    # x축 레이블 각도 조정
    plt.xticks(rotation=45)
    # plt.grid(True)
    
    # 그래프 표시
    plt.show()


# 여러 개의 plot을 그립니다.
def plot_groub_multi_plot(_data, _groub1, _groub2, _val):
    # 그래프 스타일 설정
    plt.figure(figsize=(15, 8))
    
    # 연도별로 그룹화하여 각 자치구의 운용수량 꺾은선 그래프 생성
    for year, group in _data.groupby(_groub1):
        plt.plot(group[_groub2], group[_val], label=str(year), marker='o')
    
    # 그래프 제목 및 축 레이블 설정
    plt.title(_groub2 + '별 ' + _groub1 + '별 ' + _val + ' 변화')
    plt.xlabel(_groub2)
    plt.ylabel(_val)
    plt.xticks(rotation=45)
    plt.legend(title=_groub1, loc='upper left')
    plt.grid(visible=True, linestyle='--', alpha=0.5)
    
    # 그래프 표시
    plt.tight_layout()
    plt.show()
