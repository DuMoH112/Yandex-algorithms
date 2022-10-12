import os
import sys

sys.path.append(os.getcwd())
from tools import test


def principal_period(string: str) -> str:
    idx = (string+string).find(string, 1, -1)
    return None if idx == -1 else string[:idx]


def repeat(string: str) -> int:
    prefix = principal_period(string)
    return len(string.replace(prefix, '1')) if prefix else 1


def main():
    print(repeat(input()))


tests = [
    {"test": "zzzzzz", "answer": 6},
    {"test": "zzz", "answer": 3},
    {"test": "abacaba", "answer": 1},
    {"test": "abababab", "answer": 4},
    {"test": "abcabcabc", "answer": 3},
    {"test": "zzzzcccc", "answer": 1},
    {"test": "eeezeeezeeezeeez", "answer": 4},
    {"test": "eeeeeeoeeeeeeeeeoeee", "answer": 2},
    {"test": "nzsrnsrlhsahnsdnltvrtzsnihejvnoqpeamozgclamtrrfdsfztkcodhvsplzkcpsdidetsejyebodjnwxrsjwgppaogwropeputtzfyqqbjbpaaiiqndacflbslchoawezwwirueykamtrognmfmjacnbxcnlzcpuvfimwmbuqofbgmhpbshdzvlhenedkaqqxzmkkzzfwcjepcfuicfhummsjbjcreujrudoenajgbbvwdgnwahmqduyjcswqjebzudvufwoetiltmzhdtomlfpepwzwmvzrrnazfkgfriqadnmnzsrnsrlhsahnsdnltvrtzsnihejvnoqpeamozgclamtrrfdsfztkcodhvsplzkcpsdidetsejyebodjnwxrsjwgppaogwropeputtzfyqqbjbpaaiiqndacflbslchoawezwwirueykamtrognmfmjacnbxcnlzcpuvfimwmbuqofbgmhpbshdzvlhenedkaqqxzmkkzzfwcjepcfuicfhummsjbjcreujrudoenajgbbvwdgnwahmqduyjcswqjebzudvufwoetiltmzhdtomlfpepwzwmvzrrnazfkgfriqadnmnzsrnsrlhsahnsdnltvrtzsnihejvnoqpeamozgclamtrrfdsfztkcodhvsplzkcpsdidetsejyebodjnwxrsjwgppaogwropeputtzfyqqbjbpaaiiqndacflbslchoawezwwirueykamtrognmfmjacnbxcnlzcpuvfimwmbuqofbgmhpbshdzvlhenedkaqqxzmkkzzfwcjepcfuicfhummsjbjcreujrudoenajgbbvwdgnwahmqduyjcswqjebzudvufwoetiltmzhdtomlfpepwzwmvzrrnazfkgfriqadnm", "answer": 3},
    {"test": "iibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibiiibi", "answer": 230},
    {"test": "vvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuvvvvvvvuv", "answer": 104},
]

if __name__ == '__main__':
    for idx, row in enumerate(tests):
        test(repeat, idx, row['answer'], [row['test']])
