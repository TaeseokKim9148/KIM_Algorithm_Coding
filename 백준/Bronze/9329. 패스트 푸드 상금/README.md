# [Bronze I] 패스트 푸드 상금 - 9329 

[문제 링크](https://www.acmicpc.net/problem/9329) 

### 성능 요약

메모리: 32412 KB, 시간: 276 ms

### 분류

그리디 알고리즘, 구현

### 제출 일자

2024년 12월 31일 16:58:32

### 문제 설명

<p>ACM-ICPC 아시아 지역 대회기간 중 대전의 패스트 푸드 음식점들은 그들의 음식점을 홍보하기 위해 이벤트를 준비한다. 특정 음식을 먹을 때 마다 스티커를 하나 제공하는데 스티커를 모으면 상금으로 교환할 수 있다. 같은 종류의 스티커가 필요한 상금은 여러 번 교환할 수 있으며, 같은 종류의 스티커를 가진 서로 다른 액수의 상금은 존재하지 않는다. 상금 교환에 필요없는 스티커도 있다.</p>

<p>지역대회를 보러 가면서, 당신의 코치가 패스트 푸드 음식점에서만 식사를 하도록 허락했을 때, 얼마나 많은 상금을 획득할 수 있을까?</p>

### 입력 

 <p>입력은 여러개의 테스트 케이스로 이루어져있다. 각 테스트 케이스마다 첫째 줄에는 서로 다른 상금의 종류 n (1 ≤ n ≤ 10) 과 코치가 가지고 있는 스티커의 종류 (1 ≤ m ≤ 30, 종류는 1부터 m까지 번호가 매겨진다) 가 주어진다. 다음 n개의 줄은 상금에 관한 정보가 주어지는데 각 줄마다 첫 번째 정수는 해당 상금에 필요한 스티커의 개수 k (1 ≤ k ≤ m) 가 주어지며 뒤이어 k개의 정수에는 해당 상금에 필요한 스티커의 종류가 주어지며 마지막으로 상금의 액수가 주어진다 (최대 1,000,000) . n개의 모든 입력이 주어진 후 마지막 줄은 코치가 가지고 있는 1부터 m까지 스티커의 개수가 각각 주어진다. 각각의 스티커의 개수는 100개 이하이다.</p>

### 출력 

 <p>각각의 케이스마다 최대 상금의 액수를 한줄씩 출력한다.</p>

