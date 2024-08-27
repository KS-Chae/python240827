#chatGPT가생성한이메일검증.py

import re

def is_valid_email(email):
    # 이메일 패턴 정의
    # - ^: 문자열의 시작
    # - [a-zA-Z0-9._%+-]+: 알파벳 대소문자, 숫자, 점(.), 밑줄(_), 퍼센트(%), 더하기(+), 하이픈(-)이 하나 이상
    # - @: @ 기호
    # - [a-zA-Z0-9.-]+: 알파벳 대소문자, 숫자, 점(.) 또는 하이픈(-)이 하나 이상
    # - \.: 점(.) 문자 (도메인 부분에 사용)
    # - [a-zA-Z]{2,}$: 알파벳 대소문자 2글자 이상으로 끝나야 함 (최상위 도메인)
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # re.match 함수로 이메일 주소가 패턴과 일치하는지 확인
    # - 패턴과 일치하면 True 반환
    # - 일치하지 않으면 False 반환
    if re.match(email_pattern, email):
        return True
    else:
        return False

# 테스트용 이메일 주소 리스트
email_addresses = [
    "test@example.com",                   # 올바른 이메일 주소
    "user.name+tag+sorting@example.com",  # '+' 및 '.'을 포함한 올바른 이메일 주소
    "invalid-email@",                     # '@' 뒤에 도메인이 없으므로 잘못된 이메일 주소
    "another.test@domain.co.uk",          # 올바른 이메일 주소
    "wrong@domain@domain.com"             # '@'가 두 번 사용되었으므로 잘못된 이메일 주소
]

# 각 이메일 주소를 검사하고 결과를 출력
for email in email_addresses:
    if is_valid_email(email):
        print(f"'{email}'은(는) 유효한 이메일 주소입니다.")
    else:
        print(f"'{email}'은(는) 유효하지 않은 이메일 주소입니다.")
