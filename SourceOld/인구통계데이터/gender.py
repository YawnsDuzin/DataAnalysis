import csv      # csv 파일 Reader 관련 선언
f = open('C:/_dz/Study/Python/DataAnalysis/Source/인구통계데이터/gender.csv')   # 인구통계데이터 csv 파일 오픈
data = csv.reader(f)        # 인구통계데이터 csv 파일 읽기

sLocation = '중랑구 묵제1동'        # 검색할 지역 변수 선언
m = []      # 남성데이터 배열변수 선언
f = []      # 여성데이터 배열변수 선언

for row in data:                    # 전 지역의 데이터가 있으므로, 미사1동이 있을때까지 Loop
    if sLocation in row[0]:
        for i in row[3:104]:        # 3 ~ 103 (남자1살 ~ 남자100살)
            m.append(-int(i))       # 그래프 왼쪽으로 표시 되도록 (음수) / 검색 된 값에 -를 붙인다.
        for i in row[106:207]:      # 106 ~   (여자1살 ~ 여자100살)
            f.append(int(i))        # 그래프 오른쪽으로 표시되록 (양수)
            
import matplotlib.pyplot as plt                    # 데이터 시각화(그래프) 관련 선언
plt.rc('font', family = 'Malgun Gothic')           # 표시되는 폰트종류를 지정 (한글 깨짐 방지)
plt.rcParams['axes.unicode_minus'] = False         # - 기호 깨짐 방지
plt.title(sLocation + ' 지역의 남녀 성별 인구 분포')       # 그래프 제목
plt.barh(range(101), m, label = '남성')             # 남성 가로바 그래프 생성 (range(101) => y좌표 0 ~ 100)
plt.barh(range(101), f, label = '여성')             # 여성 가로바 그래프 생성 (range(101) => y좌표 0 ~ 100)
plt.legend()                                       # 남/여 구분 범례표시
plt.show()                                         # 그래프 표시