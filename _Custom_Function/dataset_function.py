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
    
# 자전거 대여소 정보(통합)
def get_BikeRantalStation():
    filepath = 'G:\\내 드라이브\\DataSet\\_파킷 파일\\서울시 공공자전거 대여소 정보\\'
    filename = '공공자전거 대여소 정보_통합본_최종.parquet'
    df_BikeRantalStation = pd.read_parquet(filepath + filename)
    # df_BikeRantalStation.head()
    return df_BikeRantalStation

# 지하철역 정보(통합)
def get_TrainStation():
    filename = '_최종 병합 파일\\서울교통공사 역주소 및 전화번호\\지하철역통합_20241031.parquet'
    df_TrainStation = pd.read_parquet(path_dateset + filename)
    # df_TrainStation.head()
    return df_TrainStation


# ================================================================
# 자전거 이용량 - 연도별 자치구별 출퇴근 자전거 이용량 2018-2024(정비센터 제외).parquet
def get_gu_BikeUse():
    filepath = 'G:\\내 드라이브\\DataSet\\_파킷 파일\\_연도별 자치구별 여러변수와 자전거 이용량\\'
    filename = '연도별 자치구별 출퇴근 자전거 이용량 2018-2024(정비센터 제외).parquet'
    # start_time = time.time()
    df = pd.read_parquet(filepath + filename)
    # print("read_parquet time :", time.time() - start_time)
    return df

# 자전거도로 - 연도별 자치구별 자전거도로 2019-2024(기준연도 +1).parquet
def get_gu_BikeRoad():
    filepath = 'G:\\내 드라이브\\DataSet\\_파킷 파일\\_연도별 자치구별 여러변수와 자전거 이용량\\'
    filename = '연도별 자치구별 자전거도로 2019-2024(기준연도 +1).parquet'
    start_time = time.time()
    df = pd.read_parquet(filepath + filename)
    # print("read_parquet time :", time.time() - start_time)
    return df
    
# 자전거 대여소 수 - 연도별 자치구별 대여소 및 거치대수 2020-2024(기준연도 +1).parquet
def get_gu_BikeRental():
    filepath = 'G:\\내 드라이브\\DataSet\\_파킷 파일\\_연도별 자치구별 여러변수와 자전거 이용량\\'
    filename = '연도별 자치구별 대여소 및 거치대수 2020-2024(기준연도 +1).parquet'
    start_time = time.time()
    df = pd.read_parquet(filepath + filename)
    # print("read_parquet time :", time.time() - start_time)
    return df
    
# 인구밀도 - 연도별 자치구별 인구밀도 2019-2023.parquet
def get_gu_PeopleDensity():
    filepath = 'G:\\내 드라이브\\DataSet\\_파킷 파일\\_연도별 자치구별 여러변수와 자전거 이용량\\'
    filename = '연도별 자치구별 인구밀도 2019-2023.parquet'
    start_time = time.time()
    df = pd.read_parquet(filepath + filename)
    # print("read_parquet time :", time.time() - start_time)
    return df
        
# 출/퇴근 인원 밀집도(유동인구) - 연도별 자치구별 출퇴근 이동인구 2020-2024.parquet
def get_gu_PeopleMove():
    filepath = 'G:\\내 드라이브\\DataSet\\_파킷 파일\\_연도별 자치구별 여러변수와 자전거 이용량\\'
    filename = '연도별 자치구별 출퇴근 이동인구 2020-2024.parquet'
    start_time = time.time()
    df = pd.read_parquet(filepath + filename)
    # print("read_parquet time :", time.time() - start_time)
    return df

# 연도별 자치구별 출퇴근 평균 이동인구 - 연도별 자치구별 출퇴근 평균 이동인구 2020-2024.parquet
def get_gu_PeopleMove_Mean():
    filepath = 'G:\\내 드라이브\\DataSet\\_파킷 파일\\_연도별 자치구별 여러변수와 자전거 이용량\\'
    filename = '연도별 자치구별 출퇴근 평균 이동인구 2020-2024.parquet'
    start_time = time.time()
    df = pd.read_parquet(filepath + filename)
    # print("read_parquet time :", time.time() - start_time)
    return df
    
