def last_index_of(string):
    idx = 0
    for i in range(len(string)):
        if string[i] == '/':
            idx = i
    return idx

def search(dir_set, path):
    result = set()
    for d in dir_set:
        if d.startswith(path):
            last_index = last_index_of(path)
            print(111, d[last_index:])
            result.add(d[last_index:])
    return result

def solution(directory, command):
    dir_set = set(directory)
    print(dir_set)
    for c in command:
        c_split = c.split()
        if c_split[0] == 'mkdir':
            dir_set.add(c_split[1])
            print(123, dir_set)
        elif c_split[0] == 'cp':
            src, dst = c_split[1:]
            sub_dirs = set()
            for d in dir_set:
                if d.startswith(src):
                    last_index = last_index_of(src)
                    sub_dirs.add(d[last_index:])
            print(1111, sub_dirs)
            sub_dirs = {dst + src if dst != '/' else '' + src for src in sub_dirs}
            print(2222, sub_dirs)
            dir_set.update(sub_dirs)
            print(456, dir_set)
        else:
            dst = c_split[1]
            sub_dirs = set()
            for d in dir_set:
                if d.startswith(dst):
                    sub_dirs.add(d)
            print(1111, sub_dirs)
            dir_set.difference_update(sub_dirs)
            print(789, dir_set)
    answer = sorted([d for d in dir_set])
    return answer

print(solution(["/hello", "/hello/tmp", "/", "/root", "/root/abcd", "/root/abcd/etc", "/root/abcd/hello"], ["mkdir /root/tmp", "cp /hello /root/tmp", "rm /hello"]))
print(solution(["/"], ["mkdir /a", "mkdir /a/b","mkdir /a/b/c", "cp /a/b /",ㅑ "rm /a/b/c"]))