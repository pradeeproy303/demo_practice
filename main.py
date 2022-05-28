from addition import add
from multiplication import mul

if __name__ == "__main__":
    x=input("Enter a integer")
    y=input("Enter a integer")

    res_add = add(x,y)
    print(f"The result of addition is: {res_add}")

    res_mul = mul(x,y)
    print(f"The result of multiplication  is: {res_mul}")
