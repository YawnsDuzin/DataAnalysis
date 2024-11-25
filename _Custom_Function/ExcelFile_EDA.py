import datetime
import pandas as pd

# 날짜 형식이 맞는지 확인
def ss_validate_date(date_text):
	try:
		datetime.datetime.strptime(date_text,"%Y-%m-%d")
		return True
	except ValueError:
		#print("Incorrect data format({0}), should be YYYY-MM-DD".format(date_text))
		return False

# 증감률 계산
# - v1 : 이전 값
# - v2 : 이후 값
def ss_compare(v1, v2):
    if (v1 < v2).any(): #증가율계산 
        try: value = round(((v2 - v1) / v1) * 100,2)    # v1 < v2 일 때 얼마나 증가했는지 %
        except: value = 100                       # v1는 0이였고, v2는 증가했을 때 (100%)
    elif (v1 > v2).any(): #하락률 계산
        try: value = -round(((v1 - v2) / v1) * 100,2) # v1 > v2 일 때 얼마나 하락했는지 %
        except: value = -100                    # v2가 0으로 하락했을 때 (-100%)
    else:        # 값이 같으면 0% 증감
        value = 0
            
    return value

# 결측값 확인
# - 전체데이터 개수, 결측값 개수, 결측값 비율 확인 함수
def ss_isnull(df):
    df_sum = df.count().reset_index()
    df_sum_isnull = pd.DataFrame(df.isnull().sum(), columns = ['sum_isnull']).reset_index()
    df_mean_isnull = pd.DataFrame(df.isnull().mean()*100, columns = ['mean_isnull(%)']).reset_index()
    df = pd.merge(left = df_sum , right = df_sum_isnull, how = "left", on = "index")
    df = pd.merge(left = df , right = df_mean_isnull, how = "left", on = "index")
    df.columns = ['[컬럼명]', '[sum]', '[sum_isnull]', '[mean_isnull(%)]']
    return df

# 컬럼들의 value_counts 처리 함수
def ss_value_counts(df, columns = ''):
    if columns == '':
        columns = df.columns
        
    for column in columns:
        print('==========================================')
        print(df[column].value_counts())

# 이상치 제거 함수
def check_outlier(_df, _column):
    # IQR 방법
    Q1 = _df[_column].quantile(0.25)
    Q3 = _df[_column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = _df[~((_df[_column] < lower_bound) | (_df[_column] > upper_bound))]
    
    return outliers