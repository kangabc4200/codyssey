# codyssey
코디세이 연동
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