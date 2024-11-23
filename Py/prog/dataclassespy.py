from dataclasses import dataclass, field
import random
import logging
logger = logging.getLogger(__name__)

@dataclass
class Product:
    # static var
    stat = "cal"
    name:str = field(compare=True)
    category:str = field(compare=True)
    desc:str = field(compare=False)

    # def __init__(self):
    #     self.pid = random.random()


def main():
    logging.basicConfig(level=logging.INFO)
    mango = Product(name="mango", category="fruits", desc="alphanso mango")
    mexmango = Product(name="mango", category="fruits", desc="mex mango")
    mangmango = Product(name="mangmango", category="fruits", desc="mex mango")

    logger.info(f"mango == mexmango {mexmango == mango}")
    logger.info(f"mango == mangmango {mangmango == mango}")

    logger.info(Product.stat)
    logger.info(mango.stat)
    mango.stat = 'change'
    logger.info(Product.stat)
    logger.info(mango.stat)
    Product.stat = 'change1'
    logger.info(Product.stat)
    logger.info(mango.stat)
main()


class Prod:
    class_var = 10

p1 = Prod()
p2= Prod()
logger.info(f"p1 = {p1.class_var} p2 = {p2.class_var} {Prod.class_var}")
p1.class_var=20
p2.class_var=200
logger.info(f"p1 = {p1.class_var} p2 = {p2.class_var} {Prod.class_var}")

Prod.class_var=100
logger.info(f"p1 = {p1.class_var} p2 = {p2.class_var} {Prod.class_var}")

Prod.class_var=110
logger.info(f"p1 = {p1.class_var} p2 = {p2.class_var} {Prod.class_var}")