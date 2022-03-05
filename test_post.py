
import time
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Request(BaseModel) :
	inputStr: str


app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins = ['*'], allow_credentials = True, allow_methods = ['*'], allow_headers = ['*'])

nowTime_1 = time.time()

@app.post('/test')
async def ParseInput(userRequest: Request) :

	requestInfo = {
					'inputStr': userRequest.inputStr+"hihi",
				  }

	return requestInfo


if __name__ == '__main__' : uvicorn.run('test_post:app', reload = True, host = '0.0.0.0', port = 9527)

