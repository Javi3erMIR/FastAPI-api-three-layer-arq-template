import traceback

from app.services.test_service import TestService
from app.models.test_data import Test
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

router = APIRouter()
test_ser = TestService()


@router.post('/sum-json-body')
async def sumNumbers(test_body: Test):
    """
    Get two numbers un query params and adds it beetween.

    Args:
    - test_body (BaseModel): pydantic obj to hand data with JSON 
      previously declarated in module "models".

    Returns:
    - JSONResponse: with a dict in key "result" with the result of sum.

    Raises:
    - HTTPException: when some code it breask it inside rasies 500 status 
                    code error and "Internal server error".
    """
    try:
        return JSONResponse(content={'result': test_ser.sum_numbers(num_one=test_body.number_one, 
                                                                    num_two=test_body.number_two)})
    except Exception:
        traceback.print_exc()
        return HTTPException(status_code=500, detail='Internal server error.')


@router.get('/sum-query-params')
async def sumNumbers(number_one: float, number_two: float):
    """
    Get two numbers un query params and adds it beetween.

    Args:
    - number_one (int): the value of first number.
    - number_two (int): value if second number.

    Returns:
    - JSONResponse: with a dict in key "result" with the result of sum.

    Raises:
    - HTTPException: when some code it breask it inside rasies 500 status 
                    code error and "Internal server error".
    """
    try:
        return JSONResponse(content={'result': test_ser.sum_numbers(num_one=number_one, 
                                                                    num_two=number_two)})
    except Exception:
        traceback.print_exc()
        return HTTPException(status_code=500, detail='Internal server error.')
