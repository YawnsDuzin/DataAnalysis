# 라이브러리 임포트
import os
import pandas as pd
import chardet

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

# 파일 읽기
def Read_File(file_path):
    extension = Extract_Extension(file_path)
    _encoding = Get_ExcelEncoding(file_path)     # 2024.10.17 duzin
    
    if ".parquet" == extension:                 # 2024.10.21 sungwoo - parquet 형식 읽기 추가
        return pd.read_parquet(file_path)       # 2024.10.21 sungwoo
    if ".xlsx" == extension:
        return pd.read_excel(file_path)
    if ".csv" == extension:
        print('read_file - file_path : ', file_path, ', encoding : ', _encoding)
        #return pd.read_csv(file_path, encoding=_encoding)
        try:
            return pd.read_csv(file_path, encoding='utf-8')
        except BaseException as e:
            return pd.read_csv(file_path, encoding='cp949')

# 특정 폴더의 csx, xlsx 파일들 확인
def Check_Encoding(path_dateset, path_sub):
    path = path_dateset + path_sub
    #파일 경로명 변경
    file_list = os.listdir(path)
    file_lists = [file for file in file_list if file.endswith((".csv", ".xlsx"))]
    excel = pd.DataFrame()
    
    print('path : ', path)
    
    for _, file in enumerate(file_lists):
        try:
            print('file : ', file + ', encoding : ', Get_ExcelEncoding(path + file))
        except:
            print('- Err : ', file)
            
# 특정 폴더의 csx, xlsx 파일들 확인
def Check_File(path_dateset, path_sub):
    path = path_dateset + path_sub
    
    #파일 경로명 변경
    file_list = os.listdir(path)
    file_lists = [file for file in file_list if file.endswith((".csv", ".xlsx"))]
    excel = pd.DataFrame()
    
    print('path : ', path)
    
    for _, file in enumerate(file_lists):
        try:
            df = Read_File(path + file)
                
            print('==============================================================')
            print(Extract_Extension(file) + ', ' + file + ', ' + str(len(df)))
            print(list(df.columns))
            print(list(df.iloc[1]))
        except:
            print('- Err : ', file)

# 특정 폴더의 csx, xlsx 파일들 합치기
# new_filename = '저장파일이름'
# columns = '저장할 컬럼 리스트
def Merge_File(path_dateset, path_sub, new_filename = 'merge', columns = "", encoding = 'utf-8'):
    path = path_dateset + path_sub
    
    #파일 경로명 변경
    file_list = os.listdir(path)
    file_lists = [file for file in file_list if file.endswith((".csv", ".xlsx"))]
    excel = pd.DataFrame()
    
    print('path : ', path)
    
    for i, file in enumerate(file_lists):
        df = Read_File(path + file)
        
        if (i > 0):
            if columns == "":
                df = df.iloc[1:]
            else:
                df = df.iloc[1:][columns]
        else:
            if columns == "":
                df = df
            else:
                df = df[columns]

        df.rename(columns = {'구분':'고장구분'}, inplace = True)
        df['등록일시'] = df['등록일시'].astype('str')
        
        # excel = excel.append(df , ignore_index=True) #파일 하나에 다른 파일 추가하기(파일 합치기)
        excel = pd.concat([excel, df], ignore_index=True)
        
        print('==============================================================')
        print(Extract_Extension(file) + ', ' + file + ', ' + str(len(df)))
        print(list(df.columns))

    # excel.to_csv(path+'merge.csv',index=False,encoding='euc-kr')
    # excel.to_csv(path + new_filename + '.csv', index=False, encoding='cp949')
    excel.to_csv(path + new_filename + '.csv', index=False, encoding='utf-8')             # 2024.10.21 sungwoo - csv형태로 저장하다가 parquet형태로 저장 방식을 바꾸게 되어서 주석처리함
    #excel.to_parquet(path + new_filename + '.to_parquet', index=False)                             # 2024.10.21 sungwoo - parquet 형태로 저장
