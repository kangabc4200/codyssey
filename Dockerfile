# 1. 베이스 이미지로 nginx 최신판 사용
FROM nginx:latest

# 2. 내 컴퓨터의 app 폴더 내용을 컨테이너 안의 nginx 경로로 복사
# (이제 마운트를 안 해도 이미 안에 파일이 들어있게 됩니다!)
COPY ./app /usr/share/nginx/html

# 3. 80번 포트를 열어두겠다고 명시
EXPOSE 80
