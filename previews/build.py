"""Build color-only previews of the current MkDocs site into /tmp."""
from pathlib import Path
import shutil
import subprocess

repo = Path(__file__).resolve().parents[1]
output = Path('/tmp/up-proj-palettes')
subprocess.run([
    'uvx', '--from', 'mkdocs-material', 'mkdocs', 'build', '--strict',
    '--site-dir', str(output / 'original'),
], cwd=repo, check=True)

# Background, text, secondary text, border, surface, accent.
palettes = {
    'burgundy': ('#171916', '#d3d0bf', '#a5ab9f', '#383d35', '#21251f', '#b0b8a8'),
    'earth': ('#1d1510', '#d0c6a5', '#aaa183', '#4c3827', '#2b2018', '#c89463'),
    'teal': ('#121e1d', '#ccc6c6', '#9caeaa', '#2f5755', '#1b302e', '#79b1ab'),
    'navy': ('#20283e', '#cbbcb2', '#aea196', '#4b4037', '#262f46', '#cba995'),
}
for name, (bg, text, muted, border, surface, accent) in palettes.items():
    target = output / name
    shutil.copytree(output / 'original', target, dirs_exist_ok=True)
    css = target / 'stylesheets/extra.css'
    css.write_text(css.read_text() + f'''
/* Preview only: colors change; the site layout remains identical. */
[data-md-color-scheme] {{
    --md-default-bg-color: {bg};
    --md-default-fg-color: {text};
    --md-default-fg-color--light: {muted};
    --md-default-fg-color--lighter: {muted};
    --md-default-fg-color--lightest: {border};
    --md-primary-fg-color: {bg};
    --md-primary-fg-color--light: {surface};
    --md-primary-fg-color--dark: {bg};
    --md-primary-bg-color: {text};
    --md-primary-bg-color--light: {muted};
    --md-accent-fg-color: {accent};
    --md-accent-bg-color: {bg};
    --md-code-bg-color: {surface};
    --md-code-fg-color: {text};
    --md-footer-bg-color: {bg};
    --md-footer-bg-color--dark: {bg};
    --md-footer-fg-color: {text};
    --md-typeset-color: {text};
    --md-typeset-a-color: {accent};
    background-color: {bg} !important;
    color: {text} !important;
}}
.md-header__button.md-logo:focus-visible {{ outline-color: {accent}; }}
/* Override Material's scheme-specific link color, including visited links. */
[data-md-color-scheme] .md-typeset a,
[data-md-color-scheme] .md-typeset a:visited {{ color: {accent}; }}
[data-md-color-scheme] .md-typeset a:hover,
[data-md-color-scheme] .md-typeset a:focus-visible {{ color: {text}; }}

''')
    if name == 'burgundy':
        with css.open('a') as stylesheet:
            stylesheet.write("\n.md-tabs__item--active .md-tabs__link { text-decoration: underline; text-decoration-color: #b0b8a8; text-decoration-thickness: 2px; text-underline-offset: 6px; }\n")
    for asset in ['up-projection-logo.svg', 'up-projection.svg']:
        svg = target / 'assets' / asset
        svg.write_text(svg.read_text().replace('#fff', accent).replace('fill="#000"', f'fill="{bg}"'))
shutil.copyfile(repo / 'previews/palettes.html', output / 'index.html')
print(f'Previews ready: {output}')
