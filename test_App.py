import pytest
from app import add, sub, mul, div

def test_add():
  assert add(2,3)==5
  assert add(-1,1)==0
  print("Addition Test Passed")
  
def test_sub():
  assert sub(2,3)==-1
  assert sub(-1,1)==-2
  print("Subtraction Test Passed")

def test_mul():
  assert mul(2,3)==6
  assert mul(-1,1)==-1
  print("Multiplication Test Passed")

def test_div():
  assert div(3,3)==1
  assert div(-1,1)==-1
  print("Addition Test Passed")

if __name__ == "__main__":
   test_add()
   test_sub()
   test_mul()
   test_div()
  print("All Test Passed")
