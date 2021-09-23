class ConsoleException(Exception):
    """Raised when an error occurs and script execution should halt"""
    pass

class ParserException(Exception):
    """Raised when an error occurs during parsing Melon HTML"""
    def __init__(self, error_code: int):
        if(error_code == 808):
            msg = "해당 쿼리로 멜론에서 곡을 찾을 수 없습니다. 다른 키워드로 입력하세요."
        elif(error_code == 800):
            msg = "멜론에 가사 정보가 없습니다."
        else:
            msg = "인터넷 연결을 확인하세요."
        self.message = "{} - {}".format(error_code, msg)
        super().__init__(self.message)