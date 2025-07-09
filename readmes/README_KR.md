# 화재-연기 감지 (`fire-smoke-detect`) 프로젝트 및 영어 설명

## `fire-smoke-detect` 및 `fire-smoke-detect-dataset`

  * **저자**: leilei
  * 이 프로젝트가 유용하다면 별(⭐)을 눌러주세요. 여러분의 별은 저에게 큰 격려가 됩니다\!
  * **참고**: YOLOv4는 화재 감지만 지원하며, YOLOv5s는 연기-화재 두 가지 유형 감지를 지원합니다\!

### 설치 환경

```
    python: 3.6 이상
    ubuntu16.04 또는 18.04
    darknet (cuda10.0 Docker)
    pytorch 1.6 이상 (cuda10.2 Docker)
```

### 새로운 오픈 소스 데이터셋

  * **작업복 반사 의류-안전모 데이터셋**: [reflective-clothes-detect-dataset](https://github.com/gengyanlei/reflective-clothes-detect)
  * 이 데이터셋은 건설 현장이나 위험 지역과 같은 특정 구역의 감지에 사용될 수 있습니다.

### 개선 및 최적화

  * 예시: 연기를 흰 연기, 검은 연기, 회색 연기로 더 세분화하거나, 화재 또한 더 정교하게 분류할 수 있습니다.

### 데이터셋 다운로드 상세 정보

  * **[연기-화재 (이미지 10827개, 라벨 없음) - 바이두 윤판 다운로드 링크](https://www.google.com/search?q=https://pan.baidu.com/s/1GhFKbp6hN26hxJWJIg_W2A)** 코드: `hhwq`
  * **[화재-연기 (이미지 2059개, 라벨 포함) - 바이두 윤판 다운로드 링크](https://pan.baidu.com/s/1AvCMcmZ7SaAZznmyTO65cg)** 코드: `3q4r`
  * **[화재-연기 (이미지 2059개, 라벨 포함) - Google Drive 다운로드 링크](https://drive.google.com/file/d/1ydVpGphAJzVPCkUTcJxJhsnp_baGrZa7/view?usp=sharing)**

-----

  * **[YOLOv4 화재 감지 가중치 - 바이두 윤판 다운로드 링크](https://pan.baidu.com/s/14g0SkV5vR8OhnDOCTW6r9A)** 코드: `w3ip`
  * YOLOv5 화재-연기 감지 가중치는 `yolov5` 폴더 안에 있습니다\!
  * **[Darknet-YOLOv4 설치 튜토리얼](https://github.com/AlexeyAB/darknet#how-to-compile-on-linux-using-make)**
  * **[yolov4.conv.137](https://drive.google.com/open?id=1cewMfusmPjYWbrnuJRuKhPMRRe_b9PaT)**
  * 최신 버전의 Darknet 예측 함수를 사용하려면 [latest\_darknet\_API.py](https://github.com/gengyanlei/fire-detect-yolov4/blob/master/latest_darknet_API.py)를 참조하세요.

### 데이터셋 사용 방법

  * 화재 감지 데이터셋은 Pascal VOC 형식으로 주석이 지정되어 있습니다:
    ```
    --VOC2020
        --Annotations (XML 파일 수: 2059)
        --ImageSets(Main)
        --JPEGImages (이미지 파일 수: 2059)
        
        --라벨 이름: fire
    ```
  * **.tar 파일 압축 해제 명령어**:
    ```
    tar -xzvf ***.tar  (Windows 또는 Linux: Git Bash)
    또는 
    7zip (Windows: 7zip; 360zip은 2번 압축 해제 필요)
    ```
  * VOC 형식을 YOLO 형식으로 변환하려면:
    ```
    YOLOv4의 스크립트 `voc_label.py`를 호출하세요.
    ```
  * **화재 현장 종류**:
    ```
    차량 화재, 초원 화재, 산림 화재, 건물 화재, 크고 작은 화재, 낮과 밤의 화재
    ```
  * **화재-연기 이미지 크롤링**:
    ```
    * 바이두-빙 이미지 크롤링: `crawl_baidu.py` 또는 `crawl_baidu_bing.py`
    ```
  * **데이터 사전 라벨링** \#\#\#\#\#\#\#\#\#\#\#\#\#\#\# 핵심 \#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#
    ```
    (1) 10827개의 연기-화재 감지 데이터셋 다운로드
    (2) 본인의 오픈 소스 YOLOv5 화재-연기 감지 모델을 사용하여 라벨 없는 이미지 사전 라벨링
    (3) 화재-연기 감지 사전 라벨링 수동 교정 후 YOLOv4, YOLOv5 재학습
    (4) 힘내세요!!!
    ```

### YOLOv4에서 테스트-학습 코드 사용 방법

  * **YOLOv4 테스트**:

    1.  먼저, YOLOv4에 따라 직접 컴파일한 Darknet을 업로드했으므로 두 번 컴파일할 필요가 없습니다. **`yolov4`의 `libdarknet.zip` 압축을 풀어 `libdarknet.so`를 확인하세요\!**
    2.  바이두 클라우드 디스크에서 YOLOv4 화재 감지 모델을 다운로드하여 `backup_fire` 폴더에 넣으세요.
    3.  `darknet_API.py` 함수를 호출하세요:
        ```python
        from darknet_API import Detect
        detect = Detect(metaPath=r'./cfg/fire.data', configPath=r'./cfg/yolov4-fire.cfg',\
                        weightPath=r'./backup_fire/yolov4-fire_best.weights',\
                        namesPath=r'./cfg/fire.names')
        image = cv2.imread(r'/home/Datasets/20200714085948.jpg', -1)
        draw_img = detect.predict_image(image, save_path='./pred.jpg')
        ```

  * **YOLOv4를 ONNX로 변환**:

    1.  YOLOv4를 ONNX로 변환하는 방법은 `./yolov4/yolov4_to_onnx/yolov4_to_onnx.py`를 참조하세요.
    2.  ONNX를 TRT 엔진으로 변환하는 방법은 `./yolov4/yolov4_to_onnx/onnx_to_trt7.py`를 참조하세요.

  * **YOLOv4 학습**:

    1.  VOC 형식 데이터를 YOLO 형식 데이터로 변환합니다.
    2.  `cfg`와 같은 파일 정보를 구성합니다.
    3.  Darknet 명령어를 호출합니다:
        ```bash
        ./darknet detector train cfg/fire.data cfg/yolov4-fire.cfg yolov4.conv.137 -gpus 0 -map -dont_show
        GPU 메모리가 부족할 경우, 배치 크기를 수정하고 무작위 다중 스케일을 취소할 수 있습니다.
        기본적으로 random=1이며, 취소하면 random=0이 됩니다.
        ```

### YOLOv5에서 테스트 코드 사용 방법

  * **YOLOv5 테스트**:

    1.  `yolov5` 폴더로 이동하여 다음 명령을 실행합니다:

    <!-- end list -->

    ```bash
    python detect.py --source ***/aaa.jpg --weights ./best.pt
    ```

### 데모

  * `./result`: 화재-연기 감지 데모

|  |
| :------------------------------------------------: |
|                     화재-연기 감지 데모                      |

  * `./xml_lab`: 화재 감지 이미지 주석

|  |
| :-------------------------------------------------: |
|                    화재 감지 이미지 주석                     |

### 인용 (`Cite`)

  * `train_data`는 다음을 포함합니다:
  * `train_data1`: [https://blog.csdn.net/LEILEI18A/article/details/107334474](https://blog.csdn.net/LEILEI18A/article/details/107334474)
  * `train_data2`: [https://bitbucket.org/gbdi/bowfire-dataset/downloads/](https://bitbucket.org/gbdi/bowfire-dataset/downloads/)
  * `train_data3`: [https://github.com/OlafenwaMoses/FireNET/releases/download/v1.0/fire-dataset.zip](https://github.com/OlafenwaMoses/FireNET/releases/download/v1.0/fire-dataset.zip)
  * `train_data4`: [https://github.com/cair/Fire-Detection-Image-Dataset/blob/master/Fire%20images.rar](https://github.com/cair/Fire-Detection-Image-Dataset/blob/master/Fire%20images.rar)
  * `fire-demo-dataset`: [http://signal.ee.bilkent.edu.tr/VisiFire/Demo/SampleClips.html](http://signal.ee.bilkent.edu.tr/VisiFire/Demo/SampleClips.html)
  * Google Drive 다운로드 링크는 QQ 그룹의 참여자들이 제공했습니다.

### 명성 (`Reputation`)

  * **이 데이터는 학술 탐구 목적으로만 사용됩니다\!\!\!**

### 기타

  * [건물 세그멘테이션 데이터셋 (`building-segmentation-dataset`)](https://www.google.com/search?q=%5Bhttps://github.com/gengyanlei/build_segmentation_dataset%5D\(https://github.com/gengyanlei/build_segmentation_dataset\))
  * [반사 의류 감지 데이터셋 (`reflective-clothes-detect-dataset`)](https://www.google.com/search?q=%5Bhttps://github.com/gengyanlei/reflective-clothes-detect%5D\(https://github.com/gengyanlei/reflective-clothes-detect\))

-----