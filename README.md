# XIN_Picture_Downloader

## 사용법

0. [Python을 설치](https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe)한다
> Add Python3.x to PATH 는 꼭 클릭한다.

1. 해당 repository를 git으로 clone 또는 [download](https://github.com/DetegiCE/XIN_Picture_Downloader/archive/master.zip)한다

2. 터미널을 이용하여 해당 폴더에 접근한다.
> 혹은 탐색기를 C://xxx/XIN_Picture/Downloader 에 위치시킨 후 주소창을 클릭한 후 "cmd ."을 입력하고 Enter를 입력한다

3. XIN 강의의 html을 긁어오자.

3-1. XIN 강의로 들어가서 F12를 누른다.

3-2. Elements를 누르고 ``<html class=``에서 우클릭을 하고 ``Edit as HTML``을 누른다.

3-3. Ctrl+A(전체선택) 후 Ctrl+C(복사) 한다.

3-4. data 폴더 아래의 xinhtml.txt 파일에 Ctrl+V(붙여넣기) 한다.

4. 다음 명령어를 이용하여 프로그램을 돌린다

```python ./main.py```
