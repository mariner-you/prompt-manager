def show_menu():
    print("=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

prompts = [
    {
        "title": "루네아 프리미엄 자수실 광고 기획",
        "content": "안녕, 오늘 너는 나의 광고 제작 엔지니어야. 내가 제공하는 정보로 광고를 완성하는 전문가가 너를 도와줄 준비가 되었니? 나는 프랑스자수 놓을 때 사용하는 프리미엄 실을 광고로 만들고 싶어. 제품 이름은 '루네아'. 타겟은 자수를 놓는 사람들 모두야. 이 제품의 특징은 실의 꼬임은 단단하지만 부드럽고, 아주 우아한 광택을 가지고 있어. USP는 섬세한 색감과 조화로운 컬러, 우아하고 은은한 광택으로 작품의 가치를 높이는 프리미엄 자수실이라는 점을 강조하고 싶어. 톤앤매너는 우아함, 섬세함, 야무짐이야. 핵심 메시지는 '한 올의 섬세함이 작품의 가치를 완성합니다.'",
        "category": "이미지 생성",
        "favorite": False
    },
        {
        "title": "AI 시대의 수공예 교육과정 설계",
        "content": "너는 20년 이상의 교육과정 설계 및 교육 콘텐츠를 개발해 온 전문가야. [AI 시대의 수공예 : 손으로 만드는 가치]라는 주제로 중학교에서 활용 가능한 교육용 강의안과 PPT슬라이드를 구조화 해서 작성해줘. 교육 대상에 맞게 수업 난이도를 조절하고, 이론 수업은 30분 정도, 연관 활동이 배합된 형태로 구성해줘. 슬라이드는 [정의, 주제 선정 이유(수공예의 가치), AI와 수공예의 공존, 관련 직업, 체험 활동, 정리] 순서로 작성해줘. 사실 정보는 확인 가능한 내용만 사용하고, 정보가 부족하면 확인 질문을 해줘. 교육 대상, 수업 시간, 활동 방식 등 정보가 부족하면 확인 질문을 한 후 작성해줘. 최종 답변에 대한 핵심 근거 3개만 간결하게 bullet 형식으로 제시해줘.",
        "category": "텍스트 생성",
        "favorite": False
    },
     {
        "title": "중3 영어 단어 보충학습 자료 생성",
        "content": "너는 중학교 3학년 영어 교사이다. 학생명: {{학생명}}, 시험명: {{시험명}}, 시험 점수: {{점수}}점. 이 학생을 위한 영어 단어 보충학습 자료를 작성하라. 조건: 1. 중학교 3학년 수준의 필수 영단어 10개를 선정한다. 2. 각 단어마다 영어 단어, 한국어 뜻, 짧은 영어 예문을 제공한다. 3. 단어 암기 방법 3가지를 제시한다. 4. 학생을 격려하는 문장으로 마무리한다. 5. 이메일 본문에 바로 사용할 수 있는 형태로 작성한다. 6. 표가 아닌 번호 목록으로 작성한다.",
        "category": "자동화",
        "favorite": False
    }
]

def add_prompt():
    while True:
        title = input("제목: ")

        if title != "":
            break

        print("제목을 입력해주세요.")
        
    while True:
        content = input("내용: ")

        if content != "":
            break

        print("내용을 입력해주세요.")
        
    print("카테고리를 선택하세요.")
    print("1. 텍스트 생성")
    print("2. 이미지 생성")
    print("3. 영상 생성")
    print("4. 페르소나")
    print("5. 자동화")
    print("6. 기타")

    category = input("카테고리 번호: ")
    if category == "1":
        category = "텍스트 생성"
    elif category == "2":
        category = "이미지 생성"
    elif category == "3":
        category = "영상 생성"
    elif category == "4":
        category = "페르소나"
    elif category == "5":
        category = "자동화"
    elif category == "6":
        category = "기타"
        
    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }
    prompts.append(new_prompt)
    print("프롬프트가 추가되었습니다!")
    
def show_list():
    if not prompts:
     print("등록된 프롬프트가 없습니다.")
     return
    for number, prompt in enumerate(prompts, start=1):
        title = prompt["title"]
        category = prompt["category"]
        star = "⭐" if prompt["favorite"] else ""
        print(f"{number}. {title} / {category} {star}")

def show_by_category():
    print("=== 카테고리별 조회 ===")
    print("1. 이미지 생성")
    print("2. 텍스트 생성")
    print("3. 자동화")
    print("4. 기타")
    category_choice = input("카테고리를 선택하세요: ") 
    if category_choice == "1":
        selected_category = "이미지 생성"
    elif category_choice == "2":
        selected_category = "텍스트 생성"
    elif category_choice == "3":
        selected_category = "자동화"
    elif category_choice == "4":
        selected_category = "기타"
        
    found = False
    
    for prompt in prompts:
        if prompt["category"] == selected_category:
           found = True    
           print(prompt["title"])
           
    if not found:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")       
while True:
    show_menu()
    choice = input("메뉴를 선택하세요: ")

    if choice == "1":
        add_prompt()
    elif choice == "2":
        show_list()
    elif choice == "3":
        show_by_category()
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 메뉴 번호를 입력해주세요.")