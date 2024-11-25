# 라이브러리 임포트
import os
import pandas as pd
import chardet
import time

# 기본경로 설정
path_dateset = 'G:/내 드라이브/DataSet/'

# 확장자 가져오기 (Ex) .csv, .xlsx
def Extract_Extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension

# 파일명 가져오기
def Extract_Filename(file_path):
    file_name = os.path.basename(file_path)
    filename_without_extension, _ = os.path.splitext(file_name)
    return filename_without_extension

# 파일의 Encoding을 확인
def Get_ExcelEncoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read(10000))
    
    encoding = result['encoding']
    return encoding

# 2024.10.18 duzin - 추가
# chunk_size : 나눠서 읽어올 크기 (기본값 : 100만개)
def Read_nrows(file_path, _nrows = 10, encoding = ''):
    try:
        if encoding == '': 
            _encoding = Get_ExcelEncoding(file_path)
        else:
            _encoding = encoding 
        result_df = pd.DataFrame()

        try:
            result_df = pd.read_csv(file_path, nrows= _nrows, encoding='utf-8', low_memory=False)
        except:
            result_df = pd.read_csv(file_path, nrows= _nrows, encoding='cp949', low_memory=False)
        
        return result_df
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
        
# chunk_size : 나눠서 읽어올 크기 (기본값 : 100만개)
def Read_Chunk(file_path, chunk_size = 10**6):
    try:
        _encoding = Get_ExcelEncoding(file_path)
        result_df = pd.DataFrame()

        try:
            df = pd.read_csv(file_path, chunksize=chunk_size, encoding='utf-8', low_memory=False)
        except:
            df = pd.read_csv(file_path, chunksize=chunk_size, encoding='cp949', low_memory=False)
        
        for i, chunk in enumerate(df):
            # 청크 데이터프레임을 가공합니다. 여기서는 예시로 첫 5개 행만 가져옵니다.
            # processed_chunk = chunk.head()
            processed_chunk = chunk
            
            # 결과 데이터프레임에 청크를 추가합니다.
            result_df = pd.concat([result_df, processed_chunk])
            print(f" Processed a chunk of size: {len(chunk)}")
        
        return result_df
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")


def Read_pyarrow(file_path):
    from pyarrow import csv
    
    pyarrow_df = csv.read_csv(file_path).to_pandas()
    
    return pyarrow_df

def Read_dask(file_path, _dtype = ''):
    import dask.dataframe as dd

    _encoding = Get_ExcelEncoding(file_path)
    if _dtype == '':
        try:
            dask_df = dd.read_csv(file_path, encoding='utf-8')
        except:
            dask_df = dd.read_csv(file_path, encoding='cp949')
    else:
        try:
            dask_df = dd.read_csv(file_path, encoding='utf-8', dtype = _dtype)
        except:
            dask_df = dd.read_csv(file_path, encoding='cp949', dtype = _dtype)

    return dask_df


# 동일 폴더에 있는 Excel 파일의 컬럼값을 비교
# file_path = 'G:/내 드라이브/DataSet/서울시 따릉이 대여소별 대여 반납 승객수 정보/월 데이터 통합/2021/'
def Columns_Check(file_path):
    import os
    import pandas as pd
    
    #path_sub = '서울시 따릉이 대여소별 대여 반납 승객수 정보/월 데이터 통합/2021/'
    #file_path = path_dateset + path_sub
    
    #파일 경로명 변경
    file_list = os.listdir(file_path)
    file_lists = [file for file in file_list if file.endswith((".csv", ".xlsx"))]

    file_lists.sort()   #2024.10.18
    
    print('file_path : ', file_path)
    s_temps = []
    s_chk = []
    for cnt, file in enumerate(file_lists):
        try:
            #print('file : ', file)
            s_temps.append(','.join(Read_nrows(file_path + file, 5).columns))
            print(cnt, ' file : ', file)
            print('columns : ', s_temps[-1])
        except:
            print('- Err : ', file)
    
    print('================================================================================')
    # 컬럼 다른지 체크 ('X'가 있으면 안됨)
    for i, s_temp in enumerate(s_temps):
        if i == 0 : s_chk.append('O')
        if (s_temps[0] == s_temps[i]):
            s_chk.append('O')
        else:
            s_chk.append('X')
    
    print(','.join(s_chk))