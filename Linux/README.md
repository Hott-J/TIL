# linux-shell-script-master

## 리눅스 기본

### 자동완성 기능
* TAB을 사용해라

### 리눅스 디렉토리 구조
* 리눅스 최상위 디렉토리는 루트 디렉토리
    * `cd /`
* bin
    * 실행 가능한 명령어들
* sbin
    * 시스템 권한을 갖는 루트 사용자가 사용하는 명령어들
* lib
    * 여러 프로그램 라이브러리들
* dev
    * 장치 파일
    * 리눅스의 설치되있는 많은 하드웨어들을 작동하게 됨
    * 응용프로그램들이 장치프로그램들을 접근할 수 있게 함
* etc
    * 환경 파일
* home
    * 작업 디렉토리
    * 로그인 했을 때 디폴트
* var
    * 시스템에 관련된 많은 정보들을 저장
* usr
    * 프로그램 파일들, 프로그램 설치 디렉토리
    * 많은 리눅스 응용 프로그램들이 여기에 설치

### 경로변경
* /usr/local/include: 절대경로(전체경로)
* 현재 위치가 /usr/local일때, cd ./include: 상대경로
* cd ../~: 부모 디렉토리로 이동하고 다시 ~로 이동
* cd ../../~: 부모의 부모 디렉토리로 이동하고 다시 ~로 이동

### 파일의 접근권한
* 파일의 종류
    * 디렉토리(d)
    * 파일(f)
    * 심볼릭링크(s)
    * 장치파일(c/b)
    * 파이프(p)
    * 일반파일(-)
* drwxrwxr-x
    * d: 디렉토리
    * 첫번째 rwx: 유저권한
    * 두번째 rwx: 그룹권한
    * 세번째 r-x: 기타사용자권한(other): 읽기는 되고 쓰기는 안되며 열람은 가능
* 숫자
    * 1: 하드링크수
    * 2: 디렉토리갯수
* 유저의 이름(hottj)
* 그룹의 이름(staff)
* 파일의 크기
* 최근 파일 수정 시간
* 디렉토리명/파일명

### 심볼릭링크와 하드링크
* ln
    * 하드링크를 추가적으로 만듦
    * 원본인지 새로 만든건지 분간하기 힘듦
    * 원본파일에 있는 내용 자체를 가리킴
* 디렉토리는 하드링크를 만들 수 없다
* ln -s
    * 심볼릭링크 생성
    * 파일종류에 l이 붙음(lrwxrwxrwx)
    * 원본파일을 가리키는 링크파일(하드링크 파일 자체를 가리킴)
    * 윈도우즈의 바로가기와 유사
    * 하드링크처럼 얼마든지 만들 수 있다
    
## 쉘 기초 명령어
### echo
* printf에 준함
    * echo hello world: hello world 출력
    * echo "hello      world": 공백 문자를 유효한 문자로써 출력(작은 따옴표로도 가능)
        * 공백문자는 단어와 단어, 명령과 옵션 그리고 전달인자를 구분하는 용도로 사용됨
    * echo -e 'hello    world\n\n\n': 특수문자(특히 제어문자)를 적용, -e가 없으면 문자열로 출력됨
        * \n,\a(알람)
    * echo -n: 줄바꿈 처리가 안됨
    * echo *: 파일 목록 확인(목록이 공백문자하나로 구분되서 나옴) `substring할때 유익함`

### 명령의 구조
* ls -l /usr: 명령어, 옵션, 전달인자
    * 옵션은 -을 2개이상 쓸 수도 있다

### glob와 공백
* touch: 파일이 없으면 빈파일로 생성해주고 파일이 존재한다면 현재 시간으로 파일 수정 시각을 업데이트
* rm *(globe): 전부 삭제

### 인용문
* touch 'Gone with the Wind.mp3': Gone with the Wind.mp3라는 파일을 생성
    * 인용부호가 없다면 Gone, with, the, Wind.mp3 총 4개의 파일이 생성됨
