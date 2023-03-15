import sqlite3


class Database:

    def __init__(self, path):
        self.conn = sqlite3.connect(path)

    def selectAll(self, sql, parameters=[]):
        c = self.conn.cursor()
        c.execute(sql, parameters)
        return c.fetchall()

    def select(self, sql, parameters=[]):
        c = self.conn.cursor()
        c.execute(sql, parameters)
        return c.fetchone()

    def execute(self, sql, parameters=[]):
        c = self.conn.cursor()
        c.execute(sql, parameters)
        self.conn.commit()

    def close(self):
        self.conn.close()

    def get_beds(self):
        beds = self.selectAll(
            'select * from beds order by bid asc'
        )

        return [{
            'bid': bed[0],
            'name': bed[1],
            'price': bed[2],
            'user_rating': bed[3],
            'size': bed[4],
            'image': bed[5],
            'available': bed[6]
        } for bed in beds]

    def get_wardrobes(self):
        wardrobes = self.selectAll(
            'select * from wardrobes order by wid asc'
        )

        return [{
            'wid': wardrobe[0],
            'name': wardrobe[1],
            'price': wardrobe[2],
            'user_rating': wardrobe[3],
            'category': wardrobe[4],
            'image': wardrobe[5],
            'available': wardrobe[6]
        } for wardrobe in wardrobes]

    def get_outdoors(self):
        outdoors = self.selectAll(
            'select * from outdoor order by oid asc'
        )

        return [{
            'oid': outdoor[0],
            'name': outdoor[1],
            'price': outdoor[2],
            'user_rating': outdoor[3],
            'category': outdoor[4],
            'image': outdoor[5],
            'available': outdoor[6]
        } for outdoor in outdoors]

    def get_chairs(self):
        chairs = self.selectAll(
            "select * from chairs order by chid asc;"
        )

        return [{
            'chid': chair[0],
            'name': chair[1],
            'price': chair[2],
            'user_rating': chair[3],
            'material': chair[4],
            'image': chair[5],
            'available': chair[6]
        } for chair in chairs]

    def get_desks(self):
        desks = self.selectAll(
            "select * from tables_desks order by tid asc;"
        )

        return [{
            'tid': desk[0],
            'name': desk[1],
            'price': desk[2],
            'user_rating': desk[3],
            'material': desk[4],
            'image': desk[5],
            'available': desk[6]
        } for desk in desks]

    def get_sofas(self):
        sofas = self.selectAll(
            "select * from sofas order by sid asc;"
        )

        return [{
            'sid': sofa[0],
            'name': sofa[1],
            'price': sofa[2],
            'user_rating': sofa[3],
            'material': sofa[4],
            'image': sofa[5],
            'available': sofa[6],
            'no_seats': sofa[7]
        } for sofa in sofas]

    def get_bed(self, bid):
        bed = self.select(f"select * from beds where bid={bid}")
        return {
            'bid': bed[0],
            'name': bed[1],
            'price': bed[2],
            'user_rating': bed[3],
            'size': bed[4],
            'image': bed[5],
            'available': bed[6]
        }

    def get_chair(self, chid):
        chair = self.select(f"select * from chairs where chid={chid}")
        return {
            'chid': chair[0],
            'name': chair[1],
            'price': chair[2],
            'user_rating': chair[3],
            'material': chair[4],
            'image': chair[5],
            'available': chair[6]
        }

    def get_sofa(self, sid):
        sofa = self.select(f"select * from sofas where sid={sid}")
        return {
            'sid': sofa[0],
            'name': sofa[1],
            'price': sofa[2],
            'user_rating': sofa[3],
            'material': sofa[4],
            'image': sofa[5],
            'available': sofa[6],
            'no_seats': sofa[7]
        }

    def get_wardrobe(self, wid):
        wardrobe = self.select(f"select * from wardrobes where wid={wid}")
        return {
            'wid': wardrobe[0],
            'name': wardrobe[1],
            'price': wardrobe[2],
            'user_rating': wardrobe[3],
            'category': wardrobe[4],
            'image': wardrobe[5],
            'available': wardrobe[6]
        }

    def get_desk(self, tid):
        desk = self.select(f"select * from tables_desks where tid={tid}")
        return {
            'tid': desk[0],
            'name': desk[1],
            'price': desk[2],
            'user_rating': desk[3],
            'material': desk[4],
            'image': desk[5],
            'available': desk[6]
        }

    def get_outdoor(self, oid):
        outdoor = self.select(f"select * from outdoor where oid={oid}")

        return {
            'oid': outdoor[0],
            'name': outdoor[1],
            'price': outdoor[2],
            'user_rating': outdoor[3],
            'category': outdoor[4],
            'image': outdoor[5],
            'available': outdoor[6]
        }
