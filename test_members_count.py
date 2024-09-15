import pytest
import HW17_bonus
import sqlite3
@pytest.fixture
def before_after_operations_db():
    global cursor
    # BEFORE
    conn = sqlite3.connect("comm.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    yield  # test_get_years

    # AFTER
    cursor.close()

def test_members_count_gold(before_after_operations_db):
    global cursor
    cursor.execute("""SELECT COUNT(*) FROM ecommerce WHERE "membership type" LIKE "Gold" """)
    columns = cursor.fetchall()
    result = [tuple(row) for row in columns]
    expected = result[0][0]
    actual =  HW17_bonus.members_count("Gold")
    assert expected == actual

def test_members_count_silver(before_after_operations_db):
    global cursor
    cursor.execute("""SELECT COUNT(*) FROM ecommerce WHERE "membership type" LIKE "Silver" """)
    columns = cursor.fetchall()
    result = [tuple(row) for row in columns]
    expected = result[0][0]
    actual =  HW17_bonus.members_count("Silver")
    assert expected == actual

def test_members_count_bronze(before_after_operations_db):
    global cursor
    cursor.execute("""SELECT COUNT(*) FROM ecommerce WHERE "membership type" LIKE "Bronze" """)
    columns = cursor.fetchall()
    result = [tuple(row) for row in columns]
    expected = result[0][0]
    actual =  HW17_bonus.members_count("Bronze")
    assert expected == actual

