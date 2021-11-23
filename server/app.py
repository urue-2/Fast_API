from fastapi import FastAPI, Request
from .model import *
from .connection import *


pjs_server = FastAPI()


@pjs_server.get("/")
async def root():
    return {"message": "这是 基于云的帕金斯慢病监管平台 后端服务器"}


# 注册
# 数据包{“用户名”：“”，“密码”：“”}
@pjs_server.post("/register/")
async def register(requset: Request):
    try:
        data = await  requset.json()
        user_name = data["用户名"]
        password = data["密码"]
        if dbregister(user_name=user_name,passwd=password):
            # return 注册成功的消息
            return ResponseModel(user_name,"register sucessfully")
        else :
            return ResponseModel(user_name,"register failed , user has already existed!")

    except KeyError:
        return ErrorResponseModel("An error occurred.", 500, "Please check the Format of the input data!")

# 登录
# 数据包{“用户名”：“”，“密码”：“”}
@pjs_server.post("/login/")
async def login(requset: Request):
    try:
        data = await  requset.json()
        user_name = data["用户名"]
        passwd = data["密码"]
        if (dblogin(user_name=user_name,passwd=passwd)==1 ):
            #登录成功
            return ResponseModel(user_name,"login sucessfully")
        else :
            #密码错误，登录失败
            return ResponseModel(user_name,"login failed , password is wrong!")
    except KeyError:
        return ErrorResponseModel("An error occurred.", 500, "Please check the Format of the input data!")



# 修改密码 说明：设定为登录之后修改密码，不需要进行身份验证
# 数据包{“用户名”：“”，“新密码”：“”}
@pjs_server.post("/login/change/")
async def change_passwd(requset: Request):
    try:
        data = await  requset.json()
        user_name = data["用户名"]
        new_passwd = data["新密码"]
        if (dbchange_passwd(user_name=user_name,new_passwd=new_passwd)==1 ):
            #修改密码成功
            return ResponseModel(user_name,"change password sucessfully")
        else :
            #修改密码失败
            return ResponseModel(user_name,"change password  failed ")
    except KeyError:
        return ErrorResponseModel("An error occurred.", 500, "Please check the Format of the input data!")


# 插入时序数据
# 数据包{“用户名”：“”，“加速度”：，“时间”：}
@pjs_server.post("/writeaccv/")
async def insert_acc(requset: Request):
    try:
        data = await  requset.json()
        user_name = data["用户名"]
        accv = data["加速度"]
        time = data["时间"]
        if (idbinsert(user_name=user_name,acc_v=accv,time=time)==1 ):
            #加速度插入成功
            return ResponseModel(user_name,"insert accelerated velocity sucessfully")
        else :
            #加速度插入失败
            return ResponseModel(user_name,"insert accelerated velocity failed ")
    except KeyError:
        return ErrorResponseModel("An error occurred.", 500, "Please check the Format of the input data!")




