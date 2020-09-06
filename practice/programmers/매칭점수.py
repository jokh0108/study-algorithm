from pprint import pprint
def count(line, word):
    d = len(word)
    cnt = 0
    for i in range(len(line)-d+1):
        if line[i:i+d] == word:
            if i > 0 and line[i-1].isalpha():
                continue
            if i+d < len(line) and line[i+d].isalpha():
                continue
            cnt += 1

    return cnt

def solution(word, pages):
    word = word.lower()
    page_info = {}
    page_arr = []
    for page in pages:
        page_lower = page.lower()
        page_lower_split = page_lower.split('\n')
        url = ''
        external_link = []
        score = 0
        for line in page_lower_split:
            line_trimed = line.strip()
            print(line_trimed)
            if line_trimed.startswith('<meta property="og:url'):
                i = line_trimed.find('https://')
                j = i
                while line_trimed[j] != '"':
                    j += 1
                url = line_trimed[i:j]
                page_arr.append(url)
                page_info.update({url: {}})
                print(page_info, 456)
            elif '<a href=' in line_trimed:
                copied = line_trimed
                while copied:
                    i = copied.find('https://')
                    if i == -1:
                        break
                    j = i
                    while copied[j] != '"':
                        j += 1
                    external_link.append(copied[i:j])
                    copied = copied[j:]
            score += count(line, word)
        page_info[url].update({
            'external_link': external_link,
            'score': score,
            'link_score': 0,
            'match_score': 0
        })
    print(234, page_info)
    for info in page_info.values():
        cnt = len(info['external_link'])
        for link in info['external_link']:
            if link not in page_info:
                continue
            page_info[link]['link_score'] += info['score'] / cnt
    for info in page_info.values():
        info['match_score'] = info['score'] + info['link_score']
    print(456, page_info)
    pprint(page_info)
    page_index_match_score = [(idx, page_info[url]['match_score']) for idx, url in enumerate(page_arr)]
    answer = sorted(page_index_match_score, key=lambda x: (-x[1], x[0]))
    print(answer)
    return answer[0][0]

print(solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))