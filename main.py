from myhtm import htm


@htm
def html(tag, props, children):
    return tag, props, children


name = "Worldssssss"

print(html("""
    <div class="main">
        Helloxyz1234, <b>{name}!</b>
    </div>
"""))
