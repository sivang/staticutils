#!/usr/bin/env python
import lxml.html
import sys


# doc.xpath("//node()[@src]") - gets elements not just strings

def staticize(content):
    doc = lxml.html.fromstring(content)
    srcs = doc.xpath("//@src")
    srcs = [s for s in srcs if not s.startswith('http') and not s.startswith("{%")]
    srcs = set(srcs)
    for src in srcs:
        rewrite_with = None
        rewrite_with = "{% static '" + src + "' %}"
        if not src.startswith("{% static"):
            content = content.replace(src, rewrite_with)
    return content


if __name__ == '__main__':
    content = None
    with open(sys.argv[1], 'r') as f:
        content = f.read()
    new_content = staticize(content)
    with open(sys.argv[1] + '_static', 'w') as f:
        f.write(new_content)

