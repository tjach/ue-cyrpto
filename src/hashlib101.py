import hashlib as hl
import logging

logger = logging.getLogger("hashing")
logging.basicConfig(level=logging.DEBUG)

md5_col_1 = "4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa200a8284bf36e8e4b55b35f427593d849676da0d1555d8360fb5f07fea2"

md5_col_2 = "4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa202a8284bf36e8e4b55b35f427593d849676da0d1d55d8360fb5f07fea2"


def intro():
    msg = "Marry had a little lambb".encode()
    out = hl.sha1()
    out.update(msg)
    logger.info(out.hexdigest())


def colisions():
    dig_1 = hl.md5(bytearray.fromhex(md5_col_1)).hexdigest()
    dig_2 = hl.md5(bytearray.fromhex(md5_col_2)).hexdigest()
    logger.info(f"First digest: {dig_1}")
    logger.info(f"Second digest: {dig_2}")


def hmac_test():
    out = hl.pbkdf2_hmac("sha256", "password".encode(), "salt".encode(), 10000).hex()
    logger.info(f"HMAC out: {out}")



if __name__ == "__main__":
    intro()
    colisions()
    hmac_test()