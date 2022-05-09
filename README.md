#네이버 쇼핑몰 리뷰 분석
-------------------------------
##주제
--------
텍스트마이닝을 이용한 에어팟pro와 에어팟3세대 긍정도평가 비교

<br>

##데이터: 네이버 쇼핑 리뷰  
-------------------------------
### 데이터 수집  
> 네이버쇼핑 리뷰 크롤링(에어팟종류,리뷰, 별점)  
  네이버쇼핑 리뷰 크롤링
  
  (https://github.com/yoonsungil/textmining/data/air3_result.csv)
  (https://github.com/yoonsungil/textmining/data/result.csv)

<p>
  
### 데이터 전처리
> 불용어 제거, 형태소 분석(토큰화)  
  토큰화 (https://github.com/yoonsungil/textmining/data/token_review.csv)

<p>
  
### 감정사전 추가
  (https://github.com/yoonsungil/textmining/data/positive.txt)
  (https://github.com/yoonsungil/textmining/data/negative.txt)
    
### 긍정도 계산  
  감정사전을 이용하여 긍정도계산
  
--------------------------------------------------------------  
  
##결과
--------------------------------------------------------------  
  ![image](https://user-images.githubusercontent.com/90197102/167356417-eeb2ec8a-38b5-4a1b-979c-8aaf21d79368.png)

  ![image](https://user-images.githubusercontent.com/90197102/167356695-74909318-01b8-45b3-9f13-202651cd80ab.png)


  
>리뷰 별점 4~5점대 분포가 대부분. 소비자들이 부정적인 리뷰를 잘 남기지 않는 경향이 있음.
  
>아이팟3세대에 비해 아이팟pro 긍정도가 높음.

----------------------------------------------------------------
  
  >별점별 긍정도를 확인했을때 별점이 낮음에도 긍정도가 높아진 이상한 결과가 나왔다.
  낮은 별점에 비해 긍정도가 높게 측정된 리뷰를 살펴보았을때 단어의 출현빈도만 가지고 측정을 하여 이러한 결과값이 나온것으로 생각된다.
  (ex: 마침 생일쿠폰이 있어서 저렴하게 구입했어요 배송도 빠르고 음질도 좋은데 1세대에 비해귀에 꽂는부분 크기가 커져서 조금 불안해요. 별점 1)
  
##문제점
  
  감성사전 빈약.
  td-idf( Document Term Matrix(DTM) 내 단어마다 중요도를 고려하여 가중치를 주는 통계적인 단어 표현방법)

 
