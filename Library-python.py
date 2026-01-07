import sys, os, time, webbrowser

facebook_link = "https://www.facebook.com/alrafeaalimam"

def open_facebook_if_termux():
    if "com.termux" in os.getenv("PREFIX", ""):
        try:
            os.system(f'termux-open-url "{facebook_link}"')
        except:
            pass

def jalan(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

# 🔹 نظف الشاشة
os.system('cls' if os.name == 'nt' else 'clear')

# 🔹 اللــوقــو (ينزل سطر سطر)
logo = """
\033[1;35m  ╔═╗╔╗ ╔══╗╔══╗╔══╗╔═╗╔╗╔╗\033[0m
\033[1;35m  ║╔╝║║ ║╔╗║║╔╗║║╔╗║║╦╝║║║║\033[0m
\033[1;35m  ║╚╗║╚╗║╔╗║║╔╗║║╠╣║║╩╗║╚╝║\033[0m
\033[1;35m  ╚═╝╚═╝╚══╝╚══╝╚╝╚╝╚═╝╚══╝\033[0m

\033[1;36mWELCOME — ABORZAN TOOL\033[0m
\033[1;33mCREATED BY: ALRAFEA ALIMAM\033[0m
\033[1;34mتابعني على الفيسبوك: https://www.facebook.com/alrafeaalimam\033[0m
"""

for line in logo.splitlines():
    jalan(line)

# 🔹 بعد اللوقو — افتح الفيس لو داخل تيرمكس
open_facebook_if_termux()

jalan("================= Installing Python Libraries =================")

libraries = [
    'requests','colorama','bs4','beautifulsoup4','pafy','pyfiglet','youtube_dl',
    'telebot','argparse','generate_user_agent',
    'numpy','pandas','matplotlib','seaborn','scipy','sympy','pillow','opencv-python',
    'selenium','httpx','aiohttp','scrapy','mechanize','cloudscraper','paramiko',
    'cryptography','pycryptodome','hashlib','pyopenssl',
    'pyautogui','keyboard','mouse','schedule',
    'flask','django','fastapi','uvicorn','requests_toolbelt',
    'scikit-learn','tensorflow','torch','transformers',
    'rich','tqdm','loguru','dateparser','faker',
]

for lib in libraries:
    jalan(f"Installing: {lib}")
    os.system(f"pip install {lib}")

jalan("=============================================================")
jalan("✔ تم تثبيت أكبر قدر من مكتبات بايثون الشائعة")
jalan("✔ جاهز للاستخدام — بدون أي نقص في المكاتب الأساسية")
jalan("By: ABORZAN — الرفيع الإمام")