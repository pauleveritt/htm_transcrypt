from myhtm import htm


@htm
def html(tag, props, children):
    return tag, props, children


name = "World!"


def view():
    return html("""
        <div class="main">
            Hello, <b>{name}!</b>
        </div>
    """)
