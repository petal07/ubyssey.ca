from dispatch.theme import register
from dispatch.theme.templates import Template
from dispatch.theme.fields import SelectField, CharField, TextField, ArticleField, DateTimeField

@register.template
class Default(Template):
    id = 'default'
    name = 'Default'

    IMAGE_SIZE_OPTIONS = (
        ('default', 'Default'),
        ('full', 'Full')
    )

    image_size = SelectField('Image Size', options=IMAGE_SIZE_OPTIONS)

@register.template
class Blank(Template):
    id = 'blank'
    name = 'Blank'


@register.template
class FullWidth(Template):
    id = 'fw-story'
    name = 'Full width story'

    IMAGE_SIZE_OPTIONS = (
        ('default', 'Default'),
        ('full', 'Full')
    )

    HEADER_LAYOUT_OPTIONS = (
        ('right-image', 'Right Image'),
        ('top-image', 'Top Image'),
        ('banner-image', 'Banner Image')
    )

    description = TextField('Description')
    image_size = SelectField('Image Size', options=IMAGE_SIZE_OPTIONS)
    header_layout = SelectField('Header Layout', options=HEADER_LAYOUT_OPTIONS)

@register.template
class Guide(Template):
    id = 'guide-to-ubc'
    name = 'Guide to UBC'

    subheading = CharField('Sub-heading')
    intro = TextField('Intro text')
    next_a = CharField('Up next A')
    next_b = CharField('Up next B')

@register.template
class Magazine(Template):
    id = 'magazine'
    name = 'Magazine - Article'

    COLOR_OPTIONS = (
        ('green', 'Green'),
        ('pink', 'Pink'),
        ('blue', 'Blue')
    )

    DISPLAY_OPTIONS = (
        ('default', 'Default'),
        ('basic', 'Basic')
    )

    byline = TextField('Byline')
    byline_2 = TextField('Byline 2')
    description = TextField('Description')
    color = SelectField('Accent Color', options=COLOR_OPTIONS)
    display = SelectField('Display type', options=DISPLAY_OPTIONS)

@register.template
class MagazinePoem(Template):
    id = 'magazine-poem'
    name = 'Magazine - Poem'

    byline = TextField('Byline')
    byline_2 = TextField('Byline 2')
    top_color = CharField('Top Color')
    bottom_color = CharField('Bottom Color')
    text_color_a = CharField('Text Color A')
    text_color_b = CharField('Text Color B')
    offset = CharField('Top Offset')

@register.template
class VoteCompass(Template):
    id = 'vote-compass'
    name = 'Vote Compass'

    css = CharField('CSS')
    js = CharField('JavaScript')

@register.template
class OneYearLater(Template):
    id = 'one-year-later'
    name = 'Feature: One Year Later'

    title = CharField('Title')
    subtitle = CharField('Subtitle')
    snippet = TextField('Snippet')
    video_src = CharField('Video Source File')
    next_article = ArticleField('Preview Article')
    next_title = CharField('Preview Title')
    next_snippet = TextField('Preview Snippet')

    article_then = ArticleField('Then Article')
    article_now = ArticleField('Now Article')
    article_next = ArticleField('Next Article')

    about = TextField('About')

@register.template
class Timeline(Template):
    id = 'timeline'
    name = 'Timeline'

    IMAGE_SIZE_OPTIONS = (
        ('default', 'Default'),
        ('full', 'Full')
    )

    HEADER_LAYOUT_OPTIONS = (
        ('right-image', 'Right Image'),
        ('top-image', 'Top Image'),
        ('banner-image', 'Banner Image')
    )

    description = TextField('Description')
    image_size = SelectField('Image Size', options=IMAGE_SIZE_OPTIONS)
    timeline_date = DateTimeField('Timeline Date')
    header_layout = SelectField('Header Layout', options=HEADER_LAYOUT_OPTIONS, required=True)
