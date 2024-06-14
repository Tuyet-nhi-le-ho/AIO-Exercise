def calc_md_nre(y, y_hat, n, p):

    md_nre = (y**(1/n) - y_hat ** (1/n))**p
    print(f"MD_nRE = {md_nre}")
    return md_nre
