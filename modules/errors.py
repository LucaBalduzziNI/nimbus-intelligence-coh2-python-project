class IpCantBeResolved(Exception):
    """Exception raised if the given ip is does not resolve to any existing one"""
    
    def __init__(self, ip: str, *args):
        super().__init__(args)
        self.ip = ip

    def __str__(self) -> str:
        return f'The ip {self.ip} does not resolve to any existing one!'
    
class LanguageCantBeTranslated(Exception):
    """Exception raised if the given language can't be translated"""

    def __init__(self, language: str, *args):
        super().__init__(args)
        self.language = language
    
    def __str__(self) -> str:
        return f'Language {self.language} can\'t be translated!'

class LanguageCantBeSpoken(Exception):
    """Exception raised if the given language can't be spoken"""
    
    def __init__(self, language: str, *args):
        super().__init__(args)
        self.language = language
    
    def __str__(self) -> str:
        return f'Language {self.language} can\'t be spoken!' 
