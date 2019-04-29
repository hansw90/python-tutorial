import numpy as np # numpy 도 함께 import
import pandas as pd

# Series 정의하기
obj = pd.Series([4,7,-5,3])
obj

#Series 의 값만 확인하기
obj.values

#Series 의 인덱스 확인하기
obj.index

#Series 의 자료형 확인하기
obj.dtypes

#인덱스를 바꿀 수 있다.
#obj2 = pd.Series([4,7,-5,3]), index= ['d','b','a','c']
#obj2

#python 의 dictionary 자료형을 Series data 로 만들수 있다.
#dictionary 의 key가 Series 의 index가 된다.
sdata = {'Kim': 35000, 'Beomwoo': 67000, 'Joan': 12000, 'Choi': 4000}
obj3 = pd.Series(sdata)
obj3

obj3.name = 'Salary'
obj3.index.name = 'Names'
obj3

#index 변경
obj3.index = ['A','B','C','D']
obj3

##Data Frame
#data frame 정의하기
#이전에 DataFrame에 들어갈 데이터를 저의해주어야 하는데,
#이는 python 의 dictionary 또는 numpy의 array로 정의 할 수 있다.

data = {'name': ['Beomwoo', 'Beomwoo', 'Beomwoo', 'Kim', 'Park'],
        'year': [2013, 2014, 2015, 2016, 2015],
        'points': [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data)
df

#행과 열의 구조를 가진 데이터가 생긴다

#행 방향의 index
df.index

#열 방향의 index
df.colums

#값 얻기
df.values

#각 인덱스에 대한 이름 설정하기
df.index.name = "Num"
df.columns.name = "Info"
df

#DataFrome을 만들며서 columns 와 index를 설정할 수 있다.
df2 = pd.DataFrame(data, columns=['year', 'name', 'points', 'penalty'],
                  index=['one', 'two', 'three', 'four', 'five'])
df2

"""
DataFrame을 정의하면서, data로 들어가는 python dictionary와 columns의 순서가 달라도 알아서 맞춰서 정의된다.
하지만 data에 포함되어 있지 않은 값은 NaN(Not a Number)으로 나타나게 되는데,
이는 null과 같은 개념이다.
NaN값은 추후에 어떠한 방법으로도 처리가 되지 않는 데이터이다.
따라서 올바른 데이터 처리를 위해 추가적으로 값을 넣어줘야 한다.

"""

# describe() 함수는 DataFrame의 계산 가능한 값들에 대한 다양한 계산 값을 보여준다.
df2.describe()

## DataFrame Indexing
data = {"names": ["Kilho", "Kilho", "Kilho", "Charles", "Charles"],
           "year": [2014, 2015, 2016, 2015, 2016],
           "points": [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data, columns=["year", "names", "points", "penalty"],
                          index=["one", "two", "three", "four", "five"])
df


#3-1. DataFrame 에서 열을 선택하고 조작하기
df['year']

#위와 동일
df.year 

df['year','points']

#특정 열에 대해 위와 같이 선택하고, 우리가 원한느 값을 대입할 수 있다.
df['penalty'] = 0.5
df
#penalty 속성의 값이 다 0.5

# 또는
df['penalty'] = [0.1, 0.2, 0.3, 0.4, 0.5] # python의 List나 numpy의 array


#새로운 열을 추가하기
df['zeros'] = np.arange(5)

#Series를 추가할 수도 있다.
val = pd.Series([-1.2,-1.5,-1.7], index=['two','four','five'])
df['debt'] =val
df

df['net_points'] = df['points'] - df['penalty']
df['high_points'] = df['net_points'] > 2.0
df


# 열 삭제하기
del df['high_points']
del df['net_points']
del df['zeros']

df


# DataFrame 에서 행을 선택하고 조작하기

#0번째 부터 2번까지 가져온다
#뒤에 써준 숫자번쨰의 행은 뺀다.
df[0:3]


#.loc 또는 iloc 함수를 사용하는 방법
df.loc['two']

df.loc['two':'four']

df.loc['two':'four','points']

df.loc[:,'year'] # == df['year']



##4부터 다시보기
#DataFrame 에서의 boolean indexing
"""
df

Info	year	names	points	penalty	debt
Order					
one	2014.0	Kilho	1.5	0.1	NaN
two	2015.0	Kilho	1.7	0.2	-1.2
three	2016.0	Kilho	3.6	0.3	NaN
four	2015.0	Charles	2.4	0.4	-1.5
five	2016.0	Charles	2.9	0.5	-1.7
six	2013.0	Jun	4.0	0.1	2.1

"""

#year 가 2014보다 큰 boolean data
df['year'] > 2014
"""
출력

Order 
one False 
two True 
three True 
four True 
five True 
six False 
Name: year, 
dtype: bool

"""

# year 가 2014 보다 큰 모든 행의 값
df.loc[df['year']>2014,:]
"""
Info	year	names	points	penalty	debt
Order					
two	2015.0	Kilho	1.7	0.2	-1.2
three	2016.0	Kilho	3.6	0.3	NaN
four	2015.0	Charles	2.4	0.4	-1.5
five	2016.0	Charles	2.9	0.5	-1.7

"""

df.loc[df['names'] == 'Kilho',['names','points']]
"""
Info names points 
Order 
one Kilho 1.5 
two Kilho 1.7 
three Kilho 3.6

"""

#numpy 에서와 같이 논리 연산을 응용할 수 있다.



##Data
#datafrmae 을 만들때 index column 을 설정하지 않으면 기본값으로 0부터 시작하는 정수형 숫자로 입력된다
df = pd.DataFrame(np.random.randn(6,5))
df

"""

0	1	2	3
0	0.682000	-0.570393	-1.602829	-1.316469
1	-1.176203	0.171527	0.387018	1.027615
2	-0.263178	-0.212049	1.006856	0.096111
3	2.679378	0.347145	0.548144	0.826258
4	-0.249877	0.018721	-0.393715	0.302361
5	0.851420	-0.440360	-0.345895	1.055936

"""

#np.nan 은 NaN 값을 의미한다.
df['F'] = [1.0,np.nan,3.6,6.1,np.nan,7.0]
df

#행의 값중 하나라도 nan 인 경우 그 행을 없앤다.
df.dropna(how='any')

#행의 모든 값이 nana 인 경우 그행을 없앤다.
df.dropna(how='all')

"""
주의 drop 함수는 특정 행 또는 열을 drop 하고난 DataFrame 을 반환한다.
즉, 반환을 받지 않으면 기존의 DataFrame 은 ㄱ대로이다.
아니면, inplace=True 라는 인자를 추가하여 , 반환을 받지 않고서도 
기존의 DataFrame 이 변경되도록 한다
"""

#nan 값에 값 넣기
df.fillna(value=0.5)

#nan값인지 확인하기
df.isnull()
"""
A	B	C	D	F
2016-07-01	False	False	False	False	False
2016-07-02	False	False	False	False	True
2016-07-03	False	False	False	False	False
2016-07-04	False	False	False	False	False
2016-07-05	False	False	False	False	True
2016-07-06	False	False	False	False	False
"""

# 특정 행 drop 하기
df.drop(pd.to_datetime('20160701'))

# 2개 이상의 행 삭제 하기
df.drop([pd.to_datetime('20160702'),pd.to_datetime('20160704')])

# xmrwjdduf tkrwpgkrl
df.drop('F',axis = 1)

# 2개 이상의 열 삭제 가능
df.drop(['B','D'], axis = 1)



###### Data 분석용 함수들

data = [[1.4, np.nan],
           [7.1, -4.5],
        [np.nan, np.nan],
        [0.75, -1.3]]
df = pd.DataFrame(data, columns=["one", "two"], index=["a", "b", "c", "d"])

df

"""
	one	two
a	1.40	NaN
b	7.10	-4.5
c	NaN	NaN
d	0.75	-1.3
"""

# 행방향으로의 합 (즉, 각 열의 합)
df.sum(axis=0)
"""
one    9.25
two   -5.80
dtype: float64
"""

#열 방향으로의 합 
df.sum(axis=1)
"""
a    1.40
b    2.60
c    0.00
d   -0.55
dtype: float64

위에서 볼 수 있듯이 NaN 값은 배젷고 계산한다.
NaN 값을 배제하지 않고 계산하려면 아래와 같이 skipna 에 대해 false를 지정해준다

"""

df.sum(axis=1, skipna=False)
"""
a     NaN
b    2.60
c     NaN
d   -0.55
dtype: float64
"""

# 특정 행 또는 특정 열에서만 계산하기
df['one'].sum()
df.loc['b'].sum()

"""
pandas 에서 DataFrame 에 적용되는 함수들
sum() 함수 이외에도 pandas 에서 Data Frame에 적용되는 함수는 다음의 것들이 있다.

count : 전체 성분의 NaN이 아닌 값의 갯수를 계산
min,max : 전체 성분의 최솟 최대값을 계산
argmin,argmax : 전체 성분의 최솟값,최댓값이 위치한 (정수) 인덱스를 반환
idxmin,idxmax : 전체 인덱스중 최솟값,  최대값을 반환
quantile : 전체 성분의 특정 사분위수에 해당하는 값을 반환 (0~1 사이)
sum : 전체 성분의 합을 계산
mean :  전체 성분의 평균을 계싼
median : 전체 성분의 중간값을 반환
mad : 전체 성분의 평균값으로부터의 절대 편차 (absolute deviation) 의 평균을 계산
std,var : 전체 성분의 표주편자,분산을 계싼
cumsum : 맨 첫 번째 성분부터 각 성분까지의 누적합을 계산 (0에서부터 계속 더해짐)
cumprod : 맨 첫 번째 서분 부터 각 성분까지의 누적곱을 계산 (1에서부터 계속 곱해짐)

"""

df2 = pd.DataFrame(np.random.randn(6,4),
                  columns = ["A","B","C","D"],
                  index=pd.date_range("20160701",periods=6))
df2
"""
	A	B	C	D
2016-07-01	0.497612	1.120254	0.852572	-0.322620
2016-07-02	-0.499920	0.168749	0.494070	-0.599780
2016-07-03	0.221858	-1.117121	-0.690244	0.073491
2016-07-04	1.894916	0.524897	0.662899	-1.621140
2016-07-05	-1.677478	-0.683663	0.933441	0.019365
2016-07-06	0.636183	-0.433205	1.682591	2.173543
"""
# A열과 B열의 상관계수 구하기
"""
상관계수 ??? : 두 변수간 연관성을 보여주는 지표이다. 값이 1이면 두 변수의 움직임이 와전히 
같다는 뜻이며, -1 이면 움직임이 완전히 역방향임을 의미한다
"""
df2['A'].corr(df2['B'])


# B열과 C열의 공분산 구하기
"""
공분산 covariance
두 변수의 관계를 나타내는 양을 말한다. 
2개의 양 X와 Y의 상대도수로 나타낸 상관표(相關表)가 다음과 같다고 하자. 
이제, 양 X의 평균값을 , 양 Y의 평균값을 , fij는 (xi,yi)의 상대도수라고 할 때, 를 양 X,Y의 공분산이라 한다. 
양 X,Y의 표준편차(標準偏差)를 각각 σX, σY라 하면 일반적으로μ≤ σX σY 이다.

"""
df2['B'].cov(df2['C'])


## 정렬 함수 및 기타함수
dates = df2.index
random_dates = np.random.permutation(dates)
df2 = df2.reindex(index=random_dates, columns=["D", "B", "C", "A"])
df2
"""
D	B	C	A
2016-07-02	0.067814	0.619885	-1.620676	-1.693934
2016-07-06	-0.428551	0.539906	-1.900090	-1.580576
2016-07-03	-0.141637	0.659557	0.342833	-0.216422
2016-07-01	-0.304599	0.213159	0.277114	1.024359
2016-07-05	-0.663322	-1.174652	2.678657	-0.923094
2016-07-04	0.280424	0.669932	-0.515944	-0.873492
"""
# index와 column의 순서가 섞여있다.
# 이때 index가 오름차순이 되도록 정렬해보자
df2.sort_index(axis=0)
"""
	D	B	C	A
2016-07-01	0.856860	0.159376	0.081067	0.332128
2016-07-02	-0.727796	-0.408583	-0.437716	1.576066
2016-07-03	-1.603775	0.372157	-0.018480	0.666223
2016-07-04	-1.055749	0.883351	0.259047	2.084237
2016-07-05	-0.378821	0.741508	-1.030641	1.500324
2016-07-06	-1.079917	-0.746414	-0.262546	-0.029393
"""

#column 을 기준으로
df2.sort_index(axis=1)

# 내림차순으로
df2.sort_index(axis=1, ascending = False)

# 값 기준 정렬하기
# D열의 값이 오름차순이 되도록 정렬하기
df2.sort_values(by='D')

# B열의 값이 내림차순이 되도록 정렬하기 
df2.sort_values(by='B' , ascending = False)

df2["E"] = np.random.randint(0, 6, size=6)
df2["F"] = ["alpha", "beta", "gamma", "gamma", "alpha", "gamma"]
df2

# E열과 F열을 동시에 고려하여, 오름차순으로 하려면?
df2.sort_values(by=['E','F'])

# 지정한 행 또는 열에서 중복값을 제외한 유니크한 값만 얻기
df2['F'].unique()

# 지정한 행 또는 열에서 값에 따른 개수 얻기
df2['F'].value_counts()

# 지정한 행 또는 열에서 입력한 값이 있는지 확인하기
df2['F'].isin(['alpha','beta'])
"""
2016-07-01     True
2016-07-06     True
2016-07-02    False
2016-07-03    False
2016-07-04     True
2016-07-05    False
Name: F, dtype: bool
"""

# F열의 값이 alpha나 beta인 모든 행 구하기
df2.loc[df2['F'].isin(['alpha','beta']),:]

"""
	D	B	C	A	E	F
2016-07-06	0.407270	0.922917	0.431504	0.295002	1	alpha
2016-07-01	1.646865	-0.675920	-0.201763	-0.156858	4	beta
2016-07-02	-0.771735	-0.852033	-0.904946	0.052605	0	alpha
"""

# 사용자가 직접 만든 함수를 적용하기
df3 = pd.DataFrame(np.random.randn(4,3),columns=["b","d","e"],
                  index=["Seoul","Incheon","Busan","Daegu"])

df3

func = lambda x : x.max() - x.min()
df3.apply(func,axis=0)
