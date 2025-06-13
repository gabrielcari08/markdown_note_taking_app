# Importa la biblioteca LanguageTool para corrección gramatical
import language_tool_python  

# Crea una instancia del corrector gramatical configurada para español
# Nota: El parámetro 'es' especifica el idioma español
tool = language_tool_python.LanguageTool('es')

def check_text(text: str) -> list:
    """
    Analiza un texto y devuelve una lista de mensajes con errores gramaticales/ortográficos.
    
    Args:
        text (str): Texto a analizar
        
    Returns:
        list: Lista de strings con descripciones de errores encontrados
    """
    
    # Detecta todos los errores gramaticales/ortográficos en el texto
    matches = tool.check(text)
    
    # Convierte cada error encontrado en un mensaje legible y devuelve la lista
    return [match.message for match in matches]