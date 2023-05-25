from app.database import get_db
def output_formatter(results):
  out = []
  for result in results:
    res = {
        "id": result[0],
        "summary": result[1],
        "description": result[2],
        "is_active": result[3]
    }
    out.append(res)
  return out

def scan():
  conn = get_db()
  cursor = conn.execute(
    "SELECT * FROM task WHERE is_active=1",
    ()
  )
  results = cursor.fetchall()
  cursor.close()
  return output_formatter(results)

def select_by_id(pk):
  conn = get_db()
  cursor = conn.execute(
    "SELECT * FROM task WHERE is_active=1 AND id=?",
    (pk, )
  )
  results = cursor.fetchall()
  cursor.close()
  return output_formatter(results)[0]

def insert(raw_data):
  conn = get_db()
  conn.execute(
  """
    INSERT INTO task (
      summary,
      description, 
    ) VALUES (
      ?,?
    )
  """,
    (raw_data.get("summary"),
        raw_data.get("description"))
  )
  conn.commit() 

def update(raw_data, pk):
  conn = get_db()
  conn.execute(
  """
    UPDATE task SET
      summary=?,
      description=?,
      is_active=?
    WHERE id=?
  """,
    (raw_data.get("summary"),
        raw_data.get("description"),
        raw_data.get("is_active"),
        pk
    )
  )
  conn.commit() 

def delete(pk):
  conn = get_db()
  conn.execute("DELETE FROM task WHERE id=?", (pk,))
  conn.commit()
