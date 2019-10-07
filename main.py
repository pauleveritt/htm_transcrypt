from myhtm import htm


@htm
def html(tag, props, children):
    return tag, props, children


name = "World"

print(html("""
    <div class="main">
        Hellox, <b>{name}!</b>
    </div>
"""))
