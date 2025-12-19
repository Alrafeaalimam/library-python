import sys, os, time

os.system('cls' if os.name == 'nt' else 'clear')

def slow(text, delay=0.002): for c in text: sys.stdout.write(c) sys.stdout.flush() time.sleep(delay) print()

░█░░░█▀█░█▀█░█▀█░█▀▄░█▀█

░█░░░█░█░█▀▀░█▀█░█▀▄░█░█

░█▄▄░▀▀▀░▀░░░▀░▀░▀░▀░▀▀▀

logo = r"""

\033[1;35m██████████████████████████████████\033[0m
            \033[1;35m█   👁️      A B O R Z A N      👁️   █\033[0m
            \033[1;35m█              👃                    █\033[0m
            \033[1;35m█        👅                         █\033[0m
            \033[1;35m██████████████████████████████████\033[0m

               \033[1;36mCREATED BY: ALRAFEA ALIMAM\033[0m

        \033[1;33m<<<  P Y T H O N   I N S T A L L E R  >>>\033[0m

"""

slow(logo, 0.0008)

slow("================ INSTALLING PYTHON LIBRARIES ================", 0.005)

libraries = [ 'requests','colorama','bs4','beautifulsoup4','pafy','pyfiglet','youtube_dl','telebot', 'argparse','generate_user_agent','numpy','pandas','matplotlib','seaborn','scipy', 'sympy','pillow','opencv-python','selenium','httpx','aiohttp','scrapy','mechanize', 'cloudscraper','paramiko','cryptography','pycryptodome','pyopenssl','pyautogui', 'keyboard','mouse','schedule','flask','django','fastapi','uvicorn','requests_toolbelt', 'scikit-learn','tensorflow','torch','transformers','rich','tqdm','loguru','dateparser', 'faker' ]

for lib in libraries: slow(f"Installing: {lib}", 0.004) os.system(f"pip install {lib}")

os.system('cls' if os.name == 'nt' else 'clear') slow("=============================================================", 0.002) slow("✔ تم تثبيت جميع المكاتب المطلوبة بنجاح", 0.004) slow("✔ جاهز للاستخدام الآن بدون أي نقص أو مشاكل", 0.004) slow("By: ABORZAN — الرفيع الإمام", 0.004)
