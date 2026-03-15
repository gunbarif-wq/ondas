# ONdas

처음부터 새로 만든 최소 Kivy 앱입니다. 로컬 빌드 또는 GitHub Actions로 APK를 만들 수 있습니다.

## 로컬에서 APK 빌드
1. Python 3.10+ 설치
2. 의존성 설치:
   - Windows에서 APK 빌드는 WSL2/Ubuntu 환경을 권장합니다.
3. WSL2(Ubuntu) 기준:
```bash
sudo apt update
sudo apt install -y python3 python3-pip git build-essential ccache \
  libffi-dev libssl-dev libjpeg-dev zlib1g-dev
pip3 install --user buildozer
buildozer init
buildozer -v android debug
```

빌드가 끝나면 `bin/` 폴더에 APK가 생성됩니다.

## GitHub Actions로 APK 빌드
레포에 포함된 워크플로우를 실행하면 `Actions` 탭에서 APK 아티팩트를 다운로드할 수 있습니다.
