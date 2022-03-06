from datetime import datetime

'''
발음하기 쉬운 이름을 사용하라
'''


class DtaRcrd02:
    genymdhms: datetime
    modymdhms: datetime
    pszqint: str = "102"


class Customer:
    """
    위 클래스보다 커뮤니케이션이 훨씬 쉬어진다.
    """
    generationDatetime: datetime
    modificationDatetime: datetime
    recordId: str = "102"
