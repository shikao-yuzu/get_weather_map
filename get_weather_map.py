from datetime import datetime as dt
import os
import shutil
import requests


def create_dir_name_base() -> str:
    tnow = dt.now()
    return tnow.strftime('%Y-%m-%d_%H.%M.%S') + "\\"


def download(url: str, path_save: str) -> None:
    print("[donwload] "+url)
    r = requests.get(url, stream=True)

    with open(path_save, "wb") as f:
        shutil.copyfileobj(r.raw, f)

    print("done.")


def get_pdf_analysis(dir_name: str) -> None:
    # ASAS: アジア地上解析天気図
    download("http://www.data.jma.go.jp/fcd/yoho/data/wxchart/quick/ASAS_COLOR.pdf", dir_name+"ASAS.pdf")

    # AUPQ35: アジア500hPa・300hPa高度・気温・風・等風速線天気図
    download("https://www.jma.go.jp/jp/metcht/pdf/kosou/aupq35_00.pdf", dir_name+"00UTC_AUPQ35.pdf")
    download("https://www.jma.go.jp/jp/metcht/pdf/kosou/aupq35_12.pdf", dir_name+"12UTC_AUPQ35.pdf")

    # AUPQ78: アジア850hPa・700hPa高度・気温・風・湿数天気図
    download("https://www.jma.go.jp/jp/metcht/pdf/kosou/aupq78_00.pdf", dir_name+"00UTC_AUPQ78.pdf")
    download("https://www.jma.go.jp/jp/metcht/pdf/kosou/aupq78_12.pdf", dir_name+"12UTC_AUPQ78.pdf")

    # AXFE578: 極東850hPa気温・風、700hPa上昇流／500hPa高度・渦度天気図
    download("https://www.jma.go.jp/jp/metcht/pdf/kosou/axfe578_00.pdf", dir_name+"00UTC_AXFE578.pdf")
    download("https://www.jma.go.jp/jp/metcht/pdf/kosou/axfe578_12.pdf", dir_name+"12UTC_AXFE578.pdf")


def get_pdf_forecast(dir_name: str) -> None:
    # ASAS: アジア地上予想天気図
    download("http://www.data.jma.go.jp/fcd/yoho/data/wxchart/quick/FSAS24_COLOR_ASIA.pdf", dir_name+"ASAS_FT24.pdf")
    download("http://www.data.jma.go.jp/fcd/yoho/data/wxchart/quick/FSAS48_COLOR_ASIA.pdf", dir_name+"ASAS_FT48.pdf")

    # FXFE5782, FXFE5784, FXFE577: 極東850hPa気温・風、700hPa上昇流／700hPa湿数、500hPa気温予想図
    for n in ["fxfe5782", "fxfe5784", "fxfe577"]:
        download("https://www.jma.go.jp/jp/metcht/pdf/kosou/"+n+"_00.pdf", dir_name+"00UTC_"+n.upper()+".pdf")
        download("https://www.jma.go.jp/jp/metcht/pdf/kosou/"+n+"_12.pdf", dir_name+"12UTC_"+n.upper()+".pdf")

    # FXFE502, FXFE504, FXFE507: 極東地上気圧・風・降水量／500hPa高度・渦度予想図
    for n in ["fxfe502", "fxfe504", "fxfe507"]:
        download("https://www.jma.go.jp/jp/metcht/pdf/kosou/"+n+"_00.pdf", dir_name+"00UTC_"+n.upper()+".pdf")
        download("https://www.jma.go.jp/jp/metcht/pdf/kosou/"+n+"_12.pdf", dir_name+"12UTC_"+n.upper()+".pdf")

    # FXJP854: 日本850hPa相当温位・風12・24・36・48時間予想図
    download("https://www.jma.go.jp/jp/metcht/pdf/kosou/fxjp854_00.pdf", dir_name+"00UTC_FXJP854.pdf")
    download("https://www.jma.go.jp/jp/metcht/pdf/kosou/fxjp854_12.pdf", dir_name+"12UTC_FXJP854.pdf")


def main():
    dir_name_base = create_dir_name_base()

    dir_name_analysis = dir_name_base + "analysis\\"
    if not os.path.exists(dir_name_analysis):
        os.makedirs(dir_name_analysis)

    dir_name_forecast = dir_name_base + "forecast\\"
    if not os.path.exists(dir_name_forecast):
        os.makedirs(dir_name_forecast)

    # 実況天気図, 解析図
    get_pdf_analysis(dir_name_analysis)

    # 予想天気図, 数値予報天気図
    get_pdf_forecast(dir_name_forecast)


if __name__ == '__main__':
    '''
    気象庁HPから最新の天気図(PDF)を取得するスクリプト
    '''
    main()
