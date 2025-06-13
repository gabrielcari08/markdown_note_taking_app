# Importa el módulo 'markdown' que convierte texto Markdown a HTML
import markdown

def render_markdown(text: str) -> str:
    """
    Convierte texto formateado en Markdown a HTML.
    
    Args:
        text (str): Texto en sintaxis Markdown a convertir
        
    Returns:
        str: Texto convertido a HTML con las etiquetas correspondientes
    """
    # Utiliza la función markdown() del módulo para realizar la conversión
    return markdown.markdown(text)