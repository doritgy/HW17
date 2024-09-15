def members_count(membership_param:str) -> int:
    import sqlite3
    conn = sqlite3.connect("comm.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("""SELECT COUNT(*) FROM ecommerce WHERE "membership type" LIKE ?""",
        (membership_param,))
    columns = cursor.fetchall()
    result = [tuple(row) for row in columns]

    return result[0][0]

def main():
    membership_param:str = input("what is the membership type?")
    print(members_count(membership_param))

if __name__ == "__main__":
    main()




