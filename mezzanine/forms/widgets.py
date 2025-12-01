from django.forms.widgets import Widget, Input


class TitleWidget(Widget):
    def render(self, name, value, attrs=None, renderer=None):
        return f'<h3 class="form-title">{value}</h3>'


class NoteWidget(Input):
    input_type = "range"
    template_name = "pages/forms/widgets/range.html"

    def __init__(self, attrs=None, choices=()):
        super().__init__(attrs=attrs)
        try:
            if len(choices):
                self.choices = {1: "No choices"}
            else:
                self.choices = {int(k.strip()): v.strip() for k, v in choices.split("-")}
        except:
            self.choices = {1: "Syntax error in choices"}
        value = self.attrs.get("value", (min_value := min(self.choices)))
        self.attrs |= {
            "min": min_value,
            "max": max(self.choices),
            "step": 1,
            "value": value,
        }
