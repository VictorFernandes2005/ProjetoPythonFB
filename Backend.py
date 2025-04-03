import sqlite3 as sql

class TransactionObject():
    database = "clientes.db"
    conn = None
    cur = None
    connected = False

    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql, parms = None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql,parms)
            return True
        else:
            return False
        
    def fetchAll(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False
    
def initDB():
    trans = TransactionObject()
    trans.connect()

    trans.execute("create table if not exists cliente(id integer primary key autoincrement, nome text, sobrenome text, email text, cpf text)")
    trans.persist()
    trans.disconnect()

def insert(nome,sobrenome,email,cpf):
    trans = TransactionObject()
    trans.connect()
    trans.execute("insert into cliente(nome,sobrenome,email,cpf) values (?,?,?,?)",(nome,sobrenome,email,cpf))
    trans.persist()
    trans.disconnect()

def view():
    trans = TransactionObject()
    trans.connect()
    trans.execute("select * from cliente")
    rows = trans.fetchAll()
    trans.disconnect()
    return rows

def search(nome="",sobrenome="",email="",cpf=""):
    trans = TransactionObject()
    trans.connect()
    trans.execute("select * from cliente where nome = ? or sobrenome = ? or email = ? or cpf = ?",
                (nome,sobrenome,email,cpf))
    rows = trans.fetchAll()
    trans.disconnect()
    return rows

def delete(id):
    trans = TransactionObject()
    trans.connect()
    trans.execute("delete from cliente where id = ?",id)
    trans.persist()
    trans.disconnect()

def update(id, nome, sobrenome, email, cpf):
    trans = TransactionObject()
    trans.connect()
    trans.execute("update cliente set nome = ?, sobrenome = ?, email = ?, cpf = ? where id = ?",(nome,sobrenome,email,cpf,id))
    trans.persist()
    trans.disconnect()

initDB()