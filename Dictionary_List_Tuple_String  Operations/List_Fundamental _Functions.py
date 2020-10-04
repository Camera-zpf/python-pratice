name_list = ["张三", "李四", "王五", "王五", "王五", "王五"]

# 取列表元素用[]
print(name_list[0])
name_list[0] = "张三二"
# 添加元素用append  Append object to the end of the list.
name_list.append("海六")

# 显示list类型
print(type(name_list))

# 打印整个list
print(name_list)

# 将另一个列表中的元素逐个添加到列表一中  Extend list by appending elements from the iterable.
name_list2 = ["李琦", "大梅"]
name_list.extend(name_list2)
print(name_list)
# 在列表指定位置插入元素  Insert object before index
name_list.insert(0, "赵鹏飞")
print(name_list)

# -----------------统计-----------------------------
# 输出元素”王五“出现的次数  Return number of occurrences of value.
print("王五出现 %d 次" % name_list.count("王五"))
print("列表的长度为%d " % len(name_list))
# --------------------排序-------------------------
# Stable sort IN PLACE. 默认升序排列，参数recerse=True时降序排序
name_list.sort()
print("------升序排列------")
print(name_list)

name_list.sort(reverse=True)
print("------降序排列------")
print(name_list)

print("------降序排列的逆序------")
name_list.reverse()  # Reverse IN PLACE. 逆序，反转
print(name_list)

# -------------------------------------------------
# -------------------删除元素-----------------------
# "del" target_list 删除指定元素或列表
del name_list[0]
print(name_list)

# Remove first occurrence of value. 删除首次出现的元素
# Raises ValueError if the value is not present. 如果元素不存在则报值错误
name_list.remove("王五")
print(name_list)

# Remove and return item at index (default last). 删除元素（默认最后一个元素）并返回其本身
# Raises IndexError if list is empty or index is out of range.如果元素不存在则报索引错误或超出
name_list.pop()
name_list.pop(3)
print(name_list)
# 清空list  Remove all items from list.
name_list.clear()
print(name_list)  # 空list
