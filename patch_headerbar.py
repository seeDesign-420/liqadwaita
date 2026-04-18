import re

with open("/home/thomas/Frontend-css/liqadwaita/src/stylesheet/widgets/_header-bar.scss", "r") as f:
    content = f.read()

replacement = """windowcontrols {
  border-spacing: 6px;

  &.start {
    margin-right: 6px;
  }

  &.end {
    margin-left: 6px;
  }

  > .icon {
    margin: 9px;
  }
}

headerbar windowcontrols {
  button,
  button.image-button {
    > image {
      padding: 0;
      margin: 0;
      background-color: transparent;
      background-image: none;
      color: transparent;
    }

    &.close, &.maximize, &.minimize {
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
      }

      &:backdrop { opacity: 1; }
    }

    @each $k in ('close', 'maximize', 'minimize') {
      @each $l, $m in ('',''), (':backdrop','-backdrop'), (':backdrop:hover','-backdrop-hover'), (':hover','-hover'), (':active','-active') {
        &.#{$k}#{$l} {
          background-image: -gtk-scaled(url('assets/windows-assets/titlebutton-#{$k}#{$m}.png'),
                                        url('assets/windows-assets/titlebutton-#{$k}#{$m}@2.png'));
                                        
          @media (prefers-color-scheme: dark) {
            background-image: -gtk-scaled(url('assets/windows-assets/titlebutton-#{$k}#{$m}-dark.png'),
                                          url('assets/windows-assets/titlebutton-#{$k}#{$m}-dark@2.png'));
          }
        }
      }
    }
  }
}"""

# Find the block from 'windowcontrols {' to the end of 'headerbar windowcontrols { ... }'
pattern = re.compile(r"windowcontrols \{\s*border-spacing: 6px;.*?>\s*image\s*\{.*?\n\s*\}\s*\}\s*\}", re.DOTALL)
if pattern.search(content):
    new_content = pattern.sub(replacement, content)
    with open("/home/thomas/Frontend-css/liqadwaita/src/stylesheet/widgets/_header-bar.scss", "w") as f:
        f.write(new_content)
    print("Patched successfully via regex.")
else:
    print("Could not find block to patch.")