* 작은따옴표,큰따옴표 모두 가능

### [..]와 테스트
* cd mydir; [ -f 'Gone With the Wind.mp3 ]
    * mydir로 이동, Gone With the Wind.mp3라는 파일이 있는지 확인하라
    * [-f ~]처럼 하면 안되고 반드시 공백문자를 넣어야함
* [ ]: 테스트 기능

### 명령어(wc)
* wc: 사용자가 지정한 파일의 행,단어,문자 수를 세는 프로그램
    * -w: 단어 수
    * -l: 라인 수
    * -L: 가장 긴 단어의 글자수
    * -c: 총 글자 수

### 명령어(tail)
* seq 1 200 > num200 : num200이란 파일을 리다이렉션으로 생성하는데, 내용은 1~200 숫자로 채워짐
* tail -n 10 num200 : num200파일의 마지막 10번째부분을 출력
* tail -n +10 num200 : 라인10부터 마지막까지 출력
* tail -n +101 num200 | head -n 10 : 101부터 10개 출력
    * | : 파이프기호(파이프 좌측 명령의 실행결과를 우측 명령의 입력으로 전달하는 기능임)
* tail -f /var/log/syslog : f옵션으로 시스템 로그파일을 실시간으로 보여줌.(USB가 꽂히는 작업 등)

### 별칭(alias)
* 단축명령어
* alias mkdir='mkdir -p' : mkdir -p 명령어를 mkdir로 대체
* alias m='minicom -w -D/dev/ttys0': minicom은 유닉스와 유사한 운영 체제를 위한 텍스트 기반 모뎀 제어 및 터미널 에뮬레이터 프로그램
* alias는 전달인자를 넘겨주지 못함. 함수가 이에 대한 대안
* function mm() { minicom -w -D/dev/ttyS${1};}
    * mm 0 : mm 0으로 실행 가능
* alias는 스크립트 내부에서 사용x 함수는 가능

### 명령어(pushd/popd)
* pushd .: 지정한 경로를 스택에 저장
* 이후 특정 경로로 이동후, popd 명령어로 이전 경로로 쉽게 돌아옴
* cd - : 두개의 경로간 왔다갔다함

### 명령어(printf)
* echo와 달리 형식화된 출력이 가능
* printf "%02d" 1: 01이 출력됨. 2자리
* name=michael; printf -v legend "%s jackson" %name; echo $legend: michael jackson
    * -v legend: 변수(legend), 출력 결과가 변수에 저장됨, -v: variable, $legend: 변수의 참조, 선언한 변수를 참조할 때는 꼭 $를 적어준다.

### 명령어(read)
* 사용자 입력을 받음
* read num
    * 12345 입력하면 num 변수에 12345 저장됨. echo $num 으로 확인
* read -p "what is your phone number" v
    * v에 입력한 번호가 저장됨
* read -n 1 -p "Are you over 16?" v
    * -n 1: 하나의 문자만 입력받음. 입력 후 엔터키를 누르지 않아도 됨.
* read -s -n 1 -p "Are you over 16?" v
    * -s: (silent)사용자의 입력을 화면에 에코하지 않음
* read -s -n 1 -t 3 -p "Are you over 16?" v
    * 3초이상 반응없으면 종료됨

### while..do..done
* no=1; while (( no<10 )); do printf "%02d\n" $no; ((no++)); done
    * 01 ~ 09 가 줄바꿈해서 출력

### 실행파일을 사용하는 방법 4가지
* echo 'echo hello world' > helloworld.sh
* chmod +x helloworld.sh // 실행권한 부여
* ./helloworld.sh
    * hello world 출력
#### 1
* sudo cp helloworld.sh /usr/bin (루트 권한 부여)
* helloworld.sh
    * helloworld 출력
    * /usr/bin에 복사하면 경로가 어디서든 접근가능해서 기존 실행 파일들이 존재하는 경로에 복사한다
#### 2
* 실행 파일의 전체 경로를 표현
* /home/user/Desktop/shell_cmd/helloworld.sh
#### 3
* 실행 파일의 경로를 환경 변수에 추가
* PATH=$PATH:~/Desktop/shell_cmd
* echo $PATH로 확인
* helloworld.sh
    * helloworld 출력
#### 4
* 현재 경로에서 실행
* ./helloworld.sh

## 쉘 스크립트
* 쉘은 명령 인터프리터입니다
* 사용자가 운영 체제에 대화식으로 명령을 내리거나, 명령을 일과적으로 실행할 수 있는 기능을 제공하는 응용 프로그램
* 쉘은 사용자가 시스템과 대화 할 수 있는 방법

### 스크립트 작성방법
* #!/bin/bash: 쉬뱅(해쉬뱅)
    * 번역기 역할
    * bin/bash가 스크립트를 실행
* #!/usr/bin/env bash
    * 위 방법이 안될때

### DOS 스타일의 줄끝
* echo -e 'hello\n\n\n'

### 스크립트의 실행방법 4가지
* chmod +x helloworld.sh -> ./helloworld.sh
* bash helloworld.sh
* source helloworld.sh
* . helloworld.sh

## 사용이유?
* 반복된 작업 단순화, 자동화

## 쉘프로그래밍?
* 쉘: 사용자와 커널 간 인터페이스 역할을 하는 프로그램
* 쉘스크립트: 텍스트 또는 프로그램, 리눅스/유닉스 쉘에 의해 실행되도록 설계된 프로그램
    * 인터프리터 언어
* 쉘프로그래밍: 쉘의 내장된 기능 및 리눅스 명령들을 사용한 프로그램 만들기
    * 쉘도 내장 명령어, 함수, 문법이 존재

## 쉘스크립트 구조
* 쉘스크립트 구조
    * #!(샤뱅/해시뱅)인터프리터
    * #(주석)
    * 함수들
* 잘만드는법
    * 시스템관리작업의 자동화, 단순화
    * 시스템 관리 관련 명령을 잘 알아야함
    * 작업을 위해 사용될 명령들과 명령 순서를 알아야함
    * 쉘 스크립트 작성 전 사용할 명령들, 실행 순서, 실행 조건을 노트에 미리 적어봄

## 리눅스 신규 디스크 인식 쉘 스크립트
* 명령어들을 먼저 나열해보자
* 디스크 컨트롤러 정보 확인
    * /sys/devices 디렉터리에 디스크 컨트롤러에 관련된 scan 파일 존재
    * lspci, grep, awk
    * lspci | grep 'LSI Logic' | awk '{print $1}: 정보 확인
        * 00:10.0이 출력
* /sys/devices 디렉터리에 scan파일 검색
    * find /sys/devices -name scan
    * find /sys/devices -name scan | grep 00:10.0: 파일 확인
        * /sys/devices/pci0000:00/000~~
* 디스크 인식
    * scan 파일에 디스크 인식을 위한 wildcard문자 전달(-)
    * 여기서 - 기호는 all
    * --- 는 모든 채널, 모든 타겟, 모든 LUN을 나타냄
    * lsblk | grep disk: 디스크 확인
    * echo '- - -' > /sys/devices/pci0000:00/000~~: 디스크 인식
        * 디스크 추가됨을 확인

## 리눅스 파일 시스템
* 파일 시스템 명령어 - 검색 (find 명령어 -exec 옵션)
    * find [경로][옵션][옵션조건]...
    * -exec 옵션: find 명령어로 찾은 결과 대상에 대하여 원하는 명령어를 적용
    * -exec 명령어 {} \;
        * {}: find로 찾은 파일들
        * \;: -exec 옵션 내용의 끝을 나타냄
    * find /usr/local/src -name HelloWorld.txt -exec cat {} > /usr/local/src/new_HellowWorld.txt \;
        * HelloWorld.txt 파일을 찾아서 new_HelloWorld.txt 파일로 생성
        * -exec 옵션 다음에 실행 할 명령어를 주고 "{}" 는 앞에 find 명령어로 찾은 결과 대상을 뜻함
        * cat 명령어에서 ">" 를 이용하여 왼쪽 대상의 내용을 오른쪽으로 출력한다는 것을 명시
        * 마지막에 "\;" 은 -exec 옵션과 짝을 이루어 옵션의 끝을 의미
        * find로 찾은 대상을 "{}" 로 표현하기 때문에 결과 대상에 대해 얼마든지 다양한 명령문을 실행 시킬 수 있음
    * find / -size 100M -exec ls -l {} \; 2>/dev/null
        * 루트 디렉토리로부터 파일 사이즈가 100M 이상인 파일 찾아서 ls로 상세 표시하고, 에러인 것은 출력x
    * find / -name "*.txt" -exec grep "HELP" {} \; -print 2>/dev/null
        * 루트 디렉토리로부터 txt 파일 찾아서 그 안에 HELP 라는 글자가 포함된 파일과 내용 표시
    * find . -size +50M -exec cp {} /tmp \;
        * 현재 디렉토리로부터 하위 디렉토리까지 특정 조건의 파일 찾아서 특정 디렉토리로 복사하기

* 검색 명령어 - 필터링 (grep)
    * grep [옵션]패턴[파일]: 특정 패턴 검색(또는 정규표현식 패턴 검색)
    * grep -i "vim" [file]: 대소문자 무시
    * cat /var/log/syslog | grep -i "warn": 로그 파일에서 경고만 검색
    * ps x | grep "/bin" | grep -v "grep": 프로세스 목록에서 특정 단어 검색
    * netstat -a | grep 80: 특정 포트가 열려 있는지 확인
* 정렬 명령어 - sort
    * sort [옵션][파일]: 파일의 내용을 특정 순서로 정렬
    * ls -l | sort -k 2 -n -k 5 -n: 두번째 컬럼으로 정렬후, 다섯번째 컬럼으로 정렬
* 내용 검색/편집 명령어 - awk
    * 패턴 검색 및 텍스트 프로세싱
    * cat /etc/passwd | awk -F":" '{print $1}': 암호 파일에서 콜론을 구분자로 잘라서 첫번째 컬럼만 출력
    * ls -l | awk '{print "FILENAME:"$9, "SIZE:"$5}': 디렉토리 목록중 파일명과 사이즈 가공해서 출력
    * ls -l | sort -k 5 | awk '$5>=10000 {print}': 디렉토리 목록중 파일 사이즈별로 소팅해서 10000바이트보다 큰 것만 출력
* 내용 검색/편집 명령어 - sed
    * sed 's/패턴/변환/g'
    * cat /etc/passwd | sed 's/[A-Z]/\L&/g': 출력 결과를 대문자에서 소문자로 변경
* 기타 명령어 - 분석(uniq / wc)
    * cat /var/log/auth.log | awk ‘$1=$2=$3=“”; {print $0}’ | sort | uniq: 인증 로그 내에서 처음 3컬럼 제거하고 나머지 값에서 uniq한 메시지만 출력
    * wc hello.txt: 단어수 출력
* 디스크 용량 - du (disk usage)
    * du [옵션][파일]: 파일 용량 출력
    * du / -h 2>/dev/null | grep [0-9]G: 디렉토리별 누적 용량을 출력하여 GB 이상의 디렉토리 출력
    * 각종 옵션
        * -k : 결과 값의 KB 단위 출력 (기본값)
        * -m : 결과 값의 MB 단위 출력
        * -h : 사용자 편의 용량 (KB/MB/GB, 1M=2^20=1,048,576)
        * -H : 사용자 편의 용량 (KB/MB/GB, 1M=1,000,000)
        * -s : 합계만 출력
        * -S : 서브 디렉토리 용량 합치지 않고, 각각 계산
* 압축 - tar (tape archive)
    * tar [옵션][파일][경로]
    * 각종 옵션
        * c : create (생성)
        * x : extract (해지)
        * v : verbose (디테일한 상황 보고 - 실행 중 파일 목록 출력)
        * f : file (저장될 파일명 지정하기 위해)
        * t : list (목록 확인)
        * z : zip (압축)
        * j : bzip2 (압축)
    *  tar 아카이브 만들기
        * tar cvf myzip.tar dir1
    * tar 아카이브 내용 확인
        * tar tf myzip.tar
    * tar 아카이브 풀기
        * tar xvf myzip.tar
* 압축 - gz, bz2, xz
    * gzip [옵션][파일]

## 업데이트
* apt - 패키지 관리자
* dpkg - 패키지 유틸리티

## 데몬 서비스
* 데몬?
    * 사용자가 직접적으로 제어하지 않고, 백그라운드에서 돌면서 여러 작업을 하는 프로그램
* 서비스?
    * 주로 서버/클라이언트 모델에서 출발하여, 사용자의 요청에 응답하는 프로그램(주로 데몬 형태로 구동)
* 예시
    * 웹서버 - http
    * 파일서버 - ftpd
    * 시큐어쉘 - sshd
    * 웹프록시 - squid
* 우분투의 데몬
    * 내부적으로는 systemctl
    * service <daemon-name> status
    * systemctl status/start/stop/restart <daemon-name>
* systemd 를 통한 서비스 관리
    * /sbin/init -> lib/system/systemd
    * 사용이유?
        * 프로세스의 자동 시작
        * 프로세스간의 의존성 관리
        * 프로세스의 갑작스런 종료에 대응
        * 부팅 옵션에 따른 다른 프로세스 구동
* systemctl 을 통한 다양한 데몬/서비스 확인
    * 실행 중인 서비스 목록 확인
        * systemctl list-units
    * 부팅시 기본 옵션
        * systemctl get-default
    * 서비스 상태확인/시작/중시/재시작/재로드/자동시작/자동시작삭제/숨기기(시작불가)/숨기기 제거
        * systemctl status/start/stop/restart/reload/enable/disable/mask/unmask <servicename>.service
* Journalctl 을 통한 다양한 데몬/서비스 로그 확인
    * 서비스 로그 확인
        * jornalctl -b: 부팅 후 로그
    * 특정 서비스의 로그
        * journalctl -u <service-name>
* 원하는 프로세스 서비스로 등록
    * 쉘스크립트 작성
        * sudo vi /usr/local/sbin/my-daemon.sh: 꼭 관리자 권한으로 작성해야함
        *   ```shell
            #!/bin/bash
            while true
            do
                echo “I’m still in $(date +%Y%m%d-%H%M%S)”
                sleep 10
            done
            ```
    * 실행권한 부여
        * `sudo chmod +x my-daemon.sh`
    * service 작성
    * ```service
        [Unit]
        Description=My First Daemon #이름
        After=network.target #의존성
        
        [Service]
        ExecStart=/usr/local/sbin/my-daemon.sh #뭘 실행
        Restart=always #오류시 계속 재실행
        RestartSec=5 #재실행은 5초뒤에
        User=user1 #유저권한
        Group=user1 #그룹권한
        
        [Install]
        WantedBy=multi-user.target #재부팅마다 설치
    * 데몬서비스 실행
        * `systemctl start my-daemon.service`
    * 데몬서비스 상태 확인
        * `systemctl status my-daemon.service`
    * 데몬서비스 로그확인
        * `jornalctl -u my-daemon -f`
    * 데몬서비스 중지
        * `sudo systemctl disable my-daemon.service`
        * 로그 계속 쌓는건 불필요하므로