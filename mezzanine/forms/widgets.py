from django.forms.widgets import Widget, Input


class TitleWidget(Widget):
    def render(self, name, value, attrs=None, renderer=None):
        return f'<h3 class="form-title">{value}</h3>'


class RangeWidget(Input):
    input_type = "range"
    template_name = "pages/forms/widgets/range.html"

    def __init__(self, attrs=None):
        super().__init__(attrs=attrs)

    def set_choices(self, choices):
        try:
            choices = {int(k.strip()): v.strip() for k, v in choices.split("-")}
        except:
            choices = {1: "Syntax error"}

        min_value = min(choices)
        max_value = max(choices)
        step = 1

        value = self.attrs.get("value", min_value)
        self.attrs |= {
            "min": min_value,
            "max": max_value,
            "step": step,
            "value": value,
        }
