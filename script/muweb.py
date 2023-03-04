
from hstr import *
from hrequest import *
from hcaptcha import *
import script._con as con 
from script.expose import *
hdata = hcaptcha.getCaptchaData()
logresets = {}
class muweb:
    
    def __init__(self):
        self.rq = hrequest()
        self.tk = ""
        self.mk = ""
        self.timechors = 0
        self.apiAnycaptcha = ""
        pass

    def getCaptcha(self):

        print(self.tk, "getCaptcha")
        res = self.rq.get("http://tl.gamethuvn.net/capcha.asp?1659757734816", timeout=10)
        print(self.tk, "getCaptcha success")
        bytess = res.content
        base64 = hstr.byteToBase64Str(bytess)

        # print("self.apiAnycaptcha", self.apiAnycaptcha)
        if self.apiAnycaptcha != "":
            hdata = captchaData()
            hdata.timeout = 60
            hdata.website = "https://anycaptcha.com/"
            hdata.apikey = self.apiAnycaptcha
        print(self.tk, "Giải captcha")
        if self.apiAnycaptcha != "-1":
            ct = hcaptcha(hdata)
            de = ct.textCaptcha(base64)
            if not de:
                print(self.tk, "Tài khoản hết tiền")
                return ""
            result = ct.getResult()
            print(self.tk, "Giải captcha", result)
        else:
            abc = self.rq.post("http://45.32.118.181:1000/decaptchagamethuvn?key=test12345", "base64=" + base64)
            result = abc.text
            # print("hgcaptcha")
        return result, bytess

    def login(self, tk, mk):
        # if mk == "pass" or mk == "24081995a":
        #     mk = pass2
        self.tk = tk
        self.namehero = tk
        logresets[self.tk] = "Login"
        self.mk = mk
        oldck = ""
        if hfile.checkExists("data/" + self.tk + ".txt"):
            oldck = hfile.read("data/" + self.tk + ".txt")
        if oldck == "":
            if hfile.checkExists("data/cookie.txt"):
                oldck = hfile.read("data/cookie.txt")
        if oldck:
            self.rq.setCookie(oldck)
        print(tk, "Login...")
        log(f"{htime.getStrTimeNow3()}: {self.namehero} đăng nhập...")
        res = self.rq.get("http://tl.gamethuvn.net/#auth/login.asp?next=auth%2Fchecklogin1", timeout=40)
        if not res:
            log(f"{htime.getStrTimeNow3()}: {self.namehero} login fail")
            print(tk, "Login fail")
            return False
        # hfile.write("data/" + self.tk + ".txt", self.rq.getCookie())

        while True:
            print(tk, "Login", mk)
            self.rq.addHeader("accept-encoding: gzip, deflate")
            try:
                # hfile.writeLog(tk + "__" + mk, filename="data/logW.txt")
                log(f"{htime.getStrTimeNow3()}: {self.namehero} đợi captcha")
                captcha = self.getCaptcha()
                if not captcha:
                    log(f"{htime.getStrTimeNow3()}: {self.namehero} không lấy được captcha")
                    return False
                log(f"{htime.getStrTimeNow3()}: {self.namehero} reset captcha {captcha[0]}")
                html = self.rq.post("http://tl.gamethuvn.net/auth/login2.asp", f"acc={tk}&passType=1&pass={mk}&captcha={captcha[0]}", getStr=True)
            except:
                print(hfile.getError())
                
                time.sleep(5)
                continue
            print(tk, "Login", html)
            # html = self.rq.post("http://tl.gamethuvn.net/auth/login2.asp", f"acc={tk}&passType=1&pass={mk}&captcha={1234}", getStr=True)
            hfile.writeLog(html, filename="data/logW.txt")
            if "4 ký tự của mã xác thực chưa chính xác" in html:
                continue
            if hfile.checkExists("/image/"):
                try:
                    hfile.bytesToFile("/image/" + captcha[0] + ".png", captcha[1])
                except:
                    pass
            if "Quản lý tài khoản bảo trì" in html:
                logresets[self.tk] = "Quản lý tài khoản bảo trì"
                return False
            if "document.location.reload()" in html:
                logresets[self.tk] = "Login Success"
                print(tk, "Login Success")
                return True
            print(tk, html)
            return False
            # logresets[self.tk] = html
            # print(html)

    def reset(self, tennv, returncho=False):
        self.namehero = tennv
        self.timechors = 0
        log(f"{htime.getStrTimeNow3()}: {self.namehero} reset...")
        html = self.rq.getHtml(f"http://tl.gamethuvn.net/auth/Reset.asp?char={tennv}")

        if "ang level 10" in html:
            con.ini.write(tennv + "_reseted", htime.getStrTimeNowNguyenBan())
            return True
        if "Mỗi lần reset PO phải cách nhau 180 phút." in html:
            phutdoi = hstr.regex(html, "Vui lòng đợi (\\d+) phút nữa")
            if phutdoi:
                log(f"{htime.getStrTimeNow3()}: {self.namehero} không có vip. Vui lòng đợi {phutdoi} phút nữa.")
                return False
        ngayhetvip = hstr.regex(html, "đã đăng ký .*? ngày (\\d+/\\d+)")
        if ngayhetvip:
            ngayhetvip = "Vip hết hạn ngày " + ngayhetvip
        while True:
            try:
                captcha = self.getCaptcha()
                if not captcha:
                    return False
                html = self.rq.post("http://tl.gamethuvn.net/auth/Reset2.asp", f"char={tennv}&captcha={captcha[0]}", getStr=True)
            except:
                time.sleep(5)
                continue

            log(f"{htime.getStrTimeNow3()}: {self.namehero} reset status {html}\r\n{ngayhetvip}")
            hfile.writeLog(html, filename="data/logW.txt")
            if "4 ký tự của mã xác thực chưa chính xác" in html:
                continue
            if hfile.checkExists("/image/"):
                try:
                    hfile.bytesToFile("/image/" + captcha[0] + ".png", captcha[1])
                except:
                    pass

            if "Bạn hãy chú ý dòng thông báo đỏ" in html:
                print(f"Bạn hãy chú ý dòng thông báo đỏ")
                return False
            if "phien ban thu lai hoac copy link hong" in html:
                print(f"phien ban thu lai hoac copy link hong")
                html = self.rq.getHtml(f"http://tl.gamethuvn.net/auth/Reset.asp?char={tennv}")
                if "ang level 10" in html:
                    con.ini.write(tennv + "_reseted", htime.getStrTimeNowNguyenBan())
                    return True
                return False
            if " cần level " in html:
                con.ini.write(tennv + "_reseted", htime.getStrTimeNowNguyenBan())
                return True

            if "đang chơi nên không" in html:
                return False
            if "Quản lý tài khoản bảo trì" in html:
                return False

            if "Yeah! Bạn" in html:
                if "Bạn không nhận được point VC do chưa" in html:
                    hfile.writeLog(self.tk, filename="data/logVC.txt")
                con.ini.write(tennv + "_reseted", htime.getStrTimeNowNguyenBan())
                return True
            cho = hstr.regex(html, "chờ (\\d+) giây")
            if cho:
                cho = int(cho)
                if returncho:
                    self.timechors = cho
                    return False
                for i in range(cho):
                    logresets[self.tk] = f"Chờ {cho-i} giây"
                    print(f"Chờ {cho-i} giây")
                    time.sleep(1)
                continue
            levelcan = hstr.regex(html, "cần level (\\d+) để reset")
            if levelcan:
                return False
            return False
            print(html)