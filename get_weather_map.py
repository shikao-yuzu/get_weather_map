import requests
import shutil


def download(url: str, path_save: str):
    r = requests.get(url, stream=True)

    with open(path_save, "wb") as f:
        shutil.copyfileobj(r.raw, f)


def main():
    download("http://www.data.jma.go.jp/fcd/yoho/data/wxchart/quick/ASAS_COLOR.pdf", "asas.pdf")


if __name__ == '__main__':
    main()
