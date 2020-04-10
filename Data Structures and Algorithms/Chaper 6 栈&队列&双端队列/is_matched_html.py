""" 测试一个HTML文本是否有匹配标签的函数 """

from stack import ArrayStack


def is_matched_html(raw):
    """ Return True if all HTML tags are properly match; False otherwise. """
    S = ArrayStack()
    # find():返回子字符串 sub 在 s[start:end] 切片内被找到的最小索引。 可选参数 start 与 end 会被解读为切片表示法。 如果 sub 未被找到则返回 -1。
    j = raw.find('<')  # find first'<' character
    while j != -1:
        k = raw.find('>', j+1)  # find next '>'
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()
