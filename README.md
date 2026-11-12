# codyssey
코디세이 연동
# 개발 워크스테이션 구축

## 1. 프로젝트 개요

이 저장소는 개발 워크스테이션 구축 미션 결과물을 정리한 저장소입니다.  
터미널 기본 조작, 파일 권한 설정, Git/GitHub 연동, Docker 설치 확인, Dockerfile 기반 웹 서버 실행, 포트 매핑, Docker 볼륨 영속성 검증을 수행했습니다.

---

## 2. 실행 환경

- OS: Windows
- Shell: PowerShell / VS Code Terminal
- Git: `git --version` 결과 기록
- Docker: `docker --version` 결과 기록
- Editor: Visual Studio Code

## 권한 변경 실습

`touch` 명령어로 `test.txt` 파일을 생성하고, `ls -l` 명령어로 기본 권한을 확인했습니다.

```bash
touch test.txt
ls -l
```
![기본 파일 권한 확인](images/01-permission-basic.png)

### 755 권한 변경

`chmod 755` 명령어로 `test.txt` 파일 권한을 변경했습니다.

```bash
chmod 755 test.txt
ls -l test.txt
```
![755 권한 변경 확인](images/02-permission-755.png)

### 644 권한 변경

`chmod 644` 명령어로 `test.txt` 파일 권한을 변경했습니다.

```bash
chmod 644 test.txt
ls -l test.txt
```
![644 권한 변경 확인](images/03-permission-644.png)

## Docker 설치 확인

Docker가 정상적으로 설치되었는지 확인했습니다.

```bash
docker --version
```

![Docker 버전 확인](images/04-docker-version.png)

```bash
docker run hello-world
```

![Docker hello-world 실행 확인](images/05-docker-hello-world.png)

### Docker 정보 확인

Docker 실행 환경이 정상적으로 구성되어 있는지 확인하기 위해 `docker info` 명령어를 실행했습니다.

```bash
docker info
```

실행 결과 Docker Client와 Server가 모두 정상적으로 동작 중임을 확인했습니다.

```text
Client Version: 29.9.2
Context: desktop-linux
Server Version: 29.9.2
Containers: 8
Running: 2
Paused: 0
Stopped: 6
Images: 10
Storage Driver: overlayfs
Operating System: Docker Desktop
OSType: linux
Architecture: x86_64
CPUs: 24
Total Memory: 15.25GiB
```

![Docker info 확인 1](images/09-docker-info-1.png)
![Docker info 확인 2](images/09-docker-info-2.png)

## Dockerfile 웹 서버 실행

Dockerfile을 사용하여 nginx 기반 웹 서버 이미지를 빌드하고 컨테이너로 실행했습니다.

```dockerfile
FROM nginx:latest

COPY ./app /usr/share/nginx/html

EXPOSE 80
```

이미지 빌드 명령어는 다음과 같습니다.

```bash
docker build -t codyssey-web .
```

컨테이너 실행 및 웹 서버 접속 확인 명령어는 다음과 같습니다.

```bash
docker run -d --name codyssey-web -p 8080:80 codyssey-web
docker ps
curl http://localhost:8080
```

실행 결과 `curl http://localhost:8080` 명령어를 통해 HTML 파일이 정상적으로 반환되는 것을 확인했습니다.

![Dockerfile 웹 서버 실행 결과](images/06-docker-web-server.png)

## Docker 볼륨 영속성 확인

Docker volume을 생성하고 nginx 컨테이너에 연결했습니다.

```bash
docker volume create codyssey-volume
docker volume ls
```

생성한 볼륨을 nginx 컨테이너의 웹 루트 디렉터리에 연결했습니다.

```bash
docker run -d --name volume-test -p 8080:80 -v codyssey-volume:/usr/share/nginx/html nginx:latest
```

컨테이너 내부의 `/usr/share/nginx/html/index.html` 파일에 테스트 HTML을 작성했습니다.

```bash
docker exec volume-test sh -c "echo '<h1>Docker Volume Persistence Test</h1>' > /usr/share/nginx/html/index.html"
curl.exe http://localhost:8080
```

실행 결과, 브라우저 또는 curl 명령을 통해 다음 HTML이 출력되는 것을 확인했습니다.

```html
<h1>Docker Volume Persistence Test</h1>
```

![Docker 볼륨 초기 확인](images/07-docker-volume-test.png)

이후 기존 컨테이너를 삭제하고 같은 Docker volume을 새 컨테이너에 다시 연결했습니다.

```bash
docker rm -f volume-test
docker run -d --name volume-test-2 -p 8080:80 -v codyssey-volume:/usr/share/nginx/html nginx:latest
curl.exe http://localhost:8080
```

컨테이너를 삭제한 뒤에도 동일한 HTML 내용이 출력되었습니다.  
이를 통해 Docker volume에 저장된 데이터가 컨테이너 삭제 후에도 유지됨을 확인했습니다.

![Docker 볼륨 영속성 확인](images/08-docker-volume-persistence.png)
