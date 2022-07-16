import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://github.com/choieunseong" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["#FFFFFF", "#33FF33"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "최은성")
write("description", "효성중 3학년")
write("button", "github")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "좋아하는 것": "음악 감상",
  "싫어하는 것": "외출",
  "인스타 아이디": "eun_ddong",
  "요즘 보는 드라마": "환혼"
}
information(informations)
