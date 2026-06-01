import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if '<div style="display: flex; gap: 8px; margin-bottom: 16px;">' in line:
        skip = True
    
    if skip and '<div id="calculator-v2" style="display: none;">' in line:
        skip = False
        new_lines.append('  <div id="calculator-v2">\n')
        continue
        
    if not skip:
        if '<div class="version-badge">v1.0' in line:
            new_lines.append('    <div class="version-badge">v1.1 &middot; 2026</div>\n')
        else:
            new_lines.append(line)

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.writelines(new_lines)
