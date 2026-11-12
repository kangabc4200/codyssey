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

## 트러블슈팅

### 1. Docker 웹 서버 포트 접속 실패

#### 문제
Dockerfile로 nginx 웹 서버 이미지를 빌드하고 컨테이너를 실행했지만, 처음에는 브라우저에서 웹 페이지가 정상적으로 보이지 않았다.

#### 원인 가설
컨테이너 내부에서는 nginx가 `80` 포트로 실행되지만, 호스트 PC의 포트와 컨테이너 포트가 제대로 연결되지 않았을 가능성이 있다고 판단했다.

#### 확인
실행 중인 컨테이너의 상태와 포트 매핑 정보를 확인했다.

```bash
docker ps
docker ps -a
```

`PORTS` 항목에서 다음과 같이 호스트 포트와 컨테이너 포트가 연결되어 있는지 확인했다.

```text
0.0.0.0:8080->80/tcp
```

#### 해결
컨테이너 실행 시 `-p` 옵션을 사용하여 호스트의 `8080` 포트와 컨테이너의 `80` 포트를 연결했다.

```bash
docker run -d -p 8080:80 --name web-server nginx
```

또는 직접 빌드한 이미지를 사용한 경우 다음과 같이 실행했다.

```bash
docker run -d -p 8080:80 --name web-server my-nginx
```

#### 결과
포트 매핑 후 브라우저 또는 `curl` 명령어로 접속했을 때 웹 서버가 정상적으로 응답하는 것을 확인했다.

```bash
curl http://localhost:8080
```

![Docker 웹 서버 접속 확인](images/06-docker-web-server.png)

---

### 2. README 이미지가 GitHub에서 표시되지 않는 문제

#### 문제
README.md에 스크린샷 이미지를 추가했지만, GitHub에서 이미지가 깨져서 표시되는 문제가 있었다.

#### 원인 가설
README에 작성한 이미지 경로와 실제 이미지 파일명이 일치하지 않거나, 이미지 파일이 GitHub 저장소에 커밋되지 않았을 가능성이 있다고 판단했다.

#### 확인
먼저 프로젝트 폴더와 `images` 폴더의 파일 목록을 확인했다.

```bash
ls
ls images
```

그다음 Git 상태를 확인하여 이미지 파일이 Git에 추가되었는지 확인했다.

```bash
git status
```

README의 이미지 경로도 실제 파일명과 같은지 확인했다.

```markdown
![Docker info 확인](images/09-docker-info.png)
```

#### 해결
이미지 파일을 `images/` 폴더에 정리하고, README의 이미지 경로를 실제 파일명과 일치하도록 수정했다.

수정 후 변경사항을 Git에 추가하고 커밋한 뒤 GitHub에 push했다.

```bash
git add README.md images/
git commit -m "Fix README image links"
git push
```

#### 결과
GitHub 저장소의 README에서 스크린샷 이미지가 정상적으로 표시되는 것을 확인했다.

![Docker info 확인](images/09-docker-info.png)

---

### 3. Docker 컨테이너 이름 중복 문제

#### 문제
컨테이너를 다시 실행하려고 할 때 기존에 사용했던 컨테이너 이름과 중복되어 새 컨테이너가 실행되지 않는 문제가 발생할 수 있었다.

#### 원인 가설
Docker에서는 컨테이너가 중지된 상태여도 이름이 남아 있다. 따라서 기존 컨테이너와 같은 이름을 다시 사용하면 이름 충돌이 발생한다.

#### 확인
전체 컨테이너 목록을 확인했다.

```bash
docker ps -a
```

출력 결과에서 기존 컨테이너 이름을 확인했다.

```text
NAMES
web-server
```

#### 해결
기존 컨테이너가 필요하지 않은 경우 삭제했다.

```bash
docker rm web-server
```

만약 실행 중인 컨테이너라면 먼저 중지한 뒤 삭제했다.

```bash
docker stop web-server
docker rm web-server
```

또는 새 컨테이너 실행 시 다른 이름을 사용했다.

```bash
docker run -d -p 8081:80 --name web-server-2 nginx
```

#### 결과
기존 컨테이너 이름 충돌을 해결한 뒤 새 컨테이너를 정상적으로 실행할 수 있었다.

```bash
docker ps -a
```

## Git 버전 확인

개발 환경에서 Git이 정상적으로 설치되어 있는지 확인하기 위해 Git 버전을 확인했습니다.

```bash
git --version
```

실행 결과 Git 버전이 정상적으로 출력되는 것을 확인했습니다.

![Git 버전 확인](images/10-git-version.png)

---

## Docker 운영 명령 확인

Docker 이미지, 컨테이너 상태, 로그, 리소스 사용량을 확인하기 위해 Docker 운영 명령어를 실행했습니다.

### Docker 이미지 목록 확인

```bash
docker images
```

Docker에 저장된 이미지 목록을 확인했습니다.

![Docker images 확인](images/11-docker-images.png)

### Docker 컨테이너 목록 확인

```bash
docker ps -a
```

실행 중이거나 중지된 전체 컨테이너 목록을 확인했습니다.

![Docker 컨테이너 목록 확인](images/12-docker-ps-a.png)

### Docker 컨테이너 로그 확인

```bash
docker logs web-server-2
```

웹 서버 컨테이너의 실행 로그를 확인했습니다.

![Docker logs 확인](images/13-docker-logs.png)

### Docker 컨테이너 리소스 사용량 확인

```bash
docker stats
```

실행 중인 컨테이너의 CPU, 메모리, 네트워크 사용량을 확인했습니다.  
`docker stats` 명령은 실시간으로 계속 실행되므로 확인 후 `Ctrl + C`로 종료했습니다.

![Docker stats 확인](images/14-docker-stats.png)
