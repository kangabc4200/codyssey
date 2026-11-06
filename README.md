# codyssey
코디세이 연동
# 리눅스 권한 실습 기록

## 1. 권한 변경 실습

터미널에서 `chmod 755` 명령어를 사용하여 파일 권한을 변경하였습니다.

```bash
******@******-C402-B04:~/codyssey/practice_dir$ ls -l
-rw-r--r-- 1 ******@****** ******@****** 0 Nov 6 09:07 test.txt
******@******-C402-B04:~/codyssey/practice_dir$ chmod 755 test.txt
******@******-C402-B04:~/codyssey/practice_dir$ ls -l
-rwxr-xr-x 1 ******@****** ******@****** 0 Nov 6 09:07 test.txt
```
## 2. 파일 권한 변경 실습

```bash
root@454e1c03b5ec:/app/practice_dir# ls -l
total 0
-rwxr-xr-x 1 ubuntu ubuntu 0 Nov 6 00:07 test.txt

root@454e1c03b5ec:/app/practice_dir# chmod 644 test.txt

root@454e1c03b5ec:/app/practice_dir# ls -l test.txt
-rw-r--r-- 1 ubuntu ubuntu 0 Nov 6 00:07 test.txt
```

`test.txt` 파일 권한을 755에서 644로 변경했다.

## 3. 디렉토리 권한 변경 실습

`practice_dir` 디렉토리 권한을 700으로 변경한 뒤, 다시 755로 변경하였다.

```bash
root@454e1c03b5ec:/app/practice_dir# cd ..
root@454e1c03b5ec:/app# ls -ld practice_dir
drwxr-xr-x 2 ubuntu ubuntu ... practice_dir

root@454e1c03b5ec:/app# chmod 700 practice_dir
root@454e1c03b5ec:/app# ls -ld practice_dir
drwx------ 2 ubuntu ubuntu ... practice_dir

root@454e1c03b5ec:/app# chmod 755 practice_dir
root@454e1c03b5ec:/app# ls -ld practice_dir
drwxr-xr-x 2 ubuntu ubuntu ... practice_dir
```
## 4. Docker 점검

Docker 설치 상태, 이미지 목록, 컨테이너 목록을 확인하였다.

```bash
****@****:~/codyssey$ docker --version
Docker version 29.9.2, build a82e528
```

```bash
****@****:~/codyssey$ docker info
Server:
 Containers: 5
  Running: 0
  Paused: 0
  Stopped: 5
 Images: 8
 Server Version: 29.9.2
 Operating System: Docker Desktop
 OSType: linux
 Architecture: x86_64
```

```bash
****@****:~/codyssey$ docker images
IMAGE                           ID             DISK USAGE   CONTENT SIZE   EXTRA
codyssey-my-web-server:latest   47ff2608aa15   241MB        63.9MB
codyssey-web-1:latest           e12bf510f8bf   241MB        63.9MB
codyssey-web-2:latest           56fa4007ba1e   241MB        63.9MB
codyssey-web1:latest            410a1bd706eb   241MB        63.9MB
codyssey-web2:latest            5b29b6a8d524   241MB        63.9MB
hello-world:latest              c567b231f656   25.9kB       9.49kB
nginx:latest                    5ab5b0b01097   243MB        66.8MB
ubuntu:latest                   6a06111c3b0a   163MB        45.9MB
```

```bash
****@****:~/codyssey$ docker ps -a
CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS                        PORTS                  NAMES
454e1c03b5ec   ubuntu:latest   "/bin/bash"              27 minutes ago   Exited (0) 48 seconds ago                            laughing_liskov
1b55de356427   nginx:latest    "/docker-entrypoint..."  2 days ago       Exited (255) 30 minutes ago   0.0.0.0:8080->80/tcp   codyssy-lb
1a64a816ae29   codyssey-web1   "/docker-entrypoint..."  2 days ago       Exited (255) 30 minutes ago   0.0.0.0:8081->80/tcp   codyssey-web-1
64d40bfce932   codyssey-web2   "/docker-entrypoint..."  2 days ago       Exited (255) 30 minutes ago   0.0.0.0:8082->80/tcp   codyssey-web-2
9a8935ce7022   hello-world     "/hello"                 2 days ago       Exited (0) 2 days ago                                focused_wing
```

cat >> README.md <<'EOF'

## Dockerfile 웹 서버 실행 결과

- 이미지 이름: codyssey-nginx
- 컨테이너 이름: codyssey-web
- 포트 연결: localhost:8080 -> container:80
- 실행 확인 명령어:

```bash
docker build -t codyssey-nginx .
docker run -d --name codyssey-web -p 8080:80 codyssey-nginx
docker ps
curl http://localhost:8080

그다음 Git에 저장합니다.

```bash
git add README.md
git commit -m "docs: Dockerfile 웹 서버 실행 결과 기록"
git push
```
