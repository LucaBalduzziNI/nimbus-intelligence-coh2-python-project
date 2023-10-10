class APITranslationError(Exception):
    """Exception raised if there has been a failure by the API during translation"""

    def __init__(self, source_lang: str, target_lang: str, *args):
        super().__init__(args)
        self.source_lang = source_lang
        self.target_lang = target_lang
    
    def __str__(self):
        return f'Failure from the API while translating {self.source_lang} to {self.target_lang}!'

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

class TextIsBlank(Exception):
    """Exception raised if the text for the TTS is blank"""

    def __init__(self, *args):
        super().__init__(args)
    
    def __str__(self):
        return 'The provided text to translate is blank!'


class LanguageCantBeSpoken(Exception):
    """Exception raised if the given language can't be spoken"""
    
    def __init__(self, language: str, *args):
        super().__init__(args)
        self.language = language
    
    def __str__(self) -> str:
        return f'Language {self.language} can\'t be spoken!' 
    
class TextTypeIsAlreadyStored(Exception):
    """Exception raised if trying to insert a duplicated text type"""

    def __init__(self, text: str, *args):
        super().__init__(args)
        self.text = text
    
    def __str__(self) -> str:
        return f'The Text "{self.text}" is already stored in the DB!'
