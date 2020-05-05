"""
# @Author         : SYACHUN
# @Date           : 2020-04-25 16:09:39
# @LastEditTime: 2020-04-25 16:39:04
# @LastEditors: SYACHUN
# @Description    : 
# @FilePath       : \FastApi\hello.py
"""

from fastapi import FastAPI
app=FastAPI()
@app.get('/')
def rend_root():
    return {'Hello':'Api'}
