# -*- coding: utf-8 -*-
import string

name = 'terminology/gnomeguide'

data = [('properties', u'속성', u'등록 정보'),
        ('preferences', u'기본 설정', u'설정 사항'),
        ('preferences', u'기본 설정', u'선택 사항'),
        ('preferences', u'기본 설정', u'환경설정'),
        ('preferences', u'기본 설정', u'기본설정'),
        ('about', u'정보', u'대하여'),
        ('font', u'글꼴', u'폰트'),
        ('button', u'단추', u'버튼'),
        ('delete', u'삭제', u'지우기'),
        ('find', u'찾기', u'검색'),
        ('search', u'찾기', u'검색'),
        ('create', u'만들기', u'생성'),
        ('change', u'바꾸기', u'변경'),
        ('remove', u'제거', u'지우기'),
        ('remove', u'제거', u'삭제'),
        ('exit', u'끝내기/마침', u'종료'),
        ('application', u'프로그램', u'어플리케이션'),
        ('application', u'프로그램', u'애플리케이션'),
        ('key', u'키', u'글쇠'),
        ('keyboard', u'키보드', u'글쇠판'),
        ('translator', u'옮긴이', u'번역자'),
        ('password', u'암호', u'열쇠글'),
        ('password', u'암호', u'비밀번호'),
        ('password', u'암호', u'비밀 번호'),
        ('paste', u'붙여넣기', u'붙여 넣기'),
        ('focus', u'포커스', u'초점'),
        ('restart', u'다시 시작', u'재시작'),
        ('screensaver', u'화면 보호기', u'화면보호기'),
        ('link', u'링크', u'바로 가기'),
        ('link', u'링크', u'바로가기'),
        ('graphics', u'그래픽', u'그림'),
        ('graphics', u'그래픽', u'그래픽스'),
        ('shortcut', u'바로 가기', u'바로가기'),
        ('shortcut', u'바로 가기', u'단축키'),
        ('filename', u'파일 이름', u'파일이름'),
        ('filesystem', u'파일 시스템', u'파일시스템'),
        ('edit', u'편집', u'고치기'),
        ('download', u'다운로드', u'내려받'),
        ('download', u'다운로드', u'내려 받'),
        ('game', u'게임', u'놀이'),
        ('history', u'기록', u'히스토리'),
        ('desktop', u'바탕 화면', u'바탕화면'),
        ('background', u'배경', u'바탕'),
        ('filename', u'파일 이름', u'파일명'),
        ('launcher', u'실행 아이콘', u'실행기'),
        ('filter', u'필터', u'거르개'),
        ('filter', u'필터', u'거르게'),
        ('version', u'버전', u'판번호'),
        ('version', u'버전', u'버젼'),
        ('locale', u'로캘', u'로케일'),
        ('separator', u'구분선', u'구분자'),
        ('update', u'업데이트', u'갱신'),
        ('hostname', u'호스트 이름', u'호스트명'),
        ('username', u'사용자 이름', u'사용자명'),
        ('non-free', u'독점', u'비자유'),
        ]

error_string = u'%s: 그놈 데스크탑에서 \"%s\"은(는) \"%s\"(이)라고 번역'

def check(msgid,msgstr):
    ret = 1
    errmsg = ''
    msgid_l = string.lower(string.replace(string.replace(msgid,'_',''),'&',''))
    for (id, right, wrong) in data:
        if ((string.find(msgstr, wrong) >= 0) and
            (string.find(msgid_l, id) >= 0) and
            (string.find(msgstr, right) < 0)):
            ret = 0
            if errmsg:
                errmsg += '\n'
            errmsg += error_string % (wrong, id, right)
    return (ret, errmsg)    

if __name__ == '__main__':
    import sys
    msgid = sys.stdin.readline()
    msgstr = sys.stdin.readline()
    t,e = check(msgid,msgstr)
    if not t:
        print e
    else:
        print 'Success'

# Local Variables:
# coding: utf-8
# End: