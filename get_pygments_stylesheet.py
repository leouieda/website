"""Generate a pygments CSS stylesheet."""
import pathlib
import pygments.formatters


# Theme included in package accessible-pygments. The theme is originally from
# https://github.com/trallard/pitaya_smoothie
formatter = pygments.formatters.HtmlFormatter(style="pitaya-smoothie")
css = formatter.get_style_defs(".highlight")
output = pathlib.Path("css") / "pygments.css"
output.write_text(css)
