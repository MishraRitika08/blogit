import markdown
import bleach
from django import template

register = template.Library()

@register.filter
def render_markdown(text):
    html = markdown.markdown(
        text or "",
        extensions=['extra', 'fenced_code']
    )

    allowed_tags = bleach.sanitizer.ALLOWED_TAGS.union({
    'p', 'h1', 'h2', 'h3', 'h4',
    'pre', 'code', 'hr', 'br',
    'blockquote', 'ul', 'ol', 'li'
})

    return bleach.clean(html, tags=allowed_tags)