#!/usr/local/bin/python3
__author__="Hongrui"

import asyncio,logging,aiomysql 

def log(sql):
    logging.info('SQL:%s' % sql)

async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host','localhsot'),
        port=kw.get('port',3306),
        user=kw.get('user',"root"),
        pwd=kw.get('password',"root"),
        db=kw["db"],
        charset=kw.get("charset","utf8"),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get("minsize",1),
        loop=loop
    )

async def select(sql,args,size=None):
    log(sql,args)
    global __pool 
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace("?","%s"),args or ())
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
        logging.info('rows returned: %s' % len(rs))
        return rs 
    