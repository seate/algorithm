from collections import defaultdict

def solution(id_list, report, k):
    reportBy = defaultdict(list)
    for repo in set(report):
        reporter, reported = repo.split()
        reportBy[reported].append(reporter)
    
    disabled = []
    for reported, reporters in reportBy.items():
        if k <= len(reporters): disabled.append(reported)
    
    mailCount = defaultdict(int)
    for d in disabled:
        for reporter in reportBy[d]:
            mailCount[reporter] += 1
    
    return [mailCount[i] for i in id_list]