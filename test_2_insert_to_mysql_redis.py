"""
生成200个激活码，插入到mysql或redis数据库中:
1.mysql.connector用法
2.调用gen_random_str()函数，生成激活码，
3.循环调用，将列表中的激活码插入到数据库中
4.加入了一些异常处理机制
"""

import mysql.connector
from mysql.connector import Error
from test_1_gen_code import gen_code_list
import redis

def mysql_connect():
    try:
        mydb = mysql.connector.connect(
            host="",
            user="",
            passwd="",
            database="test"
        )
    except Error as e:
        print(f"someting went wrong: {e}")
        exit(1)

    mycursor = mydb.cursor()
    return mydb, mycursor

def insert_activation_code(num=200):
    mydb, mycursor = mysql_connect()
    try:
        code_list = gen_code_list(num)
        for i, activation_code in enumerate(code_list):
            try:
                mycursor.execute("insert into activation_codes (code) values (%s)", (activation_code,))
                if (i + 1) % 100 == 0:  # 每 100 条提交一次
                    mydb.commit()
            except Error as e:
                print(f"插入数据时发生错误: {e}")
                mydb.rollback()
                continue
        mydb.commit()  # 提交剩余的记录
        print(f"{num}个激活码插入成功！")
    except Error as e:
        print(f"生成激活码时发生错误: {e}")
        mydb.rollback()
    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()

def redis_connect():
    r = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True) 
    return r


def insert_activation_code_to_redis(num=200):
    r = redis_connect()
    try: 
        code_list = gen_code_list(num)
        for i, activation_code in enumerate(code_list):  # 只提取激活码值
            try:
                r.sadd('activation_codes', activation_code)  # 插入激活码
            except Exception as e:
                print(f"插入数据时发生错误: {e}")
                continue
        print(f"{num}个激活码插入成功！")
    except Exception as e:
        print(f"生成激活码时发生错误: {e}")




if __name__ == '__main__':
    insert_activation_code_to_redis()





"""
pip install mysql_connector_python

mysql commit() 方法详解
mydb.commit()

的作用是将当前事务的更改提交到数据库。它是数据库事务的一部分，用于确保数据的持久性。以下是详细说明：

1. mydb.commit() 的作用
commit() 方法会将当前事务中的所有更改保存到数据库中。事务是数据库操作的一个逻辑单元，通常包括一组插入、更新或删除操作。只有在调用 commit() 后，这些更改才会真正生效并对其他数据库用户可见。

例如：

确保插入操作被保存到数据库
如果不调用 commit()，这些更改会保留在事务中，但不会被写入数据库。这意味着：

如果程序结束或连接关闭，未提交的更改会被回滚（撤销）。
其他用户无法看到这些更改。
2. 如果不调用 commit() 会怎么样？
更改不会生效：未提交的更改不会保存到数据库中，程序结束后会被回滚。
数据一致性问题：如果程序崩溃或连接断开，未提交的事务会被自动回滚，可能导致预期的更改丢失。
无法共享更改：其他数据库连接无法看到未提交的更改。
3. 是否需要将 commit() 放在循环内？
在你的代码中，commit() 被放在循环内：

)
优点：
每次插入后立即提交，确保每条记录都被保存，即使中途程序崩溃，已提交的记录不会丢失。
避免长时间持有事务锁，减少对其他数据库操作的影响。
缺点：
性能较差：每次调用 commit() 都会触发一次磁盘写操作，频繁提交会显著降低性能。
数据一致性风险：如果某些插入失败，可能会导致部分数据提交，部分数据未提交。
改进建议：
将 commit() 移到循环外，统一提交所有插入操作：

优点：
提高性能：减少磁盘写操作的次数。
保证事务的原子性：要么所有插入都成功，要么全部回滚。
注意事项：
如果数据量非常大，可能会导致事务过大，影响性能或引发内存问题。此时可以考虑分批提交，例如每 100 条记录提交一次：
总结
mydb.commit() 用于提交事务，确保更改被保存到数据库。
如果不调用 commit()，更改不会生效，程序结束后会被回滚。
建议将 commit() 放在循环外，以提高性能并保证事务的原子性。如果数据量大，可以分批提交。
"""


"""
pip install redis
redis-py
r.sadd(name, values)

redis.StrictRedis()
StrictRedis 类是 redis-py 的主要类，用于与 Redis 服务器进行交互。sadd() 方法是 StrictRedis 类的一个方法，用于向 Redis 集合中添加一个或多个元素。

"""
