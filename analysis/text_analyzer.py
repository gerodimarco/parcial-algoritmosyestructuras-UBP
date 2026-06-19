class TextAnalyzer:
    """
    Utilidades para análisis básico de texto.
    """

    @staticmethod
    def contains_pattern(text, pattern):
        """
        Verifica si un patrón existe dentro de un texto.
        """

        return pattern.lower() in text.lower()

    @staticmethod
    def count_occurrences(text, pattern):
        """
        Cuenta ocurrencias de un patrón.
        """

        return text.lower().count(pattern.lower())

    @staticmethod
    def text_length(text):
        """
        Retorna longitud del texto.
        """

        return len(text)