"""Render one markdown copy-draft file into a styled standalone HTML page.

Minimal markdown: H1, H2, **bold** leads, [CTA] brackets, plain paragraphs.
No .format() on the template (the CSS has literal braces) -- string concat only.

    python render_copy.py <md-path> <html-path> <label> <theme>
    theme: coastal | software
"""
import re
import sys
from pathlib import Path

THEMES = {
    "coastal": {
        "bg": "#F2EFE7", "fg": "#1B2320", "muted": "#5E6B62", "line": "#D8D3C4",
        "accent": "#2F5D50", "body_font": '"Source Serif 4",Georgia,serif',
        "head_font": '"Schibsted Grotesk",system-ui,sans-serif',
    },
    "software": {
        "bg": "#F6F6F4", "fg": "#15171A", "muted": "#63666D", "line": "#DEDFDB",
        "accent": "#1D4ED8", "body_font": '"Inter",system-ui,sans-serif',
        "head_font": '"Inter",system-ui,sans-serif',
    },
}


def inline(s: str) -> str:
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]", r'<span class="btn">\1</span>', s)
    return s


def render_body(md: str) -> str:
    lines = md.replace("\r\n", "\n").split("\n")
    out = []
    para = []
    list_open = False

    def flush_para():
        nonlocal para
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para = []

    def close_list():
        nonlocal list_open
        if list_open:
            out.append("</ul>")
            list_open = False

    for raw in lines:
        line = raw.strip()
        if not line:
            flush_para()
            continue
        if line.startswith("# "):
            flush_para(); close_list()
            out.append("<h1>" + inline(line[2:]) + "</h1>")
        elif line.startswith("## "):
            flush_para(); close_list()
            out.append("<h2>" + inline(line[3:]) + "</h2>")
        elif line.startswith("- ") or line.startswith("* "):
            flush_para()
            if not list_open:
                out.append("<ul>")
                list_open = True
            out.append("<li>" + inline(line[2:]) + "</li>")
        else:
            close_list()
            para.append(line)
    flush_para()
    close_list()
    return "\n".join(out)


def main(md_path: str, html_path: str, label: str, theme_name: str) -> None:
    t = THEMES[theme_name]
    md = Path(md_path).read_text(encoding="utf-8")
    body = render_body(md)

    head = (
        "<!doctype html><meta charset=\"utf-8\"><title>" + label + "</title><style>\n"
        "body{margin:0;background:" + t["bg"] + ";color:" + t["fg"] + ";"
        "font:17px/1.6 " + t["body_font"] + "}\n"
        "main{max-width:720px;margin:0 auto;padding:56px 32px 80px}\n"
        "h1{font:600 34px/1.1 " + t["head_font"] + ";letter-spacing:-.02em;margin:0 0 6px}\n"
        ".lab{font:12px/1 ui-monospace,Consolas,monospace;letter-spacing:.14em;"
        "text-transform:uppercase;color:" + t["muted"] + ";margin-bottom:40px}\n"
        "h2{font:600 13px/1 " + t["head_font"] + ";letter-spacing:.12em;text-transform:uppercase;"
        "color:" + t["muted"] + ";margin:36px 0 10px;padding-top:14px;border-top:1px solid " + t["line"] + "}\n"
        "p{margin:0 0 12px;max-width:62ch} strong{font-weight:600}\n"
        "ul{margin:0 0 12px;padding-left:20px} li{margin:4px 0}\n"
        ".btn{display:inline-block;padding:8px 14px;margin:6px 0 4px;border:1px solid " + t["accent"] + ";"
        "border-radius:4px;font:600 14px " + t["head_font"] + ";color:" + t["accent"] + "}\n"
        "</style><main><div class=\"lab\">" + label + "</div>\n"
    )
    tail = "</main>"

    Path(html_path).write_text(head + body + tail, encoding="utf-8")
    print("wrote", html_path)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
