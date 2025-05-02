import os
import re
import html
import shutil
import filecmp
import subprocess
from bs4 import BeautifulSoup
from pathlib import Path
from openai import OpenAI

def filespath(directory="jyywiki.cn", filetype="html"):
    basepath = Path(directory).resolve()
    for path in basepath.glob(f'**/*.{filetype}'):
        if path.exists() and path.is_file():
            yield path

def structure(directory):
    pathset, basepath = set(), Path(directory).resolve()
    for path in basepath.glob(f'**/*'):
        if path.exists() and path.is_file():
            if not path.name.endswith(".tmp"):
                pathset.add(str(path.relative_to(basepath)))
    return pathset

def convert():
    count, total, failed = 1, len(list(filespath())), list()
    for path in filespath():
        try:
            decoded = html.unescape(path.read_text())
            path.write_text(decoded, encoding="utf-8")
            print(f"处理完成({count}/{total}): {path}")
            count += 1
        except:
            failed.append(f"\033[1;91m处理失败: {path}\033[0m")
    for item in failed:
        print(item)

def update(dst="Courseware", src="jyywiki.cn"):
    count, srcset, dstset = 1, structure(src), structure(dst)
    ready = (srcset - dstset) | (srcset & dstset)
    total = len(list(ready))
    for path in ready:
        srcp, dstp = Path(src) / path, Path(dst) / Path(path).parent / Path(path).name
        dstp.parent.mkdir(parents=True, exist_ok=True)
        if dstp.exists():
            if filecmp.cmp(srcp, dstp, shallow=False):
                print(f"跳过相同文件({count}/{total}): {path}")
                count += 1
                continue
        print(f"复制文件({count}/{total}): {shutil.copy2(srcp, dstp)}") # 不更新时间戳
        count += 1
    return srcset - dstset

def conclusion():

    def extract(f):
        soup = BeautifulSoup(f.read_text(), "html.parser")
        pattern = re.compile(r'[\u4e00-\u9fffA-Za-z0-9.,!?;:"\'\s]+')
        content.append(''.join(pattern.findall(soup.get_text())).strip())

    result = subprocess.run(["git", "status", "Courseware"], capture_output=True, text=True)
    output, start = result.stdout, False
    assemble, content = list(), list()

    for line in output.split("\n"):
        line = line.lstrip()
        if "Untracked files" in line:
            start = True
            continue
        if start and line.startswith("Courseware/OS/2025/"):
            assemble.append(Path(line))

    for path in assemble:
        if path.is_dir(): 
            for file in filespath(directory=path):
                extract(file)
        elif path.is_file():
            extract(path)


    SECRET_KEY, SECRET_PROMOPT = os.getenv("SECRET_KEY"), os.getenv("SECRET_PROMOPT")
    client = OpenAI(api_key=f"{SECRET_KEY}", base_url="https://api.deepseek.com")

    if len(content) == 0:
        return

    try:
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=[
                {"role": "system", "content": f"{SECRET_PROMOPT}"},
                {"role": "user", "content": f"{content}"},
            ],
            #max_tokens=8192,
            temperature=0.5,
            stream=False
        )
    except Exception as e:
        raise RuntimeError(f"Deepseek API request failed: {e}")

    starti, endi = 0, 0
    lines = Path("README.md").read_text().splitlines()
    for i, line in enumerate(lines):
        if line.startswith("========="):
            if starti == 0:
                starti = i
            else:
                endi = i
                break

    if lines[endi - 1] == "":
        Path("README.md").write_text('\n'.join(lines[:(endi - 2)]) +
                                    '\n\n' + response.choices[0].message.content.strip() + '\n\n' +
                                    '\n'.join(lines[endi:]) + '\n')

if __name__ == "__main__":
    convert()
    update()
    conclusion()
