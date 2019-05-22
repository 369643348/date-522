import re
#唱歌跳舞

pattern = r'(?P<yeah>ab)cd(?P<combo>ef)'

regex = re.compile(pattern)

obj = regex.search('abcdefosmer')


print(obj.pos)#开头位置
print(obj.endpos)#结束位置
print(obj.re)
print(obj.expand)
print(obj.string)

print(obj.group())
print(obj.groups())
print(obj.groupdict())
print(obj.span())
print(obj.start())
print(obj.end())

