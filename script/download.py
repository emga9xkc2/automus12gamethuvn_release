
import sys, signal, os
from turtle import ht
import zipfile
import requests, shutil
from distutils.dir_util import copy_tree
from os import listdir
import io, os, sys, random, re, time
import winreg as reg

title = ""


def downloadmyscript(title, useSelenium=True, useSSH=True):
    useOrbita = False
    if "Gmail Changer" in title:
        useOrbita = True
        pass

    def roaming():
        platform = sys.platform
        if platform.endswith("win32"):
            d = "~/appdata/roaming"
        elif platform.startswith("linux"):
            d = "~/.local/share"
        elif platform.endswith("darwin"):
            d = "~/Library/Application Support"
        else:
            d = "~"
        return os.path.abspath(os.path.expanduser(d))

    def temp():
        return os.getenv("TEMP")

    def chrome():
        reg_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe"
        for install_type in reg.HKEY_CURRENT_USER, reg.HKEY_LOCAL_MACHINE:
            try:
                reg_key = reg.OpenKey(install_type, reg_path, 0, reg.KEY_READ)
                chrome_path = reg.QueryValue(reg_key, None)
                reg_key.Close()
                if not os.path.isfile(chrome_path):
                    continue
            except WindowsError:
                chrome_path = None
            else:
                break

        return chrome_path

    def dirScript():
        file_path = sys.path[0]
        if not ":" in file_path:
            file_path = os.getcwd()
        return file_path

    def fixFileName(filename):
        platform = sys.platform
        if platform.endswith("win32"):
            if not ":" in filename:
                filename = dirScript() + "/" + filename
        filename = filename.replace("\\", "/")
        while True:
            if "//" in filename:
                filename = filename.replace("//", "/")
            else:
                break
        if platform.endswith("win32"):
            filename = filename.replace("/", "\\")
        elif platform.startswith("linux"):
            filename = filename.replace("\\", "/")
        return filename

    def listDir(dir2):
        dir2 = fixFileName(dir2)
        return next(os.walk(dir2))[1]

    def copyDir(src, dst):
        try:
            src = fixFileName(src)
            dst = fixFileName(dst)
            copy_tree(src, dst)
        except Exception as e:
            pass

    def createDir(dir):
        dir = fixFileName(dir)
        os.makedirs(dir, exist_ok=True)

    def checkExists(fileorfoler):
        fileorfoler = fixFileName(fileorfoler)
        if fileorfoler == None:
            return False
        return os.path.exists(fileorfoler)

    chromedriver_data = os.getenv("APPDATA") + "\\chromedriver\\"
    versionDownload = chromedriver_data + "version.txt"
    chromedriverExe = chromedriver_data + "chromedriver.exe"
    createDir(chromedriver_data)

    def writeFile(filename, text):
        f = open(filename, "w", encoding="utf-8")
        f.write(text)
        f.close()

    def readFile(filename):
        try:
            f = open(filename, "r", encoding="utf-8")
            return f.read()
        except:
            return ""

    def is_binary_patched(executable_path=None):
        try:
            with io.open(executable_path, "rb") as fh:
                # print("!")
                for line in iter(lambda: fh.readline(), b""):
                    # print(line)
                    if b"cdc_" in line:
                        # print(line)
                        return False
                else:
                    return True
        except Exception as e:
            print(e)

    def gen_random_cdc():
        cdc = random.choices("abcdefghijklmnopqrstuvwxyz", k=26)
        cdc[-6:-4] = map(str.upper, cdc[-6:-4])
        cdc[2] = cdc[0]
        cdc[3] = "_"
        return "".join(cdc).encode()

    def patch_exe(executable_path):
        linect = 0
        replacement = gen_random_cdc()
        with io.open(executable_path, "r+b") as fh:
            for line in iter(lambda: fh.readline(), b""):
                if b"cdc_" in line:
                    fh.seek(-len(line), 1)
                    newline = re.sub(b"cdc_.{22}", replacement, line)
                    fh.write(newline)
                    linect += 1
            return linect

    def downloadChromeDriver(lastVersion):
        patched = is_binary_patched(chromedriverExe)
        if patched:
            readversionDownload = readFile(versionDownload)
            if readversionDownload == lastVersion:
                return
        chromedriver_win32 = requests.get("https://chromedriver.storage.googleapis.com/" + lastVersion + "/chromedriver_win32.zip")
        zip = chromedriver_data + "\\chromedriver.zip"
        with open(zip, "wb") as f:
            f.write(chromedriver_win32.content)
        with zipfile.ZipFile(zip, "r") as zip_ref:
            os.system("taskkill /im chromedriver.exe /F")
            zip_ref.extractall(chromedriver_data)
            patch_exe(chromedriverExe)
            # patche = is_binary_patched(chromedriverExe)
            writeFile(versionDownload, lastVersion)
            print("chromedriver update success")

    def updateChromeDriver():
        try:
            folder, _ = os.path.split(chrome())
            chromeversion = listdir(folder)[0]

            # patche = is_binary_patched(chromedriverExe)
            readversionDownload = readFile(versionDownload)
            version = chromeversion.split(".")[0]
            if version in readversionDownload:
                return
            print("chromedriver updateing...")
            lastVersion = requests.get("https://chromedriver.storage.googleapis.com/LATEST_RELEASE").text
            chromedriver_win32 = requests.get("https://chromedriver.storage.googleapis.com/" + lastVersion + "/chromedriver_win32.zip")
            downloadChromeDriver(lastVersion)

        except Exception as e:
            print(e)

    def downloadNew(folder="pathmyscript", filename="hrequest.py", urldownload="http://toolmmo.pro:92/files/myscript.zip"):

        if not os.path.exists(fixFileName(folder + "/" + filename)):
            createDir(folder)
            pathzip = folder + "abc.zip"
            pathzip = fixFileName(pathzip)
            with open(pathzip, "wb") as f:
                print("Downloading...")
                response = requests.get(urldownload, stream=True)
                total_length = response.headers.get("content-length")

                if total_length is None:
                    f.write(response.content)
                else:
                    dl = 0
                    total_length = int(total_length)
                    for data in response.iter_content(chunk_size=4096):
                        dl += len(data)
                        f.write(data)
                        done = int(50 * dl / total_length)
                        sys.stdout.write("\r[%s%s]" % ("=" * done, " " * (50 - done)))
                        sys.stdout.flush()
                    print("\r")
            with zipfile.ZipFile(pathzip, "r") as zip_ref:
                folderextract = fixFileName(folder)
                zip_ref.extractall(folderextract)
                try:
                    os.remove(pathzip)
                except Exception as e:
                    pass
                if urldownload.startswith("https://github.com"):
                    dirs = listDir(folder)
                    for z in dirs:
                        if "-main" in z:
                            if "chromedriver" in folder:
                                os.system("taskkill /im chromedriver.exe /F")
                            dir1 = fixFileName(folder + "/" + z)
                            copyDir(dir1, folder)
                            shutil.rmtree(dir1)
                return True
        return False

    def gDownload(id, destination):
        URL = "https://docs.google.com/uc?export=download"
        session = requests.Session()
        params = {"id": id, "confirm": "t"}
        print("Downloading " + id)
        response = session.get(URL, params=params, stream=True)
        token = gToken(response)

        if token:
            params = {"id": id, "confirm": token}
            response = session.get(URL, params=params, stream=True)
        print("Save data " + id)
        gSave(response, destination)
        print("Success")

    def gToken(response):
        for key, value in response.cookies.items():
            if key.startswith("download_warning"):
                return value

        return None

    def gSave(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)

    def createShortcut(title, target="", wDir="", arguments="", icon=""):
        try:
            if title == "" or title == ".lnk":
                title = "Main.lnk"
            if os.path.exists(title):
                return
            path = fixFileName(title)
            target = fixFileName(target)
            wDir = fixFileName(wDir)
            arguments = fixFileName(arguments)
            icon = fixFileName(icon)
            if not checkExists(icon):
                icon = fixFileName("setup/images/icon.ico")
            from win32com.client import Dispatch

            shell = Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.Arguments = arguments
            shortcut.WorkingDirectory = wDir
            if icon == "":
                pass
            else:
                shortcut.IconLocation = icon
            shortcut.save()
        except Exception as e:
            pass

    def extractZip(pathzip, folder):
        print("extractZip " + pathzip)
        pathzip = fixFileName(pathzip)
        folder = fixFileName(folder)
        with zipfile.ZipFile(pathzip, "r") as zip_ref:
            folderextract = fixFileName(folder)
            zip_ref.extractall(folderextract)
            try:
                os.remove(pathzip)
            except Exception as e:
                print(e)
                pass
        print("extractZip success")

    pathinenv = os.environ.get("PYTHONPATH")
    pathmyscript = "D:/Google Drive/My Data/python/myscript/"
    if not os.path.exists(pathmyscript):
        pathmyscript = fixFileName(roaming() + "\\myscript\\")
        createDir(pathmyscript)
        # print(pathmyscript)

    if pathinenv != pathmyscript:
        platform = sys.platform
        if platform.endswith("win32"):
            os.system("SETX {0} {1}".format("PYTHONPATH", '"' + pathmyscript))
        elif platform.startswith("linux"):
            # os.system("export PYTHONPATH=/root/.local/share/myscript/")
            os.system("export PYTHONPATH=" + pathmyscript)
    filename = "main.pyc"
    filename = fixFileName(filename)

    createShortcut(title.split("_")[0].strip().upper() + ".lnk", r"C:\Windows\py.exe", "", '"' + filename + '"', "/form/icon.ico")
    if useSelenium:
        downloadNew(os.getenv("APPDATA") + "\\chromedriver\\", "1022.txt", "https://github.com/emga9xkc2/chromedriver-exe/archive/refs/heads/main.zip")
        if not useOrbita:
            updateChromeDriver()
        else:
            orbitaDir = fixFileName(roaming() + "/orbita")
            createDir(orbitaDir)
            while True:
                if checkExists(orbitaDir + "/orbita.exe"):
                    break
                gDownload("1SLYRPoSeXqldUPTspRAegU_0UaV4rSza", temp() + "/orbita_download_1SLYRPoSeXqldUPTspRAegU_0UaV4rSza.zip")
                extractZip(temp() + "/orbita_download_1SLYRPoSeXqldUPTspRAegU_0UaV4rSza.zip", orbitaDir)
            downloadChromeDriver("100.0.4896.60")
    if useSSH:
        downloadNew(os.getenv("APPDATA") + "\\ssh\\", "1080.tlp", "https://github.com/emga9xkc2/ssh-exe/archive/refs/heads/main.zip")
    # pathmyscript = os.getenv("APPDATA") + "\\myscript\\"
    newdownload = downloadNew(pathmyscript, "hrequest.py", "https://github.com/emga9xkc2/my-script/archive/refs/heads/main.zip")
    if newdownload:
        os.kill(os.getpid(), signal.SIGTERM)
        sys.exit()
