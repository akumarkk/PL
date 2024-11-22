from dataclasses import dataclass, field
import logging
logger = logging.getLogger(__name__)

@dataclass
class Product:
    name:str = field(compare=True)
    category:str = field(compare=True)
    desc:str = field(compare=False)

def main():
    logging.basicConfig(level=logging.INFO)
    mango = Product(name="mango", category="fruits", desc="alphanso mango")
    mexmango = Product(name="mango", category="fruits", desc="mex mango")
    mangmango = Product(name="mangmango", category="fruits", desc="mex mango")

    logger.info(f"mango == mexmango {mexmango == mango}")
    logger.info(f"mango == mangmango {mangmango == mango}")

main()

