

def calc_f1_score(tp, fp, fn):

    # kiểm tra tp,fp,fn có phải là kiểu int hay không
    if not isinstance(tp, int) or not isinstance(fp, int) or not isinstance(fn, int):
        if not isinstance(tp, int):
            print('tp must be int')
        if not isinstance(fp, int):
            print('fp must be int')
        if not isinstance(fn, int):
            print('fn must be int')
        return
    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than zero')
        return

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2*precision * recall / (precision + recall)
    print(f"precision is {precision}")
    print(f"recall is {recall}")
    print(f"f1_score is {f1_score}")
