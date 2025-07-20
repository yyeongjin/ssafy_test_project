초기에 3tier로 VM 3대를 생성하여 구축해야되었으나, 단일 VM에 nextcloud를 구축해보았다.

## VM 생성

1. 가상머신 생성을 진행한다。
![alt text](images/image.png)

2. 데비안 리눅스 기반 ISO 이미지를 선택한다.
![alt text](images/image-1.png)

3. nextcloud 서버로 이름을 정의한다.
![alt text](images/image-2.png)

4. 200기가를 할당해준다.
![alt text](images/image-3.png)

5. 브리지모드 선택 후 VM에 접속한다.


## VM 초기 세팅
1. 설치할때 Graphical install을 선택한다.
![alt text](images/image-4.png)

2. 언어는 영어를 선택한다.
![alt text](images/image-5.png)

3. location을 설정해준다.
![alt text](images/image-6.png)
![alt text](images/image-7.png)
![alt text](images/image-8.png)

4. 언어를 선택해준다.
![alt text](images/image-9.png)
![alt text](images/image-10.png)

5. 네트워크 설정을 진행한다.

- hostname은 기본값으로 선택하였다.
![alt text](images/image-11.png)

- 도메인네임도 기본값으로 선택한다.
![alt text](images/image-12.png)

- 루트 패스워드를 지정한다.
![alt text](images/image-13.png)

- 유저 풀네임은 기본값으로 설정하였다.
![alt text](images/image-14.png)

- 유저 이름은 “yeongjin”으로 설정하고, 비밀번호도 설정해주었다.
![alt text](images/image-15.png)
![alt text](images/image-16.png)

- 나중에 디스크 확장 가능성이 있기에, LVM으로 선택해주었다.
![alt text](images/image-17.png)
![alt text](images/image-18.png)

- 특정경로에 마운트를 진행한다.
![alt text](images/image-19.png)
![alt text](images/image-20.png)
![alt text](images/image-21.png)
![alt text](images/image-22.png)

- 추가로 넣을 설치미디어는 없다.
![alt text](images/image-23.png)

- 패키지 매니저 설정을 진행한다.
![alt text](images/image-24.png)
![alt text](images/image-25.png)
![alt text](images/image-26.png)

- 원격 접속과 nextcloud 사용하기 위해 web server와 ssh server를 활성화해준다.
![alt text](images/image-27.png)

- 부르로더를 설치해준다.
![alt text](images/image-28.png)
![alt text](images/image-29.png)
![alt text](images/image-30.png)

## VM 접속
1. 로그인 후 외부 아웃바운드 통신을 확인한다.
![alt text](images/image-31.png)

2. 패키지 업데이트 수행 후, sudo, vim등을 설치해준다.
![alt text](images/image-32.png)

3. /etc/ssh/sshd_config에 들어가서 포트를 변경하고, password 인증을 활성화해준다.
```sh
vim /etc/ssh/sshd_config
```
![alt text](images/image-33.png)

4. 설정 파일 reload 후 적용내역 확인해본다.
![alt text](images/image-34.png)

5. IP 주소 정보를 확인한다.
![alt text](images/image-35.png)

## termius ssh 접속
1. IP 정보를 바탕으로 termius에서 ssh 접속을 진행한다.
![alt text](images/image-36.png)
![alt text](images/image-37.png)

2. sudo 권한 활성화 진행

**주의:** sudoers에서 Nopasswd 옵션은 보안상 사용하지 않도록 한다. 
![alt text](images/image-38.png)

3. 파티션 확인
![alt text](images/image-39.png)

4. 심볼릭링크 설정
```sh
mkdir -p /home/nextcloud
mkdir -p /home/nextcloud-data
ln -s /home/nextcloud /var/www/nextcloud
chown -R www-data:www-data /home/nextcloud /home/nextcloud-data
chmod -R 755 /home/nextcloud /home/nextcloud-data
```