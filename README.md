# XIN_Picture_Downloader

XIN 강의의 사진과 영상(음성)을 자동으로 다운로드 해주는 프로그램입니다.

음성 다운로드 시에는 오래걸리니 왜 안움직이지? 오류났나? 하고 프로그램 종료하는 불상사가 없길 바랍니다.

## 사용법

0. [Python을 설치](https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe)한다
> Add Python3.x to PATH 는 꼭 클릭한다.

1. 해당 repository를 git으로 clone 또는 [download](https://github.com/DetegiCE/XIN_Picture_Downloader/archive/master.zip)한다

2. 터미널을 이용하여 해당 폴더에 접근한다.
> 혹은 탐색기를 C://xxx/XIN_Picture_Downloader 에 위치시킨 후 주소창을 클릭한 후 "cmd ."을 입력하고 Enter를 입력한다

3. 다음과 같이 라이브러리를 설치한다.
> BeautifulSoup4가 이미 깔려있으신 개발자 분께서는 이 과정을 스킵하셔도 됩니다.

```
pip install -r requirement.txt
```

또는

```
pip3 install -r requirement.txt
```

4. XIN 강의의 html을 긁어오자.

> 4-1. XIN 강의로 들어가서 F12를 누른다.

> 4-2. Elements를 누르고 ``<html class=``에서 우클릭을 하고 ``Edit as HTML``을 누른다.

> 4-3. Ctrl+A(전체선택) 후 Ctrl+C(복사) 한다. 

> 4-4. data 폴더 아래의 xinhtml.txt 파일에 Ctrl+V(붙여넣기) 한다.

5. 다음 명령어를 이용하여 프로그램을 돌린다

```python ./main.py```
