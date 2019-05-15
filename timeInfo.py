import pymysql
import db_auth_config



def add_comm_time_info(addList):

    # 사용이 용이하게 변수로 저장
    login = db_auth_config.gaus_test_db_info

    # MySQL Connection 연결
    conn = pymysql.connect(
        host=login['host'],
        port=login['port'],
        user=login['user'],
        password=login['password'],
        charset=login['charset']
    )

    # Connection 으로부터 Cursor 생성
    curs = conn.cursor()

    query ='INSERT INTO gausad_v2.ga_common_time_info (media_idx, rpt_ymd, tm, keyword, link_url, ranking) VALUES (%s, %s, %s, %s, %s, %s)'

    msg_query= ""

    # 문제가 생길 수도 있기 때문에 예외처리를 해줍니다
    try:
        # insert query를 실행
        curs.execute(query, (addList['media_idx'],addList['rpt_ymd'], addList['tm'], addList['keyword'], addList['link_url'], addList['ranking']))
        # 성공하면 commit() 명령어로 변화를 저장
        conn.commit()
        msg_query="성공"
    except Exception as e:
        # 문제가 생겼으면 롤백
        conn.rollback()
        print("에러가 발생하였습니다." + e)
        msg_query="에러"
    finally:
        # Connection 닫기
        conn.close()

    return msg_query