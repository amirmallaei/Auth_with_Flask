import os
import pymssql

from dotenv import load_dotenv


def insert_auth(email: str, code: str):
    load_dotenv()
    conn = pymssql.connect(host='185.128.82.62:11433', user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'), database='Consulet')
    cursor = conn.cursor()
    params = (email, code)
    cursor.callproc('insert_auth', params)
    conn.commit()
    cursor.close()
    conn.close()
    return True


def insert_update_jwt(access_token: str, refresh_token: str, email: str):
    load_dotenv()
    conn = pymssql.connect(host='185.128.82.62:11433', user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'), database='Consulet')
    cursor = conn.cursor()
    params = (access_token, refresh_token, email)
    cursor.callproc('UpdateAuth', params)
    conn.commit()
    cursor.close()
    conn.close()
    return True


def get_email(access_token: str):
    load_dotenv()
    conn = pymssql.connect(host='185.128.82.62:11433', user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'), database='Consulet')
    cursor = conn.cursor()
    cursor.execute(f"SELECT Email from auth where  AccessToken = '{access_token}'")
    t = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    if t:
        print(t[0])
        return t[0]
    else:
        # print(t)
        # print(f"This access token '{access_token}' has not email")
        return None


def get_code(email: str):
    load_dotenv()
    conn = pymssql.connect(host='185.128.82.62:11433', user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'), database='Consulet')
    cursor = conn.cursor()
    cursor.execute(f"SELECT VarificationCode from auth where Email = '{email}'")
    t = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    if t:
        print(t[0])
        return t[0]
    else:
        # print(t)
        # print(f"This email '{email}' has not code")
        return None
