# Numpy 기초 사용법

-- Numerical Python
-  C언어로 구현된 저수준 고성능 라이브러리
-  반복문을 작성할 필요 없이 전체 데이터 배열에 대한 빠른 연산 지원
-  배열 데이터를 디스크에 쓰거나 읽을 수 있는 도구와 메모리에 올려진 파일에 사용하는 도구
-  빠르고 메모리를 효율적으로 사용하여 다차원 배열 ndarray ㅣ원
-  선형대수,난수 발생기, 푸리에 변환 기능

import numpy as np

-  스칼라/벡터/행렬
   - 스칼라는 number
   - 벡터는 숫자들의 리스트(row || columns)
   - 행렬은 숫자들의 array(row && columns)
   
   
-  numpy 배열 (1/2)
   - numpy 배열을 만들 때는 np.array() 메소드 이용
   - np.array()는 파이썬의 리스트를 numpy,ndarray 형태로 변환
   - numpy는 다차원 행렬로 표현하고 , 계산하기 쉬움
   arr = [[1,2,3,4],[5,6,7,8]]
   arr2 = np.array(arr)
   arr2.ndim
   Out[] : 2
   arr2.shape
   Out[] : (2,4)
   arr2 * 10
   Out[] : array([10,20,30,40],[50,60,70,80])
   arr2 + 10
   Out[] : array([11,12,13,14],[15,16,17,18])
   
   - np.zeros(5) : 0으로 초기화된 배열
   Out[] : array([0.,0.,0.,0.,0.])
   - np.ones(5) : 1로 초기화된 배열
   Out[] : array([1.,1.,1.,1.,1.])
   - np.linespace(0, 10, 5) : 선형 구간에서 지정 구간의 수만큼 분할
   Out[] : array([0,2.5,5,7.5,10])
   - np.logspace(0, 100, 5) : 로그 구간에서 지정 구간의 수만큼 분할
   Out[] : array([1.e+000, 1.e+025, 1.e+050, 1.e+075, 1.e+100, ])
   - np.empty(5) : 배열을 메모리에 생성만하고 특정한 값을 초기화하지 않는 배열 (초기화 시간 단축)
