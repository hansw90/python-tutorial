"""
모듈을 설치할때 설치를 해도 모듈을 찾을 수 없을땐 가상 환경과 메인 os에 설치된 python 경로 비교를 해보아야 한다.
아래 와 같은 명령어로 경로를 탐색후 설치 한다.
"""

from sys import executable                                                        
print(executable) #Out[] : /usr/local/opt/python/bin/python3.7

#	/usr/local/opt/python/bin/python3.7 -m pip install pandas 로 설치
