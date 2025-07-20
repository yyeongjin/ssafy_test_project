## 회고
- 3tier로 VM 3대를 생성하여 구축해야되었으나, 단일 VM에 nextcloud 환경을 세팅하였다.
- 제로트러스트 환경으로 방화벽 제어가 필요하다.
- 키페어 생성 후 sshd 보안설정 시 Authenticationmethods publickey password로 변경 예정이다.


## 구현이유
하드디스크 케이블이 c to c 케이블인데, 사용중인 데스크톱에 호환이 되지 않아,
NAS 서버를 직접 구축하였다.

## 사용도구
- termius
- vmware workstation 17 pro

## 네트워크 환경
- 브리지 모드

## 디스크 용량
- 200GB

## OS
- debian 12