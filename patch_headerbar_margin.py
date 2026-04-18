import re

with open("/home/thomas/Frontend-css/liqadwaita/src/stylesheet/widgets/_header-bar.scss", "r") as f:
    content = f.read()

# Replace margin: 0 6px; with margin: 15px 4px; and ensure translucent background for the button via extra specificity.
# Also use 16px standard size to honor the PNG.
replacement = """    &.close, &.maximize, &.minimize {
      min-width: 16px;
      min-height: 16px;
      padding: 0;
      margin: 11px 4px;
      border-radius: 9999px;
      background-position: center;
      background-repeat: no-repeat;
      background-size: 16px 16px;

      &, &:hover, &:focus, &:active, &:backdrop {
        background-color: transparent;
        border: none;
        box-shadow: none;
        color: transparent;
      }"""

# Target the block correctly
content = content.replace("""    &.close, &.maximize, &.minimize {
      min-width: 14px;
      min-height: 14px;
      padding: 0;
      margin: 0 6px;
      border-radius: 9999px;
      background-position: center;
      background-repeat: no-repeat;
      background-size: 14px 14px;

      &, &:hover, &:focus, &:active, &:backdrop {
        background-color: transparent;
        border: none;
        box-shadow: none;
        color: transparent;
      }""", replacement)

with open("/home/thomas/Frontend-css/liqadwaita/src/stylesheet/widgets/_header-bar.scss", "w") as f:
    f.write(content)
print("Updated margin and background overrides.")
