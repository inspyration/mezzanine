from django.forms.widgets import Widget, Input


class TitleWidget(Widget):
    def render(self, name, value, attrs=None, renderer=None):
        return f'<h3 class="form-title">{value}</h3>'


class NoteWidget(Input):
    input_type = "range"
    template_name = "pages/forms/widgets/range.html"

    def __init__(self, attrs=None, min_value=1, max_value=5, step=1):
        super().__init__(attrs=attrs)
        value = self.attrs.get("value", min_value)
        self.attrs |= {
            "min": min_value,
            "max": max_value,
            "step": step,
            "value": value,
        }
