import justpy as jp
from webapp import layout
from webapp import page

class About(page.Page):
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        
        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the About page!", classes="text-4xl m-2")
        jp.Div(a=div, text=""""Programming isn't about what you know; it's about what you can figure out.” - Chris Pine
            Especially important for beginners. At first, we're so anxious about knowing everything, especially language
             syntax.
            Problem-solving is the skill we end up using most.
            "The only way to learn a new programming language is by writing programs in it." - Dennis Ritchie
            Programmers are mostly "learn by doing" types. 
            No amount of academic study or watching other people code can compare 
            to breaking open an editor and start making mistakes.
            "Sometimes it's better to leave something alone, to pause, and that's very true of programming."
             - Joyce Wheeler
        """, classes="text-lg")
        return wp