# 지하철역 인근여부 - 연도별 자치구별 대여소-지하철역 최단거리 펑균 2021-2024(기준연도 +1).parquet
def get_gu_NearTrainStatin():
    filepath = 'G:\\내 드라이브\\DataSet\\_파킷 파일\\_연도별 자치구별 여러변수와 자전거 이용량\\'
    filename = '연도별 자치구별 대여소-지하철역 최단거리 펑균 2021-2024(기준연도 +1).parquet'
    start_time = time.time()
    df = pd.read_parquet(filepath + filename)
    # print("read_parquet time :", time.time() - start_time)
    return df
    
# 차량통행속도 - 연도별 자치구별 평균 차량통행속도 2020-2024.parquet
def get_gu_VehiSpeed():
    filepath = 'G:\\내 드라이브\\DataSet\\_파킷 파일\\_연도별 자치구별 여러변수와 자전거 이용량\\'
    filename = '연도별 자치구별 평균 차량통행속도 2020-2024.parquet'
    start_time = time.time()
    df = pd.read_parquet(filepath + filename)
    # print("read_parquet time :", time.time() - start_time)
    return df
    
# 유가(기름 가격) - 연도별 자치구별 평균 유가 2021-2024.parquet
def get_gu_OilPrice():
    filepath = 'G:\\내 드라이브\\DataSet\\_파킷 파일\\_연도별 자치구별 여러변수와 자전거 이용량\\'
    filename = '연도별 자치구별 평균 유가 2021-2024.parquet'
    start_time = time.time()
    df = pd.read_parquet(filepath + filename)
    # print("read_parquet time :", time.time() - start_time)
    return df

# ======================================================================

# 서울특별시 공공자전거 대여이력 정보(이용량top50)
def get_RentalHistory_use_top50():
    rental = get_BikeRantalStation()
    
    # 데이터 불러오기
    filepath = 'G:\\내 드라이브\\DataSet\\_파킷 파일\\서울특별시 공공자전거 대여이력 정보\\'
    filename = '서울특별시 공공자전거 대여이력 정보_2023_preprocessed.parquet'
    start_time = time.time()
    df = pd.read_parquet(filepath + filename)
    # print("read_parquet time :", time.time() - start_time)
    # df.head(5)
    
    # 대여대여수 count
    df_rent = df.groupby(['대여대여소번호']).agg({
            '자전거번호': 'count'  # count를 이용해 이용량 계산
        }).rename(columns={'자전거번호': '대여수'}).reset_index()
    df_rent = df_rent.rename(columns={'대여대여소번호': '대여소번호'})
    # df_rent
    
    # 반납대여수 count
    df_return = df.groupby(['반납대여소번호']).agg({
            '자전거번호': 'count'  # count를 이용해 이용량 계산
        }).rename(columns={'자전거번호': '반납수'}).reset_index()
    df_return = df_return.rename(columns={'반납대여소번호': '대여소번호'})
    # df_return
    
    # 대여수와 반납수 데이터프레임 합치기
    use = pd.merge(df_rent, df_return, on='대여소번호', how='left')
    # use
    
    ## 대여수와 반납수 합쳐서 총이용량 구하기
    use['총이용량'] = use['대여수'] + use['반납수']
    # use
    
    lowest_usage_53 = use.nsmallest(53, '총이용량')
    # lowest_usage_53
    
    merge = pd.merge(lowest_usage_53, rental, on='대여소번호', how='left')
    # merge
    
    # 첫번째(09979), 두번째(04339), 사십구번째(09980)로 이용량 적은 대여소. 대여소 정보 없음. 2024년 6월 대여소 정보에 없음.
    # 따라서 대여소가 사라졌으므로 제외함
    merge_2 = merge.drop(index=[0, 1, 49])
    merge_2.reset_index()
    return merge_2

# 출근대여 퇴근반납 차
def get_BikeEmpty():
    _year='2023'
    filepath = 'G:\\내 드라이브\\DataSet\\_파킷 파일\\서울특별시 공공자전거 대여이력 정보\\'
    filename = '출퇴근대여반납차이_' + _year + '.parquet'
    start_time = time.time()
    df_BikeEmpty = pd.read_parquet(filepath + filename)
    df_BikeEmpty['퇴근반납수-출근대여수'] = df_BikeEmpty['퇴근반납수'] - df_BikeEmpty['출근대여수']
    # top_20 = df.nlargest(20, '퇴근반납수-출근대여수')
    
    # print("read_parquet time :", time.time() - start_time)
    # df_BikeEmpty.head(5)
    return df_BikeEmpty
