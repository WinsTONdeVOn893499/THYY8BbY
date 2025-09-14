# 代码生成时间: 2025-09-15 07:26:20
import psycopg2
from psycopg2 import pool
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager

# 数据库配置参数
DB_CONFIG = {
    "dbname": "your_dbname",
    "user": "your_username",
    "password": "your_password",
    "host": "your_host",
    "port": "your_port"
}

# 创建数据库连接池
db_pool = psycopg2.pool.SimpleConnectionPool(1, 10, **DB_CONFIG)

"""
数据库连接池管理器
"""
class DatabasePoolManager():
    def __init__(self):
        """
        初始化数据库连接池
        """
        self.db_pool = db_pool

    @contextmanager
    def get_connection(self):
        """
        获取数据库连接
        """
        try:
            conn = self.db_pool.getconn()
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            yield conn, cursor
        except Exception as e:
            """
            处理连接错误
            """
            print(f"Error getting connection: {e}")
        finally:
            """
            释放连接
            """
            self.db_pool.putconn(conn)

    def execute_query(self, query, params=None):
        """
        执行查询

        Args:
            query (str): SQL查询语句
            params (list): 查询参数

        Returns:
            list: 查询结果
        """
        with self.get_connection() as (conn, cursor):
            try:
                cursor.execute(query, params)
                results = cursor.fetchall()
                return results
            except Exception as e:
                """
                处理查询错误
                """
                print(f"Error executing query: {e}")
                return None
            finally:
                cursor.close()

    def execute_non_query(self, query, params=None):
        """
        执行非查询语句

        Args:
            query (str): SQL非查询语句
            params (list): 非查询参数

        Returns:
            int: 影响行数
        """
        with self.get_connection() as (conn, cursor):
            try:
                cursor.execute(query, params)
                conn.commit()
                return cursor.rowcount
            except Exception as e:
                """
                处理非查询错误
                """
                print(f"Error executing non-query: {e}")
                conn.rollback()
                return None
            finally:
                cursor.close()

# 示例用法
if __name__ == "__main__":
    db_manager = DatabasePoolManager()
    query = "SELECT * FROM your_table"
    results = db_manager.execute_query(query)
    print(results)

    non_query = "INSERT INTO your_table (column) VALUES (%s)"
    affected_rows = db_manager.execute_non_query(non_query, [123])
    print(affected_rows)