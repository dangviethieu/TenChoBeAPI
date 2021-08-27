from typing import List
import requests
import re
from os import name
from typing import Dict, List
import csv
import configs
from bs4 import BeautifulSoup
from models import NameDB, Sex, FirstNameDB, DetailDB


def get_names() -> List:
    names: List[Dict] = []
    with open(configs.NAMES_PATH, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            names.append(NameDB(name=row[0], sex=Sex(row[1])).dict())
    return names

def get_first_names() -> List:
    first_names: List[Dict] = []
    with open(configs.FIRST_NAMES_PATH, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            first_names.append(FirstNameDB(first_name=row[0]).dict())
    return first_names


def get_detail(detail_name: str) -> Dict:
    url = f"https://tenchocon.vn/name/{detail_name}.html"
    print(url)
    ret = requests.get(url)
    soup = BeautifulSoup(ret.content, 'html.parser', from_encoding="utf8")
    # with open('test.html', 'w+') as f:
    #     f.write(str(soup))
    lb_thien = "".join([str(x) for x in soup.find("span", {"id": "lb_thien"}).contents])
    lb_nhan = "".join([str(x) for x in soup.find("span", {"id": "lb_nhan"}).contents])
    lb_dia = "".join([str(x) for x in soup.find("span", {"id": "lb_dia"}).contents])
    lb_ngoai = "".join([str(x) for x in soup.find("span", {"id": "lb_ngoai"}).contents])
    lb_tongcach = "".join([str(x) for x in soup.find("span", {"id": "lb_tongcach"}).contents])
    lb_danhgia = soup.find("span", {"id": "lb_danhgia"}).text
    m_likes = re.findall('\d*\.?\d+',soup.find("span", {"id": "m_like"}).text)
    m_like = m_likes[0] if len(m_likes) > 0 else 0
    return DetailDB(
        thien_cach=lb_thien,
        nhan_cach=lb_nhan,
        dia_cach=lb_dia,
        ngoai_cach=lb_ngoai,
        tong_cach=lb_tongcach,
        danh_gia=lb_danhgia,
        liked=m_like
    ).dict()