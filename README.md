# Mechwarrior 5 Mercenaries 비공식 한글 패치
[![GitHub](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/TariTomo/MechwarriorOnline-Korean-Localization/blob/master/LICENSE)
[Steam - Tari_Tomo](https://steamcommunity.com/id/Tari_Tomo/)
![맥워리어 온라인 비공식 한글패치](./screenshots/main.jpg)

### 멕워리어 5 / 멕워리어 온라인 한국 커뮤니티
| 디시인사이드 배틀테크-맥워리어 갤러리 | 멕워리어 온라인 네이버 카페 |
|:-------------:|:-------------:|
| [![디시인사이드 배틀테크-맥워리어 갤러리](./screenshots/dcgall.jpg)](https://gall.dcinside.com/mgallery/board/lists?id=mwo) | [![멕워리어 온라인 네이버 카페](./screenshots/navercafe.PNG)](https://cafe.naver.com/mechon) |

### 멕워리어 5 / 멕워리어 온라인 한국인 스트리머
| 나미노예_우혜인 |
|:-------------:|
| <a href="https://www.twitch.tv/rose0fsharoncassidy"><img src = "./screenshots/kor_mwo_streamer_1.png" width="50%"></a> |

<br>

[맥워리어5 (Steam, PC)](https://store.steampowered.com/app/784080/MechWarrior_5_Mercenaries)의 비공식 한글 패치입니다.<br>

<!-- #### 모든 수정사항은 [여기](./version_history.md) 에서 확인이 가능합니다. -->


## DLC9 (Ashes & Ascension) 대응 - 게임 버전 1.15.398
- 언어 파일(`ko-KR`, `ko-KP`)을 게임 1.15.398의 영문 원본 기준으로 재구성했습니다. (47,065개 항목)
- 기존 번역 38,142개는 그대로 유지하고, 문자열 테이블로 이동된 항목 801개는 기존 번역을 재사용했습니다.
- DLC9 캠페인 브리핑/대사/시네마틱 자막, 신규 메크 설명, 신규 무기·장비, 파일럿 특성·쿼크, 인물명 등 1,881개 항목(고유 문장 1,360개)을 새로 번역했습니다.
  - 추가 번역 원문/번역문 목록: [`translations/DLC9_1.15.398_additions.json`](./translations/DLC9_1.15.398_additions.json)
- 항성계 이름, 메크 섀시/파생형 이름, 무작위 파일럿 성씨는 기존 패치와 같이 영문으로 둡니다.
- 다른 모드와 함께 쓸 때 임무 문구가 영문으로 나오는 문제 대응: YAML, DelayedDeadlines, TTRulez AI Mod, ModOptions, MarketplaceQOL이 게임 문구를 자체 키로 다시 담고 있어 번역이 연결되지 않던 1,282개 키를 언어 파일에 추가했습니다. (영문이 게임 원문과 같은 문구에 한해 기존 번역을 재사용, 모드 고유 문구는 미번역)
- `tools/cityhash.py` : 언어 파일 v3의 네임스페이스/키 해시(CityHash64) 계산 모듈
- `tools/locres.py` : UE4 `.locres` (v0~v3) 읽기/쓰기용 파이썬 모듈

## ※멕워리어5 한글패치 참여방법
### [멕워리어5 한글패치 스프레드시트](https://docs.google.com/spreadsheets/d/1wsApuxcBJIi7p4p7p4AkVqx9v3-axuONpd8sKDd26Rg/edit#gid=0)
### 디스코드: https://discord.gg/c5MeTpQ8D6 에 접속하셔서 확인 부탁드립니다!

## 1. 테스트 패치 다운로드 및 적용방법
### 스팀판
1. [「`스팀워크샵`」](https://steamcommunity.com/sharedfiles/filedetails/?id=2518884137)에서 해당 모드를 구독합니다.
### 이외 버전
<!-- 1. 아래 링크로 이동하여 테스트 패치 파일을 다운로드 합니다. -->
1. [Release](https://github.com/angel606k/Mechwarrior-5-Korean-Localization/releases/latest)에 있는 최신버전의 한글패치를 다운로드 합니다.<br>
(※ Korean_Localization_Mod_<버전>_<날짜>.zip 파일을 다운로드 합니다.)<br>
(※ Source code 의 다운로드는 불필요 합니다.)
2. 맥워리어5가 설치된 디렉터리 (일반적으로 `C:\Program files\Steam\steamapps\common\MechWarrior 5 Mercenaries`)로 이동합니다.
3. 다운로드 한 모드파일을 `\MW5Mercs\Mods` 에 압축 해제합니다. (Mods 폴더가 없으시면 새 폴더를 작성 후 압축해제)
  (※ Mods 폴더 이하에 Korean_Localization_Mod_V(버전) 폴더가 존재하여야 정상입니다.)
4. 멕워리어5를 실행하여 MODS -> Korean Localization_<버전> 모드를 활성화 후 게임을 재시작합니다.
5. 재시작 후 Options -> Language 옵션을 Korea(South Korea)으로 선택하시면 언어 변경이 완료됩니다.
  (※ 한국어(북한) 언어는 번역 디버그용입니다.) 

## 2. 번역/검수 및 피드백은 어디에서 할 수 있나요?
・디시인사이드 배틀테크-맥워리어 마이너 갤러리를 참고하셔서 번역/검수에 참여하거나 피드백을 남겨주세요!<br>
・여러분들의 도움이 절실합니다!<br>
### 「게임이 버전업 됨에 따라 번역문도 추가 예정입니다.」

[![멕워리어 5 번역](./screenshots/dcgall.jpg)](https://docs.google.com/spreadsheets/d/1ESSVLUUrMF8etYM5_d5iWWtLyQp8_n8O_07Shvt5yN0/edit?usp=sharing)

## 스크린샷
![한글패치 적용 스크린샷 1](./screenshots/1.png)
![한글패치 적용 스크린샷 2](./screenshots/2.png)
![한글패치 적용 스크린샷 3](./screenshots/3.png)
![한글패치 적용 스크린샷 4](./screenshots/4.png)
![한글패치 적용 스크린샷 5](./screenshots/5.png)
![한글패치 적용 스크린샷 6](./screenshots/6.png)
![한글패치 적용 스크린샷 7](./screenshots/7.png)

## License

본 프로젝트는 [MIT License](./LICENSE) 하에 제공됩니다.
